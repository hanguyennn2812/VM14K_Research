#!/usr/bin/env python3
"""
modal_decision.py — score VM14K with off-the-shelf System One decision models on a Modal H100.

Each item becomes one Choice question built exactly as run_jev.py builds it for Jev (state = the
question, instructions = the paper's line, criteria = option letters -> option texts) and goes to the
model's own `system_one` method (transformers AutoModel, trust_remote_code), one item per call, in bf16.
Records follow run_eval's format via run_jev.to_record and are written to
reports/eval/runs/decision__<model>__choice__<split>[__shufN][__nN].jsonl. Several models run in
parallel containers. Weights are cached in the Modal volume `vm14k-hf-cache`.

    modal run scripts/eval/modal_decision.py --models vllm-sr/d3-nano --limit 20          # smoke test
    modal run scripts/eval/modal_decision.py --models vllm-sr/d3-edge,vllm-sr/d3-nano     # full test split
    modal run scripts/eval/modal_decision.py --models vllm-sr/d3-nano --shuffle-seed 1    # option-order check
"""
import json
import os
import sys
import time
from types import SimpleNamespace

import modal

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

app = modal.App("vm14k-decision")
cache = modal.Volume.from_name("vm14k-hf-cache", create_if_missing=True)
image = (modal.Image.debian_slim(python_version="3.12")
         .pip_install("transformers==5.17.0", "torch", "torchvision", "pillow", "opencv-python-headless",
                      "safetensors", "accelerate", "hf_transfer")
         .env({"HF_HOME": "/cache", "HF_HUB_ENABLE_HF_TRANSFER": "1"}))


@app.function(image=image, gpu="H100", volumes={"/cache": cache}, timeout=3600)
def decide(model_id, bodies):
    import torch
    from transformers import AutoModel

    model = AutoModel.from_pretrained(model_id, trust_remote_code=True, dtype=torch.bfloat16)
    if next(model.parameters()).device.type != "cuda":
        model = model.to("cuda")
    model.eval()
    cache.commit()
    out = []
    for body in bodies:
        t = time.time()
        try:
            resp = model.system_one(state=body["state"], questions=body["questions"])
            out.append((json.loads(json.dumps(resp, default=float)), None, time.time() - t))
        except Exception as exc:  # one bad item must not lose the run
            out.append((None, repr(exc)[:300], time.time() - t))
    return out


med_image = (modal.Image.debian_slim(python_version="3.12")
             .pip_install("transformers==5.18.0", "torch", "peft", "flash-linear-attention", "accelerate",
                          "hf_transfer")
             .env({"HF_HOME": "/cache", "HF_HUB_ENABLE_HF_TRANSFER": "1"}))


@app.function(image=med_image, gpu="H100", volumes={"/cache": cache}, timeout=3600)
def meddecide(model_id, bodies):
    """MedDecider (a LoRA on a Qwen base read at the option letters) through its own meddecider_infer.py:
    its prompt, letter ids and choice temperature, both option orders averaged as in MedDecider.decide.
    Probabilities are kept by position, so duplicate option texts stay apart. The state is the question."""
    import torch
    from huggingface_hub import snapshot_download

    path = snapshot_download(model_id)
    sys.path.insert(0, path)
    from meddecider_infer import MedDecider

    mj = MedDecider(path)
    cache.commit()
    t_choice = mj.cfg["temperature"].get("choice", 1.0)
    out = []
    for body in bodies:
        crit = body["questions"]["answer"]["criteria"]
        opts, n, t = list(crit.values()), len(crit), time.time()
        try:
            probs = torch.zeros(n)
            for order in (list(range(n)), list(range(n))[::-1]):
                ids = mj.tok(mj.prompt(None, body["state"], [opts[i] for i in order]), return_tensors="pt",
                             add_special_tokens=False).to(mj.model.device)
                with torch.no_grad():
                    z = mj.model(**ids, logits_to_keep=1).logits[0, -1, mj.letter_ids[:n]].float().cpu()
                p = torch.softmax(z / t_choice, -1)
                for pos, orig in enumerate(order):
                    probs[orig] += p[pos] / 2
            resp = {"model": model_id, "answers": {"answer": {"probabilities": dict(zip(crit, probs.tolist())),
                                                              "choice": list(crit)[int(probs.argmax())]}}}
            out.append((resp, None, time.time() - t))
        except Exception as exc:  # one bad item must not lose the run
            out.append((None, repr(exc)[:300], time.time() - t))
    return out


def add_context(bodies, split, context):
    """Put retrieved context before the question in each state, using rag_moh.py's retrieval over all
    MoH documents: `docs` = the 3 closest guideline chunks, `shots` = the 3 TF-IDF-closest train items
    with their keyed answers. Returns each item's best-chunk similarity (for gating on val)."""
    from rag_moh import DOCS_HEAD, Prompts, setup

    chunks, emb, train = setup("all")
    p = Prompts(split, "all", chunks, emb, train)
    for k, body in enumerate(bodies):
        parts = []
        if "shots" in context:
            parts.append("Solved exam questions similar to this one:\n\n" + "\n\n".join(
                f"Q: {train[j]['question']}\nA: {train[j]['options'][train[j]['answer_index']]}" for j in p.shots[k]))
        if "docs" in context:
            parts.append(DOCS_HEAD + "\n\n" + "\n\n".join(f"[{n + 1}] {chunks[j]['text']}"
                                                          for n, j in enumerate(p.top[k])))
        body["state"] = "\n\n".join(parts + ["Question: " + body["state"]])
    return [round(float(s), 4) for s in p.top_sim]


@app.local_entrypoint()
def main(models: str, split: str = "test", shuffle_seed: int = -1, limit: int = 0, context: str = "",
         items: str = ""):
    # --items FILE: score generated questions (gen_moh_mcq.py) instead of a VM14K split; --split names the run.
    # --context own: each item's own source chunk (`chunk_text`) in the state, as the CS1 teacher reads it.
    from run_eval import RUNS_DIR, load_rows, permute
    from run_jev import request_body, to_record

    seed = None if shuffle_seed < 0 else shuffle_seed
    if items:
        with open(items, encoding="utf-8") as fh:
            rows = [json.loads(line) for line in fh][:limit or None]
    else:
        rows = load_rows(split, None, 0)[:limit or None]
    prepared = [(r, *permute(r, seed)) for r in rows]  # (row, options as shown, gold index, perm)
    model_ids = [m for m in models.split(",") if m]
    jobs = [(m, [request_body(r, opts, m) for r, opts, _, _ in prepared]) for m in model_ids]
    top_sim = None
    if context == "own":
        from rag_moh import DOCS_HEAD
        for _, bodies in jobs:
            for (r, *_), body in zip(prepared, bodies):
                body["state"] = f"{DOCS_HEAD}\n\n[1] {r['chunk_text']}\n\nQuestion: {body['state']}"
    elif context:
        top_sim = [add_context(bodies, split, context) for _, bodies in jobs][0]
    calls = [(meddecide if "MedDecider" in m else decide).spawn(m, bodies) for m, bodies in jobs]  # in parallel
    for m, results in zip(model_ids, (c.get() for c in calls)):
        args = SimpleNamespace(model=m, shuffle_seed=seed, split=split)
        recs = [dict(to_record(r, gold, perm, resp, err, args, lat), provider="decision")
                for (r, _, gold, perm), (resp, err, lat) in zip(prepared, results)]
        if top_sim:
            recs = [dict(rec, context=context, top_sim=s) for rec, s in zip(recs, top_sim)]
        style = f"choice-{context}" if context else "choice"
        name = (f"decision__{m.replace('/', '_')}__{style}__{split}" + (f"__shuf{seed}" if seed is not None else "")
                + (f"__n{limit}" if limit else ""))
        with open(os.path.join(RUNS_DIR, name + ".jsonl"), "w", encoding="utf-8") as fh:
            for rec in recs:
                fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
        ok = [r for r in recs if not r["error"]]
        print(f"{name}: n={len(recs)} acc={100 * sum(r['correct'] for r in ok) / max(len(ok), 1):.1f} "
              f"errors={len(recs) - len(ok)} median_latency_ms={1000 * sorted(lat for _, _, lat in results)[len(results) // 2]:.0f}")
        if results and results[0][0]:
            print("  first answer:", json.dumps(results[0][0].get("answers"), ensure_ascii=False)[:300])
        if len(ok) < len(recs):
            print("  first error:", next(r["error"] for r in recs if r["error"])[:300])
