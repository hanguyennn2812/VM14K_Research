#!/usr/bin/env python3
"""Train a Qwen3-8B grounded QLoRA adapter on a CUDA GPU.

This trainer consumes only the evidence-gated conversational JSONL created by
``export_qwen_sft_grounded.py``.  It refuses CPU-only execution, train/validation
leakage, unverified evidence by default, and silent sequence truncation.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
import math
from datetime import UTC, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_DATA = ROOT / "data" / "derived" / "qwen_sft_grounded"
DEFAULT_OUTPUT = ROOT / "artifacts" / "qwen3_8b_grounded_qlora"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def load_jsonl(path: Path, expected_split: str, allow_uncalibrated: bool) -> list[dict]:
    if not path.exists():
        raise FileNotFoundError(f"missing SFT data: {path}")
    rows: list[dict] = []
    with path.open(encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            row = json.loads(line)
            messages = row.get("messages")
            metadata = row.get("metadata", {})
            if not isinstance(messages, list) or [m.get("role") for m in messages] != [
                "system",
                "user",
                "assistant",
            ]:
                raise ValueError(f"invalid messages at {path}:{line_number}")
            if metadata.get("split") != expected_split:
                raise ValueError(f"split mismatch at {path}:{line_number}")
            if metadata.get("support_label") != "supported":
                raise ValueError(f"unsupported row reached trainer at {path}:{line_number}")
            verification = metadata.get("verification_status")
            if (
                verification not in {"human_verified", "calibrated_auto_check"}
                and not allow_uncalibrated
            ):
                raise ValueError(
                    f"unverified evidence at {path}:{line_number}; use human/calibrated "
                    "data or explicitly opt into an exploratory run"
                )
            if not metadata.get("source_id"):
                raise ValueError(f"missing source_id at {path}:{line_number}")
            rows.append(row)
    if not rows:
        raise ValueError(f"no usable rows in {path}")
    return rows


def percentile(values: list[int], quantile: float) -> int:
    ordered = sorted(values)
    index = min(len(ordered) - 1, math.ceil(quantile * len(ordered)) - 1)
    return ordered[max(index, 0)]


def package_versions(names: list[str]) -> dict[str, str]:
    versions: dict[str, str] = {}
    for name in names:
        try:
            versions[name] = importlib.metadata.version(name)
        except importlib.metadata.PackageNotFoundError:
            versions[name] = "missing"
    return versions


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--model", default="Qwen/Qwen3-8B")
    parser.add_argument("--epochs", type=float, default=2.0)
    parser.add_argument("--learning-rate", type=float, default=1e-4)
    parser.add_argument("--max-length", type=int, default=2048)
    parser.add_argument("--gradient-accumulation", type=int, default=16)
    parser.add_argument("--lora-rank", type=int, default=16)
    parser.add_argument("--lora-alpha", type=int, default=32)
    parser.add_argument("--lora-dropout", type=float, default=0.05)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--max-steps", type=int, default=-1, help="use a small value only for a smoke run")
    parser.add_argument("--resume", action="store_true")
    parser.add_argument(
        "--allow-uncalibrated-auto-check",
        action="store_true",
        help="exploratory pilot only; train on auto-checked evidence before calibration",
    )
    args = parser.parse_args()

    try:
        import torch
        from datasets import Dataset
        from peft import LoraConfig, prepare_model_for_kbit_training
        from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
        from trl import SFTConfig, SFTTrainer
    except ImportError as exc:
        raise RuntimeError(
            "install a CUDA PyTorch build and requirements-gpu.txt before training"
        ) from exc

    if not torch.cuda.is_available():
        raise RuntimeError(
            "Qwen3-8B QLoRA requires a CUDA GPU in this reproducible path; "
            "use Colab/Kaggle/A10/L4/A100 rather than the CPU-only local PyTorch build"
        )

    data_dir = args.data_dir if args.data_dir.is_absolute() else ROOT / args.data_dir
    output_dir = args.output_dir if args.output_dir.is_absolute() else ROOT / args.output_dir
    train_path = data_dir / "train.jsonl"
    val_path = data_dir / "val.jsonl"
    train_rows = load_jsonl(
        train_path, "train", args.allow_uncalibrated_auto_check
    )
    val_rows = load_jsonl(val_path, "val", args.allow_uncalibrated_auto_check)
    train_ids = {row["metadata"]["source_id"] for row in train_rows}
    val_ids = {row["metadata"]["source_id"] for row in val_rows}
    overlap = train_ids & val_ids
    if overlap:
        raise ValueError(f"train/validation source leakage: {sorted(overlap)[:5]}")
    if output_dir.exists() and any(output_dir.iterdir()) and not args.resume:
        parser.error(f"{output_dir} is not empty; use a new path or --resume")

    tokenizer = AutoTokenizer.from_pretrained(args.model, use_fast=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "right"
    all_rows = train_rows + val_rows
    lengths = [
        len(
            tokenizer.apply_chat_template(
                row["messages"], tokenize=True, add_generation_prompt=False
            )
        )
        for row in all_rows
    ]
    longest = max(lengths)
    if longest > args.max_length:
        raise ValueError(
            f"silent truncation is forbidden: longest example is {longest} tokens but "
            f"--max-length={args.max_length}; increase --max-length or shorten evidence"
        )

    device_index = torch.cuda.current_device()
    capability = torch.cuda.get_device_capability(device_index)
    use_bf16 = bool(torch.cuda.is_bf16_supported())
    compute_dtype = torch.bfloat16 if use_bf16 else torch.float16
    quantization = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_use_double_quant=True,
        bnb_4bit_compute_dtype=compute_dtype,
    )
    model = AutoModelForCausalLM.from_pretrained(
        args.model,
        quantization_config=quantization,
        device_map={"": device_index},
        torch_dtype=compute_dtype,
        attn_implementation="sdpa",
    )
    model.config.use_cache = False
    model = prepare_model_for_kbit_training(
        model, use_gradient_checkpointing=True
    )
    peft_config = LoraConfig(
        r=args.lora_rank,
        lora_alpha=args.lora_alpha,
        lora_dropout=args.lora_dropout,
        target_modules="all-linear",
        bias="none",
        task_type="CAUSAL_LM",
    )

    output_dir.mkdir(parents=True, exist_ok=True)
    manifest = {
        "created_at_utc": datetime.now(UTC).isoformat(),
        "model": args.model,
        "purpose": "grounded answer + explanation + page citation QLoRA",
        "data": {
            "train_path": str(train_path),
            "train_sha256": sha256(train_path),
            "train_rows": len(train_rows),
            "val_path": str(val_path),
            "val_sha256": sha256(val_path),
            "val_rows": len(val_rows),
            "source_id_overlap": 0,
            "verification_gate_bypassed": args.allow_uncalibrated_auto_check,
        },
        "sequence_tokens": {
            "max": longest,
            "p50": percentile(lengths, 0.50),
            "p95": percentile(lengths, 0.95),
            "configured_max_length": args.max_length,
            "truncated_examples": 0,
        },
        "gpu": {
            "name": torch.cuda.get_device_name(device_index),
            "capability": list(capability),
            "memory_bytes": torch.cuda.get_device_properties(device_index).total_memory,
            "compute_dtype": str(compute_dtype),
        },
        "qlora": {
            "quant_type": "nf4",
            "double_quant": True,
            "target_modules": "all-linear",
            "rank": args.lora_rank,
            "alpha": args.lora_alpha,
            "dropout": args.lora_dropout,
            "assistant_only_loss": True,
        },
        "training": {
            "epochs": args.epochs,
            "max_steps": args.max_steps,
            "learning_rate": args.learning_rate,
            "per_device_train_batch_size": 1,
            "gradient_accumulation_steps": args.gradient_accumulation,
            "seed": args.seed,
            "checkpoint_selection": "lowest validation loss; test remains unopened",
        },
        "packages": package_versions(
            ["torch", "transformers", "datasets", "accelerate", "bitsandbytes", "peft", "trl"]
        ),
    }
    (output_dir / "run_manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    training_args = SFTConfig(
        output_dir=str(output_dir),
        num_train_epochs=args.epochs,
        max_steps=args.max_steps,
        learning_rate=args.learning_rate,
        lr_scheduler_type="cosine",
        warmup_ratio=0.05,
        weight_decay=0.01,
        per_device_train_batch_size=1,
        per_device_eval_batch_size=1,
        gradient_accumulation_steps=args.gradient_accumulation,
        gradient_checkpointing=True,
        gradient_checkpointing_kwargs={"use_reentrant": False},
        optim="paged_adamw_8bit",
        bf16=use_bf16,
        fp16=not use_bf16,
        tf32=capability[0] >= 8,
        max_length=args.max_length,
        assistant_only_loss=True,
        packing=False,
        eval_packing=False,
        eval_strategy="epoch",
        save_strategy="epoch",
        load_best_model_at_end=True,
        metric_for_best_model="eval_loss",
        greater_is_better=False,
        save_total_limit=2,
        logging_steps=5,
        logging_first_step=True,
        report_to="none",
        seed=args.seed,
        data_seed=args.seed,
    )
    trainer = SFTTrainer(
        model=model,
        args=training_args,
        train_dataset=Dataset.from_list(
            [{"messages": row["messages"]} for row in train_rows]
        ),
        eval_dataset=Dataset.from_list(
            [{"messages": row["messages"]} for row in val_rows]
        ),
        processing_class=tokenizer,
        peft_config=peft_config,
    )
    trainer.model.print_trainable_parameters()
    train_result = trainer.train(resume_from_checkpoint=True if args.resume else None)
    eval_metrics = trainer.evaluate()
    trainer.save_model(str(output_dir / "best_adapter"))
    tokenizer.save_pretrained(output_dir / "best_adapter")
    metrics = {"train": train_result.metrics, "validation": eval_metrics}
    (output_dir / "metrics.json").write_text(
        json.dumps(metrics, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(metrics, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
