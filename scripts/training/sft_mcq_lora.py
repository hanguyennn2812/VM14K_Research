#!/usr/bin/env python3
"""
sft_mcq_lora.py — LoRA fine-tune a small Hugging Face model on the VM14K train
split, and score it on test the same way before and after.

Scoring reads the next-token logits of the option letters right after the
paper's Fig. 6 prompt (chat template, thinking off): pred = argmax over the
valid letters, and the softmax over those letters is kept as the model's
probability, for calibration. Nothing is generated, so nothing goes unparsed.
That differs from run_eval.py (greedy generation, then parse), so compare a
fine-tuned run only with the zero-shot run of the same model scored here.

Training puts one cross-entropy term per question on the gold letter at that
same position; the prompt itself is not trained on. --shuffle permutes the
options per example and per epoch, so the model cannot learn the release's
answer-position bias (the key is A in ~30% of rows). Rows flagged
contradiction_pending_review are never used, as in run_eval.py.

    python scripts/training/sft_mcq_lora.py eval  --model Qwen/Qwen3.5-2B
    python scripts/training/sft_mcq_lora.py train --model Qwen/Qwen3.5-2B --shuffle --out F:/ft/q35-2b-shuf
    python scripts/training/sft_mcq_lora.py eval  --model Qwen/Qwen3.5-2B --adapter F:/ft/q35-2b-shuf
"""
import argparse
import json
import math
import os
import random
import sys
import time

import torch

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "eval"))
from run_eval import LETTERS, RUNS_DIR, build_prompt, load_rows, permute  # noqa: E402

# Projection names of Qwen3 / Qwen3.5 text layers (attention, Gated DeltaNet, MLP).
LORA_TARGETS = r".*(language_model|model\.layers).*\.(q_proj|k_proj|v_proj|o_proj|in_proj_qkv|in_proj_z|out_proj|gate_proj|up_proj|down_proj)"


def pick_device(name):
    if name != "auto":
        return name
    if torch.cuda.is_available():
        return "cuda"
    return "xpu" if hasattr(torch, "xpu") and torch.xpu.is_available() else "cpu"


def amp_dtype(device):
    """fp16 autocast on CUDA cards without native bf16 (T4, P100); None elsewhere."""
    if device.startswith("cuda") and torch.cuda.get_device_capability()[0] < 8:
        return torch.float16
    return None


def load(model_id, device, adapter=None, split_fp16=False):
    from transformers import AutoModelForCausalLM, AutoTokenizer
    tok = AutoTokenizer.from_pretrained(model_id)
    tok.padding_side = "left"
    # fp32 weights on CPU and on pre-Ampere CUDA (where matmuls autocast to fp16), bf16 elsewhere
    dtype = torch.float32 if device == "cpu" or amp_dtype(device) else torch.bfloat16
    if split_fp16:  # a model too big for one card: fp16 weights spread over every visible GPU
        model = AutoModelForCausalLM.from_pretrained(model_id, dtype=torch.float16, device_map="auto")
    else:
        model = AutoModelForCausalLM.from_pretrained(model_id, dtype=dtype).to(device)
    if adapter:
        from peft import PeftModel
        model = PeftModel.from_pretrained(model, adapter)
        if not split_fp16:
            model = model.to(device)
    letter_ids = [tok.convert_tokens_to_ids(c) for c in LETTERS]
    assert all(isinstance(i, int) and i >= 0 for i in letter_ids), letter_ids
    return tok, model, letter_ids


def render(tok, row, shuffle_seed):
    options, gold, perm = permute(row, shuffle_seed)
    msgs = [{"role": "user", "content": build_prompt("paper", row["question"], options)}]
    text = tok.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True, enable_thinking=False)
    return text, gold, perm


def letter_logits(model, tok, texts, letter_ids, device):
    enc = tok(texts, return_tensors="pt", padding=True).to(device)
    out = model(**enc, logits_to_keep=1)
    return out.logits[:, -1, :][:, letter_ids].float()


def run_name(args):
    base = f"hf-logit__{args.model.replace('/', '_')}"
    if args.adapter:
        base += "+" + os.path.basename(os.path.normpath(args.adapter))
    name = f"{base}__paper__{args.split}"
    return name + (f"__n{args.limit}" if args.limit else "")


def cmd_eval(args):
    device = pick_device(args.device)
    tok, model, letter_ids = load(args.model, device, args.adapter, args.split_fp16)
    model.eval()
    rows = load_rows(args.split, args.limit, 0)
    items = [(r, *render(tok, r, None)) for r in rows]
    items.sort(key=lambda x: len(x[1]))  # similar lengths per batch: less padding
    path = os.path.join(RUNS_DIR, run_name(args) + ".jsonl")
    t0 = time.time()
    recs = []
    amp = amp_dtype(device)
    with torch.no_grad(), torch.autocast(device.split(":")[0], dtype=amp or torch.bfloat16, enabled=amp is not None):
        for i in range(0, len(items), args.batch):
            chunk = items[i:i + args.batch]
            logits = letter_logits(model, tok, [c[1] for c in chunk], letter_ids, device)
            for (r, _, gold, perm), lg in zip(chunk, logits):
                n = len(perm)
                p = torch.softmax(lg[:n], -1)
                k = int(p.argmax())
                recs.append({
                    "id": r["id"], "provider": "hf-logit", "model": run_name(args).split("__paper__")[0],
                    "prompt_style": "paper", "think": False, "shuffle_seed": None, "split": args.split,
                    "medical_topic": r["medical_topic"], "difficulty_level": r["difficulty_level"],
                    "n_options": n, "perm": perm, "gold": LETTERS[gold], "pred": LETTERS[k],
                    "correct": k == gold, "probs": [round(float(x), 5) for x in p], "error": None,
                })
            if (i // args.batch) % 20 == 0:
                print(f"  {len(recs)}/{len(items)}  {time.time() - t0:.0f}s", flush=True)
    os.makedirs(RUNS_DIR, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        for rec in recs:
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
    acc = sum(r["correct"] for r in recs) / len(recs)
    print(f"{path}\nn={len(recs)} acc={100 * acc:.1f} pickA={100 * sum(r['pred'] == 'A' for r in recs) / len(recs):.1f} "
          f"ECE={100 * ece(recs):.1f} time={time.time() - t0:.0f}s")


def ece(recs, bins=10):
    """Expected calibration error of the top-letter probability, equal-width bins."""
    total, err = len(recs), 0.0
    for b in range(bins):
        sel = [r for r in recs if b / bins < max(r["probs"]) <= (b + 1) / bins]
        if sel:
            conf = sum(max(r["probs"]) for r in sel) / len(sel)
            acc = sum(r["correct"] for r in sel) / len(sel)
            err += len(sel) / total * abs(conf - acc)
    return err


def cmd_train(args):
    from peft import LoraConfig, get_peft_model
    from transformers import get_linear_schedule_with_warmup
    device = pick_device(args.device)
    tok, model, letter_ids = load(args.model, device, split_fp16=args.split_fp16)
    model = get_peft_model(model, LoraConfig(r=args.rank, lora_alpha=2 * args.rank, lora_dropout=0.05,
                                             target_modules=LORA_TARGETS))
    model.print_trainable_parameters()
    # Without CUDA, Qwen3.5's Gated DeltaNet runs its reference PyTorch kernel, which keeps large per-chunk
    # tensors for backward: 8 × 361 tokens needs >14 GiB without checkpointing, 4.9 GiB with it.
    model.gradient_checkpointing_enable(gradient_checkpointing_kwargs={"use_reentrant": False})
    model.enable_input_require_grads()
    rows = load_rows("train", args.limit, 0)
    if args.exclude_topic:  # held-out-topic run: does the gain on topic X need training items from X?
        rows = [r for r in rows if args.exclude_topic not in r["medical_topic"]]
    per_step = args.batch * args.accum
    total = math.ceil(len(rows) * args.epochs / per_step)
    opt = torch.optim.AdamW([p for p in model.parameters() if p.requires_grad], lr=args.lr)
    sched = get_linear_schedule_with_warmup(opt, max(1, total // 30), total)
    targets = torch.tensor(letter_ids, device=device)
    amp = amp_dtype(device)
    scaler = torch.amp.GradScaler("cuda", enabled=amp is not None)
    model.train()
    step, t0, run_loss, run_ok, run_n = 0, time.time(), 0.0, 0, 0
    print(f"train rows={len(rows)} epochs={args.epochs} steps={total} shuffle={args.shuffle} device={device}", flush=True)
    for epoch in range(args.epochs):
        order = rows[:]
        random.Random(f"order{epoch}").shuffle(order)
        # Group by length inside windows of 50 batches (less padding), then shuffle the batch order.
        win, size = args.batch * 50, lambda r: len(r["question"]) + sum(map(len, r["options"]))
        batches = [s[j:j + args.batch] for w in range(0, len(order), win)
                   for s in [sorted(order[w:w + win], key=size)] for j in range(0, len(s), args.batch)]
        random.Random(f"batches{epoch}").shuffle(batches)
        for bi, rows_b in enumerate(batches):
            batch = [render(tok, r, f"train{epoch}" if args.shuffle else None) for r in rows_b]
            enc = tok([b[0] for b in batch], return_tensors="pt", padding=True).to(device)
            with torch.autocast(device.split(":")[0], dtype=amp or torch.bfloat16, enabled=amp is not None):
                full = model(**enc, logits_to_keep=1).logits[:, -1, :].float()
            gold = targets[[b[1] for b in batch]].to(full.device)
            loss = torch.nn.functional.cross_entropy(full, gold)
            scaler.scale(loss / args.accum).backward()
            run_loss += loss.item() * len(batch)
            run_ok += (full[:, letter_ids].argmax(-1).cpu() == torch.tensor([b[1] for b in batch])).sum().item()
            run_n += len(batch)
            if (bi + 1) % args.accum == 0 or bi + 1 == len(batches):
                scaler.unscale_(opt)
                torch.nn.utils.clip_grad_norm_([p for p in model.parameters() if p.requires_grad], 1.0)
                scaler.step(opt)
                scaler.update()
                sched.step()
                opt.zero_grad(set_to_none=True)
                step += 1
                if step % args.log_every == 0 or step == total:
                    el = time.time() - t0
                    print(f"step {step}/{total} ep {epoch} loss {run_loss / run_n:.3f} train-acc {100 * run_ok / run_n:.1f} "
                          f"lr {sched.get_last_lr()[0]:.2e} {el:.0f}s eta {el / step * (total - step):.0f}s", flush=True)
                    run_loss, run_ok, run_n = 0.0, 0, 0
        model.save_pretrained(args.out)
        print(f"saved {args.out} after epoch {epoch}", flush=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", choices=["eval", "train"])
    ap.add_argument("--model", required=True)
    ap.add_argument("--adapter", help="eval: LoRA adapter dir to apply")
    ap.add_argument("--out", help="train: adapter output dir")
    ap.add_argument("--split", default="test", choices=["train", "val", "test"])
    ap.add_argument("--limit", type=int, help="seeded subsample of the split")
    ap.add_argument("--device", default="auto")
    ap.add_argument("--batch", type=int, default=8)
    ap.add_argument("--accum", type=int, default=2)
    ap.add_argument("--epochs", type=int, default=1)
    ap.add_argument("--lr", type=float, default=2e-4)
    ap.add_argument("--rank", type=int, default=16)
    ap.add_argument("--split-fp16", action="store_true",
                    help="load fp16 weights across all visible GPUs (a 9B model on two 16 GB T4s)")
    ap.add_argument("--shuffle", action="store_true", help="train: permute options per example and epoch")
    ap.add_argument("--exclude-topic", help="train: drop every train row carrying this medical_topic label")
    ap.add_argument("--log-every", type=int, default=10)
    args = ap.parse_args()
    if args.cmd == "train" and not args.out:
        ap.error("train needs --out")
    cmd_eval(args) if args.cmd == "eval" else cmd_train(args)


if __name__ == "__main__":
    main()
