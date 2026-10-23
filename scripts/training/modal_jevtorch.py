#!/usr/bin/env python3
"""Prepared VM14K jev-torch training job; importing this file does not launch it.

    python scripts/training/jevtorch_data.py --out data/derived/jevtorch
    modal run scripts/training/modal_jevtorch.py --data data/derived/jevtorch

One H100, one epoch of BF16 LoRA, validation-only temperature fitting, then
original-order test probabilities in run_eval format. No Hub or W&B uploads.
"""

import hashlib
import json
import math
from pathlib import Path
import uuid

import modal


JEVTORCH_COMMIT = "96b1f101d90d6b878804000d67645b8ee0631227"
MODEL_ID = "Qwen/Qwen3.5-2B"
LETTERS = "ABCDE"  # two train items have five options
INSTRUCTION = "Choose the correct option from these answers"
MAX_LENGTH = 2048
TIMEOUT = 2 * 3600
RESULT_NAME = "jevtorch__Qwen_Qwen3.5-2B__choice__test.jsonl"

app = modal.App("vm14k-jevtorch")
cache = modal.Volume.from_name("vm14k-hf-cache", create_if_missing=True)

# UNVERIFIED RUNTIME: this Modal image has not been built or GPU-tested. CUDA
# 12.8 / torch 2.8 match upstream's tested RunPod stack. The devel image supplies
# nvcc: upstream requires TileLang + nvcc for correct FLA backward on H100 with
# Triton 3.4. This is BF16 LoRA, not the upstream-unvalidated QLoRA path.
image = (
    modal.Image.from_registry(
        "nvidia/cuda:12.8.1-cudnn-devel-ubuntu24.04", add_python="3.12"
    )
    .apt_install("git", "build-essential")
    .pip_install("torch==2.8.0", index_url="https://download.pytorch.org/whl/cu128")
    .pip_install(
        "torch==2.8.0",  # Keep the CUDA stack while resolving jev-torch extras.
        f"jev-torch[cuda] @ git+https://github.com/smha1012/jev-torch.git@{JEVTORCH_COMMIT}",
    )
    .env({"HF_HOME": "/cache", "TOKENIZERS_PARALLELISM": "false",
          "CUDA_HOME": "/usr/local/cuda", "JEV_OVERRIDES": "",
          "WANDB_MODE": "disabled", "PYTORCH_CUDA_ALLOC_CONF": "expandable_segments:True"})
)


def native_item(item):
    """Translate the requested keyed export to the verified JEVExample schema.

    Upstream schema.py/collate.py require list[str], and use `question` for
    instructions. Passing a dict directly would score its keys as option text.
    Extra fields (id, perm, medical_topic, etc.) survive in JEVExample.meta.
    """
    n = len(item["options"])
    keys = list(LETTERS[:n])
    if not 2 <= n <= len(LETTERS) or list(item["options"]) != keys:
        raise ValueError(f"{item.get('id')}: expected ordered A-E option keys")
    if item["kind"] != "choice" or item["instructions"] != INSTRUCTION:
        raise ValueError(f"{item['id']}: unexpected kind/instructions")
    label = item["label"]
    if not isinstance(label, int) or not 0 <= label < n:
        raise ValueError(f"{item['id']}: invalid hard label")
    if item["target"] != [float(i == label) for i in range(n)]:
        raise ValueError(f"{item['id']}: target must be one-hot at label")
    if sorted(item["perm"]) != list(range(n)):
        raise ValueError(f"{item['id']}: invalid permutation")
    return {**item, "question": item["instructions"],
            "options": [item["options"][key] for key in keys]}


@app.function(image=image, volumes={"/cache": cache}, timeout=TIMEOUT, retries=0)
def fetch():
    """Download on CPU before starting GPU billing; return an immutable snapshot."""
    from huggingface_hub import snapshot_download

    snapshot = snapshot_download(MODEL_ID)
    cache.commit()
    return snapshot


@app.function(image=image, gpu="H100", volumes={"/cache": cache},
              timeout=TIMEOUT, retries=0, scaledown_window=2)
def train_and_score(splits, model_snapshot, seed, run_id):
    import os
    import subprocess
    import sys

    import torch
    import yaml

    # APIs below were read at JEVTORCH_COMMIT: config.py, train.py, trainer.py,
    # schema.py and predict.py. No guessed CLI flags or calibration command.
    # UNVERIFIED: dependency resolution and actual 2B training/inference on Modal.
    import fla
    from jev import JEVPredictor
    from jev.schema import JEVExample, KINDS

    if not torch.cuda.is_available() or not torch.cuda.is_bf16_supported():
        raise RuntimeError("This job requires a CUDA GPU with BF16 support")
    if torch.__version__.split("+")[0] != "2.8.0" or torch.version.cuda != "12.8":
        raise RuntimeError(f"Unexpected torch/CUDA stack: {torch.__version__}/{torch.version.cuda}")
    # Fail before training if the Hopper-safe backward backend cannot load.
    import fla.utils as fla_utils
    if (fla_utils.IS_NVIDIA_HOPPER and fla_utils.TRITON_ABOVE_3_4_0
            and not fla_utils.TRITON_ABOVE_3_7_1):
        from fla.ops.common.backends.tilelang import TileLangBackend
        if not (TileLangBackend.is_available() and TileLangBackend.is_enabled()):
            raise RuntimeError("H100 + this Triton version requires the FLA TileLang backend and nvcc")
    print(f"torch={torch.__version__}, fla={getattr(fla, '__version__', '?')}", flush=True)

    # Unique directory avoids collisions with Claude's simultaneous cache use.
    work = Path("/cache/jevtorch-vm14k") / run_id
    data_dir, output = work / "data", work / "run"
    data_dir.mkdir(parents=True, exist_ok=False)
    native = {split: [native_item(item) for item in items] for split, items in splits.items()}

    # Fixed 50/50 development/calibration partition of frozen val, independent
    # of training seed. Test is never passed to the trainer or temperature fit.
    ordered_val = sorted(native["val"], key=lambda x: hashlib.sha256(str(x["id"]).encode()).digest())
    cut = len(ordered_val) // 2
    staged = {"train": native["train"], "validation": ordered_val[:cut],
              "calibration": ordered_val[cut:], "test": native["test"]}
    for split, items in staged.items():
        with (data_dir / f"{split}.jsonl").open("w", encoding="utf-8") as fh:
            for item in items:
                fh.write(json.dumps(item, ensure_ascii=False) + "\n")
    config = {
        "model": {"name": model_snapshot, "lora_r": 16, "lora_alpha": 32,
                  "lora_dropout": 0.05, "gradient_checkpointing": True, "load_in_4bit": False},
        "data": {"source": "jsonl", "path": str(data_dir), "train_split": "train",
                 "val_split": "validation", "calib_split": "calibration", "eval_splits": [],
                 "max_length": MAX_LENGTH, "shuffle_prob": 0.0},
        "train": {"output_dir": str(output), "num_gpus": 1, "epochs": 1, "max_steps": None,
                  "global_batch_size": 32, "micro_batch_size": 4, "eval_batch_size": 8,
                  "lr": 1e-4, "head_lr": 2e-4, "loss": {"ce": 1.0},
                  "dtype": "bfloat16", "device": "cuda", "seed": seed,
                  "eval_every": 1000000, "save_every": 100, "log_every": 10,
                  "val_max_examples": None, "num_workers": 0,
                  "hf_push": None, "wandb_project": None, "export_vllm": False},
    }
    # CE is supported upstream. For our one-hot targets, KL has the same
    # objective; adding both would merely duplicate it. The data is already
    # shuffled, so disable upstream's additional random option augmentation.
    config_path = work / "vm14k.yaml"
    config_path.write_text(yaml.safe_dump(config, sort_keys=False), encoding="utf-8")
    (work / "pip-freeze.txt").write_text(
        subprocess.check_output([sys.executable, "-m", "pip", "freeze"], text=True), encoding="utf-8")
    (work / "provenance.json").write_text(json.dumps({
        "jevtorch_commit": JEVTORCH_COMMIT, "model_id": MODEL_ID,
        "model_snapshot": model_snapshot, "seed": seed,
        "counts": {k: len(v) for k, v in staged.items()},
    }, indent=2), encoding="utf-8")
    cache.commit()
    print(f"artifacts: {work}; split counts: { {k: len(v) for k, v in staged.items()} }", flush=True)

    # train.main() calls fit(), then calibrate_and_report(): selects between
    # step 0 and epoch end on development KL, fits choice temperature on the
    # calibration half of val, and saves it in run/best/head.pt. Subprocess
    # exit releases training GPU memory before loading the calibrated model.
    env = {**os.environ, "HF_HUB_OFFLINE": "1", "JEV_OVERRIDES": ""}
    try:
        subprocess.run([sys.executable, "-m", "jev.train", "--config", str(config_path)],
                       check=True, cwd=str(work), env=env)
    finally:
        cache.commit()

    predictor = JEVPredictor(str(output / "best"), device="cuda",
                             max_length=MAX_LENGTH, batch_size=8)
    temperature = float(predictor.temperature[KINDS.index("choice")])
    if not math.isfinite(temperature) or temperature <= 0:
        raise ValueError(f"invalid fitted temperature: {temperature}")
    print(f"choice temperature={temperature:.6f}", flush=True)
    records = []
    for start in range(0, len(native["test"]), 8):
        batch = native["test"][start:start + 8]
        examples = [JEVExample.from_dict(item) for item in batch]
        try:
            # Use logits rather than predict_batch's text-keyed dict: duplicate
            # answer texts must still have separate A-D probabilities.
            logits = predictor.logits(examples)
            probabilities = [torch.softmax(lg / temperature, dim=-1).tolist() for lg in logits]
            if len(probabilities) != len(batch) or any(
                len(p) != len(item["options"]) or not all(math.isfinite(v) for v in p)
                or abs(sum(p) - 1.0) > 1e-5 for item, p in zip(batch, probabilities)
            ):
                raise ValueError("invalid test probabilities")
            error = None
        except (RuntimeError, ValueError) as exc:
            probabilities = [None] * len(batch)
            error = f"{type(exc).__name__}: {exc}"[:1000]
        for item, probs in zip(batch, probabilities):
            n = len(item["options"])
            gold = LETTERS[item["label"]]
            pred = LETTERS[max(range(n), key=lambda i: probs[i])] if probs is not None else None
            records.append({
                "id": item["id"], "gold": gold, "pred": pred, "correct": pred == gold,
                "probs": probs, "n_options": n, "perm": item["perm"],
                "medical_topic": item["medical_topic"], "difficulty_level": item["difficulty_level"],
                "error": error, "provider": "jevtorch", "model": MODEL_ID,
                "split": "test", "prompt_style": "choice", "temperature": temperature,
                "seed": seed, "jevtorch_commit": JEVTORCH_COMMIT, "run_id": run_id,
            })
    with (work / RESULT_NAME).open("w", encoding="utf-8") as fh:
        for record in records:
            fh.write(json.dumps(record, ensure_ascii=False, allow_nan=False) + "\n")
    cache.commit()
    return records


@app.local_entrypoint()
def main(data: str = "data/derived/jevtorch", seed: int = 42, limit: int = 0):
    # --limit N keeps the first N items of every split: a cheap smoke run of image, kernels and scoring.
    repo_root = Path(__file__).resolve().parents[2]
    name = RESULT_NAME.replace(".jsonl", f"__n{limit}.jsonl") if limit else RESULT_NAME
    destination = repo_root / "reports" / "eval" / "runs" / name
    if destination.exists():
        raise FileExistsError(f"Refusing to overwrite {destination}; archive it before a new run")
    splits, seen = {}, set()
    for split in ("train", "val", "test"):
        with (Path(data) / f"{split}.jsonl").open(encoding="utf-8") as fh:
            items = [json.loads(line) for line in fh if line.strip()]
        ids = {item["id"] for item in items}
        if not items or len(ids) != len(items) or seen.intersection(ids):
            raise ValueError(f"{split}: empty split, duplicate id, or split overlap")
        for item in items:
            native_item(item)  # Validate the export before any paid remote calls.
            if item["split"] != split:
                raise ValueError(f"{item['id']}: wrong split")
            if split != "train" and item["perm"] != list(range(len(item["options"]))):
                raise ValueError(f"{item['id']}: held-out options must retain original order")
            if split == "train" and item["shuffle_seed"] != seed:
                raise ValueError("--seed must match jevtorch_data.py --seed")
        splits[split] = items[:limit or None]
        seen.update(ids)
    if len(splits["val"]) < 2:
        raise ValueError("Need at least two validation items for development/calibration")
    run_id = uuid.uuid4().hex
    model_snapshot = fetch.remote()
    records = train_and_score.remote(splits, model_snapshot, seed, run_id)
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("x", encoding="utf-8") as fh:
        for record in records:
            fh.write(json.dumps(record, ensure_ascii=False, allow_nan=False) + "\n")
    print(f"{destination}: n={len(records)} acc={sum(r['correct'] for r in records) / len(records):.4f} "
          f"errors={sum(r['error'] is not None for r in records)}")
    print(f"Checkpoint/config/calibration report: vm14k-hf-cache:/jevtorch-vm14k/{run_id}/run")
