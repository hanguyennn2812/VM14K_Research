# VM14K decision training with jev-torch

Prepared 2026-10-23; **no Modal job launched**. From the repository root:

```powershell
python scripts/training/jevtorch_data.py --self-check
python scripts/training/jevtorch_data.py --out data/derived/jevtorch --seed 42
modal run scripts/training/modal_jevtorch.py --data data/derived/jevtorch --seed 42
```

The last command requires an authenticated Modal CLI and starts paid compute.
The converter uses `load_rows(split, None, 0)`, seeded per-ID train permutations,
and remapped one-hot targets. Val/test retain order and IDs. The job translates
the requested A–D keyed options to upstream's native list and maps the instruction
to `question`; the keyed export alone is not a native upstream input.

Training uses Qwen/Qwen3.5-2B, one H100, BF16, rank-16 LoRA, 2,048-token context,
microbatch 4/global batch 32, and CE (equivalent to KL for one-hot targets).
Upstream may drop trailing microbatches to complete accumulation groups.
Frozen val is split 50/50 by SHA-256 of ID: development selects between step zero
and epoch end; calibration fits temperature. Test is scored afterward. Hub/W&B
uploads are disabled. CPU fetch caches the immutable model snapshot on
`vm14k-hf-cache` at `/cache` (`HF_HOME=/cache`). Config, checkpoint, calibration
report, package versions, and predictions persist in `/jevtorch-vm14k/<run-id>/`.
The protected local output is
`reports/eval/runs/jevtorch__Qwen_Qwen3.5-2B__choice__test.jsonl`.

**Cost assumption:** about 7,313 training items, typically 500–1,000 tokens, working FLA
kernels, and 15–45 GPU minutes including compilation, validation, and test scoring.
At Modal's listed **$0.001097/s ($3.95/hour)**, that is **$0.99–$2.96 GPU cost**;
budget **$1–$4 total** with CPU/memory overhead. Each remote function has a hard
7,200-second timeout and no automatic retries; two GPU hours alone cost $7.90.
This is an estimate, not a billing cap. [Modal pricing](https://modal.com/pricing).

**Verified by source inspection:** README/data format, JSONL loading, config names,
CE loss, automatic calibration/checkpoint layout, and `JEVPredictor.logits`, all at
commit `96b1f101d90d6b878804000d67645b8ee0631227` (Apache-2.0 code).
[README](https://github.com/smha1012/jev-torch/blob/96b1f101d90d6b878804000d67645b8ee0631227/README.md),
[schema](https://github.com/smha1012/jev-torch/blob/96b1f101d90d6b878804000d67645b8ee0631227/jev/schema.py),
[trainer](https://github.com/smha1012/jev-torch/blob/96b1f101d90d6b878804000d67645b8ee0631227/jev/trainer.py).
**Unverified:** image/dependency resolution, H100 TileLang/FLA execution, memory/time,
and training quality; these are commented in the job. The fake-row self-check passed
with `.venv\Scripts\python.exe` (the system `python` alias was inaccessible).
Full export/training/scoring remain unrun.
