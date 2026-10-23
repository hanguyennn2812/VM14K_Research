#!/usr/bin/env python3
"""
kaggle_27b.py — does a bigger model, or retrieved worked examples, help on VM14K? Kaggle job (2 x T4).

Qwen3.5-27B does not fit two 16 GB T4s in fp16 (55.6 GB), so this loads a 4-bit NF4 copy
(cyberenchanter/Qwen3.5-27B-bnb-4bit: standard bitsandbytes NF4 + double quant of Qwen/Qwen3.5-27B,
18 GB) with fp16 compute, split over both GPUs. Two runs, letter-logit scored like sft_mcq_lora.py:

  hf-logit__Qwen_Qwen3.5-27B-bnb4__paper__test           zero-shot, the paper's Fig. 6 prompt
  hf-logit__Qwen_Qwen3.5-27B-bnb4__fewshot3-tfidf__test  the same, preceded by the 3 most similar train
                                                          questions (TF-IDF over question + options) with
                                                          their keys, options shuffled, as earlier chat turns

The second is a cheap form of retrieval: knowledge from the train bank at answer time, no training.

    kaggle kernels push -p <folder with this file + kernel-metadata.json> --accelerator NvidiaTeslaT4
"""
import json
import os
import subprocess
import sys
import time

REPO = "https://github.com/hanguyennn2812/VM14K_Research.git"
COMMIT = "ba4e512"
MODEL = "cyberenchanter/Qwen3.5-27B-bnb-4bit"
TOKENIZER = "Qwen/Qwen3.5-27B"
NAME = "hf-logit__Qwen_Qwen3.5-27B-bnb4"
OUT = "/kaggle/working"
K_SHOTS = 3


def sh(cmd):
    print("$", cmd, flush=True)
    subprocess.run(cmd, shell=True, check=True)


sh("nvidia-smi --query-gpu=name,memory.total --format=csv && df -h / /kaggle/working | tail -2")
sh("pip install -q 'transformers==5.19.0' accelerate bitsandbytes")
sh(f"git clone -q {REPO} /tmp/repo && git -C /tmp/repo checkout -q {COMMIT}")
sh(f"python -c \"from huggingface_hub import snapshot_download; snapshot_download('{MODEL}'); "
   f"snapshot_download('{TOKENIZER}', allow_patterns=['*.json', '*.txt', '*.jinja'])\"")

import torch  # noqa: E402  (after the installs above)
from sklearn.feature_extraction.text import TfidfVectorizer  # noqa: E402
from transformers import AutoTokenizer, BitsAndBytesConfig  # noqa: E402

sys.path.insert(0, "/tmp/repo/scripts/eval")
from run_eval import LETTERS, build_prompt, load_rows, permute  # noqa: E402

tok = AutoTokenizer.from_pretrained(TOKENIZER)
tok.padding_side = "left"
quant = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4", bnb_4bit_use_double_quant=True,
                           bnb_4bit_compute_dtype=torch.float16)  # T4 has no native bf16
kw = dict(quantization_config=quant, dtype=torch.float16, device_map="auto", max_memory={0: "14GiB", 1: "14GiB"})
try:
    from transformers import AutoModelForCausalLM
    model = AutoModelForCausalLM.from_pretrained(MODEL, **kw)
except Exception as exc:  # the checkpoint is the vision-language class; fall back to it, text-only input
    print("CausalLM load failed, using the image-text-to-text class:", repr(exc)[:300], flush=True)
    from transformers import AutoModelForImageTextToText
    model = AutoModelForImageTextToText.from_pretrained(MODEL, **kw)
model.eval()
# Modules bitsandbytes leaves unquantized (lm_head, embeddings, norms) keep the checkpoint's bf16; T4 computes in fp16.
for t in list(model.parameters()) + list(model.buffers()):
    if t.dtype == torch.bfloat16:
        t.data = t.data.to(torch.float16)
dev = model.get_input_embeddings().weight.device
letter_ids = [tok.convert_tokens_to_ids(c) for c in LETTERS]
print(f"loaded {MODEL} as {type(model).__name__}; memory per GPU (GB):",
      [round(torch.cuda.memory_allocated(i) / 1e9, 1) for i in range(torch.cuda.device_count())], flush=True)

test, train = load_rows("test", None, 0), load_rows("train", None, 0)
text = lambda r: r["question"] + " " + " ".join(r["options"])  # noqa: E731
vec = TfidfVectorizer(ngram_range=(1, 2), sublinear_tf=True).fit([text(r) for r in train + test])
sim = (vec.transform([text(r) for r in test]) @ vec.transform([text(r) for r in train]).T).toarray()
print("retrieval done", sim.shape, flush=True)


def chat(row, shots):
    msgs = []
    for ex in shots:  # least similar first, so the closest example sits next to the question
        options, gold, _ = permute(ex, "fewshot")
        msgs += [{"role": "user", "content": build_prompt("paper", ex["question"], options)},
                 {"role": "assistant", "content": LETTERS[gold]}]
    msgs.append({"role": "user", "content": build_prompt("paper", row["question"], row["options"])})
    return tok.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True, enable_thinking=False)


def run(name, style, shots_for, batch):
    t0, recs, bad = time.time(), [], 0
    items = sorted(((r, chat(r, shots_for(k))) for k, r in enumerate(test)), key=lambda x: len(x[1]))
    for s in range(0, len(items), batch):
        chunk = items[s:s + batch]
        enc = tok([c[1] for c in chunk], return_tensors="pt", padding=True).to(dev)
        with torch.no_grad():
            logits = model(**enc, logits_to_keep=1).logits[:, -1, :].float()[:, letter_ids]
        for (r, _), lg in zip(chunk, logits):
            n = len(r["options"])
            bad += int(not torch.isfinite(lg[:n]).all())
            p = torch.softmax(torch.nan_to_num(lg[:n]), 0).tolist()
            k = p.index(max(p))
            recs.append({"id": r["id"], "provider": "hf-logit", "model": MODEL, "prompt_style": style, "think": False,
                         "shuffle_seed": None, "split": "test", "medical_topic": r["medical_topic"],
                         "difficulty_level": r["difficulty_level"], "n_options": n, "perm": list(range(n)),
                         "gold": LETTERS[r["answer_index"]], "pred": LETTERS[k], "correct": k == r["answer_index"],
                         "probs": [round(x, 5) for x in p], "error": None})
        if (s // batch) % 50 == 0:
            print(f"  {name}: {len(recs)}/{len(items)} {time.time() - t0:.0f}s", flush=True)
    with open(os.path.join(OUT, name + ".jsonl"), "w", encoding="utf-8") as fh:
        for rec in recs:
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
    acc = sum(r["correct"] for r in recs) / len(recs)
    print(f"{name}: n={len(recs)} acc={100 * acc:.1f} pickA={100 * sum(r['pred'] == 'A' for r in recs) / len(recs):.1f}"
          f" non-finite={bad} time={time.time() - t0:.0f}s", flush=True)


run(f"{NAME}__paper__test", "paper", lambda k: [], batch=8)
top = sim.argsort(axis=1)[:, ::-1][:, :K_SHOTS]
run(f"{NAME}__fewshot3-tfidf__test", "fewshot3-tfidf", lambda k: [train[j] for j in top[k][::-1]], batch=4)
