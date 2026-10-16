#!/usr/bin/env python3
"""
kaggle_lora9b.py — LoRA fine-tune Qwen3.5-9B on the VM14K train split, on Kaggle (2 x T4).

Same recipe as the 2B run (sft_mcq_lora.py: LoRA r=16, one epoch, shuffled options, letter-logit
scoring), with the fp16 weights spread over both GPUs (--split-fp16). Compare the result with the
zero-shot backbone scored the same way, reports/eval/runs/hf-logit__Qwen_Qwen3.5-9B__paper__test.jsonl
(64.5%). Writes the run file, the log and the adapter to /kaggle/working.

    kaggle kernels push -p <folder with this file + kernel-metadata.json> --accelerator NvidiaTeslaT4
"""
import glob
import os
import shutil
import subprocess

REPO = "https://github.com/hanguyennn2812/VM14K_Research.git"
COMMIT = "f7b83fb"
MODEL = "Qwen/Qwen3.5-9B"
NAME = "q35-9b-sft-shuf"
OUT = "/kaggle/working"


def sh(cmd):
    print("$", cmd, flush=True)
    subprocess.run(cmd, shell=True, check=True, executable="/bin/bash")


sh("nvidia-smi --query-gpu=name,memory.total --format=csv")
sh("pip install -q 'transformers==5.19.0' 'peft==0.21.2' accelerate")
sh("pip uninstall -y -q torchao")  # Kaggle's torchao 0.10 makes peft 0.21 refuse to import
sh(f"git clone -q {REPO} /tmp/repo && git -C /tmp/repo checkout -q {COMMIT}")
sh(f"python -c \"from huggingface_hub import snapshot_download; snapshot_download('{MODEL}', "
   f"allow_patterns=['*.json', '*.safetensors', '*.txt', '*.jinja'])\"")
run = "cd /tmp/repo && PYTHONUNBUFFERED=1 python scripts/training/sft_mcq_lora.py"
sh(f"set -o pipefail; {run} train --model {MODEL} --shuffle --split-fp16 --out {OUT}/{NAME} --log-every 25 "
   f"2>&1 | tee {OUT}/train.log")
sh(f"set -o pipefail; {run} eval --model {MODEL} --split-fp16 --adapter {OUT}/{NAME} --batch 16 2>&1 | tee {OUT}/eval.log")
for f in glob.glob("/tmp/repo/reports/eval/runs/hf-logit__*9B+*.jsonl"):
    shutil.copy(f, OUT)
    print("saved", os.path.basename(f), flush=True)
