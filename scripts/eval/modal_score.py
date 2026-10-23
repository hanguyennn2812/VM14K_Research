#!/usr/bin/env python3
"""
modal_score.py — score exported VM14K prompts with vLLM on a Modal H100, in bf16.

Reads a prompts JSONL written by `rag_moh.py --export` (one chat per line, with its run name and the
item's metadata) and writes one run file per run name to reports/eval/runs/, in run_eval's record
format. Two scorings:

  logit  one token with its top-20 logprobs: the probability of each option letter, renormalised,
         as the hf-logit runs do (a letter outside the top 20 counts as 0) -> vllm-logit__<model>__<run>
  gen    up to 32 greedy tokens, the letter parsed as run_eval.py does: the paper's scoring
         -> vllm-gen__<model>__<run>

Weights are downloaded once by a CPU container into the Modal volume `vm14k-hf-cache`, so the GPU
is billed only for scoring. --limit N scores the first N items of each run (smoke test) and adds
__nN to the file names.

    modal run scripts/eval/modal_score.py --model Qwen/Qwen3.8-27B --prompts <dir>/prompts.jsonl
    modal run scripts/eval/modal_score.py --model Qwen/Qwen3.8-27B --prompts <file> --mode gen --runs paper__test-all
"""
import json
import math
import os
import sys

import modal

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

app = modal.App("vm14k-score")
cache = modal.Volume.from_name("vm14k-hf-cache", create_if_missing=True)
image = (modal.Image.debian_slim(python_version="3.12")
         .pip_install("vllm==0.31.0", "hf_transfer")
         # FlashInfer's sampler JIT-compiles at startup and needs nvcc, which this image lacks; scoring is
         # greedy, so vLLM's PyTorch sampler is enough.
         .env({"HF_HOME": "/cache", "HF_HUB_ENABLE_HF_TRANSFER": "1", "VLLM_USE_FLASHINFER_SAMPLER": "0"})
         .add_local_python_source("run_eval"))


@app.function(image=image, volumes={"/cache": cache}, timeout=2 * 3600)
def fetch(model_id):
    from huggingface_hub import snapshot_download
    snapshot_download(model_id)
    cache.commit()


@app.function(image=image, gpu="H100", volumes={"/cache": cache}, timeout=3 * 3600)
def score(model_id, items, mode):
    from vllm import LLM, SamplingParams

    from run_eval import LETTERS, parse_letter

    # max_num_seqs: Qwen3.5's linear-attention layers need one state slot per running sequence, and
    # an H100 holds about 358 next to the bf16 weights; vLLM's default of 1024 fails at startup.
    llm = LLM(model=model_id, dtype="bfloat16", max_model_len=8192, gpu_memory_utilization=0.92,
              max_num_seqs=256, limit_mm_per_prompt={"image": 0, "video": 0})
    letter_ids = [llm.get_tokenizer().convert_tokens_to_ids(c) for c in LETTERS]
    params = (SamplingParams(temperature=0, max_tokens=1, logprobs=20) if mode == "logit"
              else SamplingParams(temperature=0, max_tokens=32))
    outs = llm.chat([it["messages"] for it in items], params, use_tqdm=False,
                    chat_template_kwargs={"enable_thinking": False})
    recs = []
    for it, out in zip(items, outs):
        n, o = it["n_options"], out.outputs[0]
        if mode == "logit":
            top = o.logprobs[0]
            p = [math.exp(top[t].logprob) if t in top else 0.0 for t in letter_ids[:n]]
            p = [x / sum(p) for x in p] if sum(p) else [1 / n] * n
            pred, extra = LETTERS[p.index(max(p))], {"probs": [round(x, 5) for x in p]}
        else:
            pred, extra = parse_letter(o.text, n), {"raw": o.text}
        meta = {k: v for k, v in it.items() if k not in ("messages", "run")}
        recs.append({**meta, "provider": f"vllm-{mode}", "model": model_id, "pred": pred,
                     "correct": pred == it["gold"], **extra, "error": None})
    return recs


@app.local_entrypoint()
def main(model: str, prompts: str, mode: str = "logit", runs: str = "", limit: int = 0):
    from run_eval import RUNS_DIR

    items = [json.loads(line) for line in open(prompts, encoding="utf-8")]
    wanted = [r for r in runs.split(",") if r] or list(dict.fromkeys(it["run"] for it in items))
    picked, count = [], {}
    for it in items:
        if it["run"] in wanted and (not limit or count.get(it["run"], 0) < limit):
            picked.append(it)
            count[it["run"]] = count.get(it["run"], 0) + 1
    print(f"{len(picked)} prompts, runs: {count}")
    fetch.remote(model)
    recs = score.remote(model, picked, mode)
    for run in count:
        name = f"vllm-{mode}__{model.replace('/', '_')}__{run}" + (f"__n{limit}" if limit else "")
        sel = [r for r, it in zip(recs, picked) if it["run"] == run]
        with open(os.path.join(RUNS_DIR, name + ".jsonl"), "w", encoding="utf-8") as fh:
            for rec in sel:
                fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
        print(f"{name}: n={len(sel)} acc={100 * sum(r['correct'] for r in sel) / len(sel):.1f} "
              f"unparsed={sum(r['pred'] is None for r in sel)}")
