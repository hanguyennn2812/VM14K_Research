#!/usr/bin/env python3
"""
kaggle_decision.py — score export_context_bodies.py's Choice requests with vllm-sr/d3-flash (9B) on Kaggle 2 x T4.

The plan's AutoModel.from_pretrained(dtype=float16, device_map=...) is refused by d3's remote code (BF16 fixed,
one device), and the BF16 9B backbone (~19 GB) does not fit one T4. So this loads the checkpoint through the
d3 runtime itself (d3_runtime.D3) with its backbone loader patched to fp16 over both GPUs, its fast path off
(plain transformers path), and the readout moved to the last GPU. That is a numerical deviation from the
H100 bf16 runs, which is why a smoke gate comes first: the first SMOKE_N `val-infect__zero` predictions must
agree >= 95% with reference_zero_val.json (the H100 bf16 predictions) and contain no NaN, else the job stops.

Inputs (private dataset): bodies.jsonl, reference_zero_val.json. Outputs in /kaggle/working:
d3flash__<run>.jsonl (records like run_jev.to_record plus the body's metadata) and smoke.json.
`ONLY` / `LIMIT` below are set by sed at push time (smoke kernel: one run, 50 items).

    python scripts/eval/kaggle_decision.py --selfcheck      # local, no GPU
"""
import glob
import json
import math
import os
import subprocess
import sys
import time

MODEL = "vllm-sr/d3-flash"
OUT = "/kaggle/working"
LETTERS = "ABCDEFG"
SMOKE_N, SMOKE_MIN = 50, 0.95
ONLY = None  # @@ONLY@@  list of run names, or None for all (in file order)
LIMIT = None  # @@LIMIT@@  first N items of each run, or None
META_DROP = ("state", "questions", "run", "model")


def agreement(preds, ref):
    """Share of ids whose prediction equals the reference; NaN-free check is the caller's."""
    ids = [i for i in preds if i in ref]
    return sum(preds[i] == ref[i] for i in ids) / len(ids) if ids else 0.0


def to_record(item, resp, err, latency):
    """A run_jev.to_record-style record from a system_one response (or an error), plus the body's metadata."""
    n = item["n_options"]
    rec = {**{k: v for k, v in item.items() if k not in META_DROP}, "provider": "decision",
           "model": item["model"], "prompt_style": "paper-choice", "think": False, "shuffle_seed": None,
           "perm": list(range(n)), "pred": None, "correct": False, "probs": None, "latency_s": round(latency, 3),
           "error": err}
    if err is None:
        ans = (resp.get("answers") or {}).get("answer") or {}
        raw = ans.get("probabilities") or {}
        probs = [float(raw.get(LETTERS[i], 0.0)) for i in range(n)]
        if not sum(probs) or any(math.isnan(p) for p in probs):
            rec["error"] = "no/NaN probabilities: " + json.dumps(resp, ensure_ascii=False)[:200]
            return rec
        choice = ans.get("choice")
        pred = choice if choice in LETTERS[:n] else LETTERS[probs.index(max(probs))]
        rec.update(pred=pred, correct=pred == item["gold"], probs=[round(p, 5) for p in probs])
    return rec


def selfcheck():
    item = {"id": "x", "run": "r", "cond": "zero", "state": "s", "questions": {}, "model": MODEL, "gold": "B",
            "n_options": 3, "top_sim": 0.4}
    ok = to_record(item, {"answers": {"answer": {"probabilities": {"A": .1, "B": .7, "C": .2}, "choice": "B"}}}, None, 1)
    assert ok["pred"] == "B" and ok["correct"] and ok["probs"] == [.1, .7, .2] and "state" not in ok and ok["top_sim"] == .4
    bad = to_record(item, {"answers": {"answer": {"probabilities": {"A": float("nan"), "B": 1, "C": 0}}}}, None, 1)
    assert bad["error"] and not bad["correct"] and bad["pred"] is None
    assert to_record(item, None, "boom", 1)["error"] == "boom"
    assert agreement({"a": "A", "b": "B"}, {"a": "A", "b": "C", "z": "A"}) == 0.5 and agreement({}, {}) == 0.0
    print("kaggle_decision selfcheck ok")


def sh(cmd):
    print("$", cmd, flush=True)
    subprocess.run(cmd, shell=True, check=True)


def load_d3():
    """D3 runtime with the fp16 two-GPU backbone and no fast path."""
    import torch
    from huggingface_hub import snapshot_download

    root = snapshot_download(MODEL, local_dir="/kaggle/temp/d3-flash", ignore_patterns=["assets/*"])
    sys.path.insert(0, root)
    import d3_runtime

    d3_runtime.d3_fast = None

    def no_fast(_root):
        raise RuntimeError("fast path disabled on T4")

    d3_runtime.fast_module = no_fast
    stock = d3_runtime.backbone_class

    def fp16_backbone(kind):
        cls = stock(kind)

        class Fp16:
            @staticmethod
            def from_pretrained(path, **kw):
                m = cls.from_pretrained(path, dtype=torch.float16, attn_implementation="sdpa", device_map="auto",
                                        max_memory={0: "13GiB", 1: "14GiB"})
                for t in list(m.parameters()) + list(m.buffers()):  # buffers the loader leaves in bf16
                    if t.dtype == torch.bfloat16:
                        t.data = t.data.to(torch.float16)
                return m
        return Fp16

    d3_runtime.backbone_class = fp16_backbone
    d3 = d3_runtime.D3.from_pretrained(root, device="cuda:0", verify="none", batch_size=1)
    last = torch.device("cuda:1" if torch.cuda.device_count() > 1 else "cuda:0")
    d3.device, d3.readout = last, d3.readout.to(last)  # hidden states leave the backbone on its last GPU
    print("d3 loaded; gpus:", torch.cuda.device_count(), flush=True)
    return d3


def main():
    sh("nvidia-smi --query-gpu=name,memory.total --format=csv")
    sh("pip install -q 'transformers==5.17.0' accelerate safetensors pillow opencv-python-headless torchvision "
       "einops huggingface_hub")
    d3 = load_d3()
    data = os.path.dirname(glob.glob("/kaggle/input/**/bodies.jsonl", recursive=True)[0])
    with open(os.path.join(data, "bodies.jsonl"), encoding="utf-8") as fh:
        items = [json.loads(line) for line in fh]
    with open(os.path.join(data, "reference_zero_val.json"), encoding="utf-8") as fh:
        ref = json.load(fh)
    runs = [r for r in dict.fromkeys(it["run"] for it in items) if ONLY is None or r in ONLY]
    print(f"{len(items)} bodies; runs: {runs}", flush=True)
    for n, run in enumerate(runs):
        todo = [it for it in items if it["run"] == run][:LIMIT]
        t0, recs = time.time(), []
        for k, it in enumerate(todo):
            t = time.time()
            try:
                resp, err = d3.system_one(state=it["state"], questions=it["questions"]), None
                resp = json.loads(json.dumps(resp, default=float))
            except Exception as exc:  # one bad item must not lose the run
                resp, err = None, repr(exc)[:300]
            recs.append(to_record(it, resp, err, time.time() - t))
            if k % 25 == 0:
                print(f"  {run}: {k + 1}/{len(todo)} {time.time() - t0:.0f}s", flush=True)
        with open(os.path.join(OUT, f"d3flash__{run}.jsonl"), "w", encoding="utf-8") as fh:
            for rec in recs:
                fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
        ok = [r for r in recs if not r["error"]]
        print(f"{run}: n={len(recs)} acc={100 * sum(r['correct'] for r in ok) / max(len(ok), 1):.1f} "
              f"errors={len(recs) - len(ok)} time={time.time() - t0:.0f}s", flush=True)
        if n == 0 and run == "val-infect__zero":  # the smoke gate
            head = recs[:SMOKE_N]
            agree = agreement({r["id"]: r["pred"] for r in head}, ref)
            smoke = {"n": len(head), "agreement": agree, "errors": sum(bool(r["error"]) for r in head),
                     "median_latency_s": sorted(r["latency_s"] for r in head)[len(head) // 2]}
            print("SMOKE", smoke, flush=True)
            with open(os.path.join(OUT, "smoke.json"), "w") as fh:
                json.dump(smoke, fh)
            if agree < SMOKE_MIN or smoke["errors"]:
                sys.exit(f"smoke gate failed: agreement {agree:.2f}, errors {smoke['errors']}")


if __name__ == "__main__":
    if "--selfcheck" in sys.argv:
        selfcheck()
    else:
        main()
