#!/usr/bin/env python3
"""
kaggle_27b_rag.py — score rag_moh.py's prompts with Qwen3.5-27B NF4 on Kaggle (2 x T4).

The prompts (chat messages, with or without MoH excerpts and train examples) are built locally by
`python scripts/eval/rag_moh.py --export <dir>` and attached as a private Kaggle dataset, so this job
needs neither the repo nor an API. Same model, loading and letter-logit scoring as kaggle_27b.py;
one output file per run, hf-logit__Qwen_Qwen3.5-27B-bnb4__<run>.jsonl, in the order the prompts list them.

    kaggle kernels push -p <folder with this file + kernel-metadata.json>
"""
import glob
import json
import os
import subprocess
import time

MODEL = "cyberenchanter/Qwen3.5-27B-bnb-4bit"
TOKENIZER = "Qwen/Qwen3.5-27B"
NAME = "hf-logit__Qwen_Qwen3.5-27B-bnb4"
OUT = "/kaggle/working"
LETTERS = "ABCDEFG"
TOKEN_BUDGET = 4096  # padded tokens per batch


def sh(cmd):
    print("$", cmd, flush=True)
    subprocess.run(cmd, shell=True, check=True)


sh("nvidia-smi --query-gpu=name,memory.total --format=csv")
sh("pip install -q 'transformers==5.19.0' accelerate bitsandbytes")

import torch  # noqa: E402  (after the installs above)
from transformers import AutoTokenizer, BitsAndBytesConfig  # noqa: E402

tok = AutoTokenizer.from_pretrained(TOKENIZER)
tok.padding_side = "left"
quant = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4", bnb_4bit_use_double_quant=True,
                           bnb_4bit_compute_dtype=torch.float16)
kw = dict(quantization_config=quant, dtype=torch.float16, device_map="auto", max_memory={0: "14GiB", 1: "14GiB"})
try:
    from transformers import AutoModelForCausalLM
    model = AutoModelForCausalLM.from_pretrained(MODEL, **kw)
except Exception as exc:  # the checkpoint is the vision-language class; fall back to it, text-only input
    print("CausalLM load failed, using the image-text-to-text class:", repr(exc)[:300], flush=True)
    from transformers import AutoModelForImageTextToText
    model = AutoModelForImageTextToText.from_pretrained(MODEL, **kw)
model.eval()
for t in list(model.parameters()) + list(model.buffers()):
    if t.dtype == torch.bfloat16:
        t.data = t.data.to(torch.float16)
dev = model.get_input_embeddings().weight.device
letter_ids = [tok.convert_tokens_to_ids(c) for c in LETTERS]

path = glob.glob("/kaggle/input/**/prompts.jsonl", recursive=True)[0]
items = [json.loads(line) for line in open(path, encoding="utf-8")]
runs = list(dict.fromkeys(it["run"] for it in items))
print(f"{len(items)} prompts from {path}; runs: {runs}", flush=True)


def score(batch):
    enc = tok([b["text"] for b in batch], return_tensors="pt", padding=True).to(dev)
    with torch.no_grad():
        return model(**enc, logits_to_keep=1).logits[:, -1, :].float()[:, letter_ids]


for run in runs:
    todo = [it for it in items if it["run"] == run]
    for it in todo:
        it["text"] = tok.apply_chat_template(it["messages"], tokenize=False, add_generation_prompt=True,
                                             enable_thinking=False)
        it["len"] = len(tok(it["text"]).input_ids)
    todo.sort(key=lambda it: it["len"])
    batches, cur = [], []
    for it in todo:
        if cur and (len(cur) + 1) * it["len"] > TOKEN_BUDGET:
            batches.append(cur)
            cur = []
        cur.append(it)
    batches.append(cur)
    t0, recs = time.time(), []
    for n, batch in enumerate(batches):
        try:
            logits = score(batch)
        except torch.cuda.OutOfMemoryError:
            torch.cuda.empty_cache()
            logits = torch.cat([score([b]) for b in batch])
        for it, lg in zip(batch, logits):
            k = it["n_options"]
            p = torch.softmax(torch.nan_to_num(lg[:k]), 0).tolist()
            pred = LETTERS[p.index(max(p))]
            rec = {key: v for key, v in it.items() if key not in ("messages", "text", "len", "run")}
            recs.append({**rec, "provider": "hf-logit", "model": MODEL, "pred": pred, "correct": pred == it["gold"],
                         "probs": [round(x, 5) for x in p], "prompt_tokens": it["len"], "error": None})
        if n % 20 == 0:
            print(f"  {run}: {len(recs)}/{len(todo)} {time.time() - t0:.0f}s", flush=True)
    with open(os.path.join(OUT, f"{NAME}__{run}.jsonl"), "w", encoding="utf-8") as fh:
        for rec in recs:
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print(f"{run}: n={len(recs)} acc={100 * sum(r['correct'] for r in recs) / len(recs):.1f} "
          f"time={time.time() - t0:.0f}s", flush=True)
