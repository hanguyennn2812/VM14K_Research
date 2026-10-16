#!/usr/bin/env python3
"""
kaggle_heldout.py — Kaggle job for the held-out-topic experiment.

Does fine-tuning teach topic knowledge, or only general habits? Two LoRA runs
of sft_mcq_lora.py, identical except that the second drops every train row
labelled Obstetrics and Gynecology (1,475 of 7,313). Both are scored on the
full test split; the comparison that matters is on the 319 OB/GYN test items.
The first run also replicates the laptop result on different hardware.

On a 2-GPU machine (Kaggle "GPU T4 x2") the runs go in parallel, one per GPU.
Only the run files and logs are written to /kaggle/working.

    kaggle kernels push -p <folder with this file + kernel-metadata.json> --accelerator NvidiaTeslaT4
"""
import glob
import os
import shutil
import subprocess
import sys

REPO = "https://github.com/hanguyennn2812/VM14K_Research.git"
COMMIT = "5208a66"
MODEL = "Qwen/Qwen3.5-2B"
JOBS = {
    "kg-sft-shuf": "",
    "kg-sft-shuf-noOBGYN": "--exclude-topic 'Obstetrics and Gynecology'",
}
OUT = "/kaggle/working"


def sh(cmd):
    print("$", cmd, flush=True)
    subprocess.run(cmd, shell=True, check=True)


sh("nvidia-smi --query-gpu=name,memory.total --format=csv")
sh("pip install -q 'transformers==5.19.0' 'peft==0.21.2' accelerate")
sh("pip uninstall -y -q torchao")  # Kaggle ships torchao 0.10, which peft 0.21 refuses to import alongside
sh(f"git clone -q {REPO} /tmp/repo && git -C /tmp/repo checkout -q {COMMIT}")
sh(f"python -c \"from huggingface_hub import snapshot_download; snapshot_download('{MODEL}')\"")

import torch  # noqa: E402  (after the pip install above)

ngpu = max(1, torch.cuda.device_count())
procs = []
for k, (name, extra) in enumerate(JOBS.items()):
    cmd = (f"cd /tmp/repo && python scripts/training/sft_mcq_lora.py train --model {MODEL} --shuffle {extra} "
           f"--out /tmp/ft/{name} --log-every 25 && python scripts/training/sft_mcq_lora.py eval --model {MODEL} "
           f"--adapter /tmp/ft/{name} --batch 32")
    # tee to a per-run log and to the kernel log (prefixed), so progress shows while the job runs
    cmd = f"set -o pipefail; ({cmd}) 2>&1 | tee {OUT}/{name}.log | sed -u 's/^/[{name}] /'"
    p = subprocess.Popen(cmd, shell=True, executable="/bin/bash",
                         env=dict(os.environ, CUDA_VISIBLE_DEVICES=str(k % ngpu), PYTHONUNBUFFERED="1"))
    procs.append((name, p))
    print(f"started {name} on GPU {k % ngpu}", flush=True)
    if ngpu < 2:
        p.wait()

failed = False
for name, p in procs:
    p.wait()
    print(f"{name}: exit {p.returncode}", flush=True)
    failed |= p.returncode != 0
    with open(os.path.join(OUT, f"{name}.log")) as fh:
        print("".join(fh.readlines()[-6:]), flush=True)

for f in glob.glob("/tmp/repo/reports/eval/runs/hf-logit__*kg-*.jsonl"):
    shutil.copy(f, OUT)
    print("saved", os.path.basename(f), flush=True)
sys.exit(1 if failed else 0)
