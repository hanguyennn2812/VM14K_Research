#!/usr/bin/env python3
"""
kaggle_jev9b.py — an open-weights stand-in for Jev on the VM14K test split, run on Kaggle (2 x T4).

autotrust/JEV-9B (Apache-2.0) is a student of TypeSafe Jev 1.13: its card reports a mean KL of 0.019
to Jev's own output distributions. Its language backbone is bit-identical to Qwen3.5-9B, and a LoRA
adapter plus a 24-slot head turn one prefill pass into a probability per option. Three runs, written
in run_eval's record format so analyze_jev.py reads them:

  hf-logit__Qwen_Qwen3.5-9B__paper__test        the backbone alone: letter probabilities after the paper's prompt
  jev9b__autotrust_JEV-9B__choice__test         JEV-9B's System 1 head (E2)
  jev9b__autotrust_JEV-9B__choice__test__shuf1  the same with options shuffled (E5)

T4s have no native bf16, so the 18 GB of weights load in fp16 across both GPUs. The card's own
example (refund question, expected P(true) = 0.991) is checked first to catch fp16 trouble.

    kaggle kernels push -p <folder with this file + kernel-metadata.json> --accelerator NvidiaTeslaT4
"""
import json
import os
import subprocess
import sys
import time

REPO = "https://github.com/hanguyennn2812/VM14K_Research.git"
COMMIT = "d1f622d"
MODEL = "autotrust/JEV-9B"
OUT = "/kaggle/working"
INSTRUCTION = "Choose the correct option from these answers"  # same as run_jev.py


def sh(cmd):
    print("$", cmd, flush=True)
    subprocess.run(cmd, shell=True, check=True)


sh("nvidia-smi --query-gpu=name,memory.total --format=csv")
sh("pip install -q 'transformers==5.19.0' 'peft==0.21.2' accelerate")
sh("pip uninstall -y -q torchao")  # Kaggle's torchao 0.10 makes peft 0.21 refuse to import
sh(f"git clone -q {REPO} /tmp/repo && git -C /tmp/repo checkout -q {COMMIT}")
sh(f"python -c \"from huggingface_hub import snapshot_download; snapshot_download('{MODEL}', "
   f"ignore_patterns=['vl/*', 'videos/*', 'adapter_vllm/*', 'reports/*', 'assets/*', '*.mp4', '*.png', '*.jpg'])\"")

import torch  # noqa: E402  (after the installs above)
from huggingface_hub import hf_hub_download  # noqa: E402
from peft import PeftModel  # noqa: E402
from safetensors.torch import load_file  # noqa: E402
from transformers import AutoModelForCausalLM, AutoTokenizer  # noqa: E402

sys.path.insert(0, "/tmp/repo/scripts/eval")
from run_eval import LETTERS, build_prompt, load_rows, permute  # noqa: E402

tok = AutoTokenizer.from_pretrained(MODEL)
tok.padding_side = "left"
model = AutoModelForCausalLM.from_pretrained(MODEL, dtype=torch.float16, device_map="auto",
                                             max_memory={0: "13GiB", 1: "14GiB"})
model.eval()
dev = model.get_input_embeddings().weight.device
rows = load_rows("test", None, 0)
print(f"loaded {MODEL} in fp16 over {torch.cuda.device_count()} GPUs; {len(rows)} test rows", flush=True)


def batches(items, size, key):
    items = sorted(items, key=key)
    return [items[i:i + size] for i in range(0, len(items), size)]


def save(name, recs):
    with open(os.path.join(OUT, name + ".jsonl"), "w", encoding="utf-8") as fh:
        for r in recs:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    acc = sum(r["correct"] for r in recs) / len(recs)
    pick_a = sum(r["pred"] == "A" for r in recs) / len(recs)
    print(f"{name}: n={len(recs)} acc={100 * acc:.1f} pickA={100 * pick_a:.1f}", flush=True)


def record(row, gold, perm, probs, provider, model_name, style, seed):
    n = len(perm)
    k = probs.index(max(probs))
    orig = [0.0] * n
    for i, p in enumerate(probs):
        orig[perm[i]] = p
    return {"id": row["id"], "provider": provider, "model": model_name, "prompt_style": style, "think": False,
            "shuffle_seed": seed, "split": "test", "medical_topic": row["medical_topic"],
            "difficulty_level": row["difficulty_level"], "n_options": n, "perm": perm, "gold": LETTERS[gold],
            "pred": LETTERS[k], "correct": k == gold, "probs": [round(p, 5) for p in probs],
            "probs_orig": [round(p, 5) for p in orig], "confidence": round(max(probs), 5), "error": None}


# 1. Backbone alone (System 2 weights, adapter not attached): letter probabilities after the paper prompt.
t0 = time.time()
letter_ids = [tok.convert_tokens_to_ids(c) for c in LETTERS]
items = []
for r in rows:
    msgs = [{"role": "user", "content": build_prompt("paper", r["question"], r["options"])}]
    items.append((r, tok.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True, enable_thinking=False)))
recs, nan = [], 0
for chunk in batches(items, 8, key=lambda x: len(x[1])):
    enc = tok([c[1] for c in chunk], return_tensors="pt", padding=True).to(dev)
    with torch.no_grad():
        logits = model(**enc, logits_to_keep=1).logits[:, -1, :].float()[:, letter_ids]
    for (r, _), lg in zip(chunk, logits):
        n = len(r["options"])
        nan += int(not torch.isfinite(lg[:n]).all())
        p = torch.softmax(torch.nan_to_num(lg[:n]), 0).tolist()
        recs.append(record(r, r["answer_index"], list(range(n)), p, "hf-logit", "Qwen/Qwen3.5-9B (JEV-9B backbone)",
                           "paper", None))
print(f"backbone done in {time.time() - t0:.0f}s, non-finite rows: {nan}", flush=True)
save("hf-logit__Qwen_Qwen3.5-9B__paper__test", recs)

# 2. JEV-9B System 1: LoRA adapter merged into the backbone, then the 24-slot head on the last hidden state.
model = PeftModel.from_pretrained(model, MODEL, subfolder="adapter").merge_and_unload()
head = load_file(hf_hub_download(MODEL, "head.safetensors"))
cfg = json.load(open(hf_hub_download(MODEL, "judge_config.json")))
temp = json.load(open(hf_hub_download(MODEL, "calibration.json")))["per_kind"]
W, b = head["proj.weight"].float(), head["proj.bias"].float()


def decide(kind, states, question, options_list):
    texts = []
    for state, options in zip(states, options_list):
        lines = options if kind != "choice" else [f"{LETTERS[i]}) {o}" for i, o in enumerate(options)]
        texts.append(f"[kind] {kind}\n[state] {state}\n[question] {question}\n[options]\n" + "\n".join(lines)
                     + "\n[decision]:")
    ids = tok(texts, return_tensors="pt", padding=True, add_special_tokens=False).to(dev)
    with torch.no_grad():
        h = model.model(**ids).last_hidden_state[:, -1].float()
    z = (h @ W.to(h.device).T + b.to(h.device)) / temp[kind]
    s = cfg["slots"]["ranges"][kind][0]
    return [torch.softmax(torch.nan_to_num(z[j, s:s + len(opts)]), 0).tolist() for j, opts in enumerate(options_list)]


check = decide("noul", ["Customer says the parcel arrived damaged and wants their money back."],
               "Is the customer asking for a refund?", [["false", "true"]])[0]
pair = decide("noul", ["Customer says the parcel arrived damaged and wants their money back.",
                       "A much longer second state so that the first one is left-padded in this batch of two."],
              "Is the customer asking for a refund?", [["false", "true"]] * 2)[0]
print(f"fp16 check: P(true) = {check[1]:.3f} (card: 0.991); padded batch: {pair[1]:.3f}", flush=True)
if abs(check[1] - 0.991) > 0.05 or abs(pair[1] - check[1]) > 0.02:
    print("WARNING: fp16 check off; treat the JEV-9B runs below with suspicion", flush=True)

for seed in (None, 1):
    t0 = time.time()
    items = []
    for r in rows:
        options, gold, perm = permute(r, seed)
        items.append((r, options, gold, perm))
    recs = []
    for chunk in batches(items, 8, key=lambda x: len(x[0]["question"]) + sum(map(len, x[1]))):
        probs = decide("choice", [c[0]["question"] for c in chunk], INSTRUCTION, [c[1] for c in chunk])
        for (r, options, gold, perm), p in zip(chunk, probs):
            recs.append(record(r, gold, perm, p, "jev9b", MODEL, "jev9b-choice", seed))
    print(f"JEV-9B seed={seed} done in {time.time() - t0:.0f}s", flush=True)
    save("jev9b__autotrust_JEV-9B__choice__test" + ("" if seed is None else f"__shuf{seed}"), recs)
