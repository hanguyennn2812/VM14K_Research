#!/usr/bin/env python3
"""Did MoH training add knowledge? Paired comparison of two jev-torch runs on VM14K val.

Written before either full run finished. Primary: gain on Infectious Diseases minus gain elsewhere
(format gains spread evenly, knowledge gains stay where it was trained). Secondary: the same contrast
for questions naming a disease in the MoH train documents, and MoH val, whose diseases were never trained.

    python scripts/eval/analyze_moh_train.py --base RUN.jsonl --new RUN.jsonl
"""
import argparse
import json
import random
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts" / "training"))
from moh_mcq_source import fold  # noqa: E402

# Diseases of the MoH train documents in the frozen split (document_split_v1_20261105.json).
TRAINED = re.compile(r"\b(?:lao(?! dong)|covid|dengue|sot xuat huyet|tay chan mieng|herpes|hsv)\b")


def read(path):
    with open(path, encoding="utf-8") as fh:
        return {r["id"]: r for r in map(json.loads, fh) if not r.get("error")}


def gain(ids, base, new):
    return (sum(new[i]["correct"] for i in ids) - sum(base[i]["correct"] for i in ids)) / len(ids) * 100


def contrast(inside, outside, base, new, reps=2000, seed=20261105):
    """Gain(inside) - gain(outside), with a paired bootstrap 95% CI over questions."""
    rng = random.Random(seed)
    point = gain(inside, base, new) - gain(outside, base, new)
    draws = sorted(gain(rng.choices(inside, k=len(inside)), base, new) -
                   gain(rng.choices(outside, k=len(outside)), base, new) for _ in range(reps))
    return point, draws[int(reps * .025)], draws[int(reps * .975)]


def line(name, ids, base, new):
    a = sum(base[i]["correct"] for i in ids) / len(ids) * 100
    b = sum(new[i]["correct"] for i in ids) / len(ids) * 100
    wins = sum(new[i]["correct"] and not base[i]["correct"] for i in ids)
    losses = sum(base[i]["correct"] and not new[i]["correct"] for i in ids)
    print(f"{name:34} n={len(ids):5} base={a:5.1f} new={b:5.1f} gain={b - a:+5.1f}  wins={wins} losses={losses}")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--base", required=True)
    ap.add_argument("--new", required=True)
    ap.add_argument("--data", default=str(ROOT / "data/derived/jevtorch/val.jsonl"))
    ap.add_argument("--split", default="val", help="VM14K split to report")
    args = ap.parse_args()
    base, new = read(args.base), read(args.new)
    with open(args.data, encoding="utf-8") as fh:
        text = {r["id"]: fold(r["state"] + " " + " ".join(r["options"].values())) for r in map(json.loads, fh)}
    shared = sorted(set(base) & set(new))
    val = [i for i in shared if base[i]["split"] == args.split]
    moh = [i for i in shared if base[i]["split"].startswith("moh-")]
    infectious = [i for i in val if "Infectious Diseases" in base[i]["medical_topic"]]
    other = [i for i in val if "Infectious Diseases" not in base[i]["medical_topic"]]
    trained = [i for i in val if TRAINED.search(text[i])]
    untrained = [i for i in val if not TRAINED.search(text[i])]
    print(f"errors or missing: base {len(base)} new {len(new)} shared {len(shared)}")
    line("VM14K, all", val, base, new)
    line("VM14K, Infectious Diseases", infectious, base, new)
    line("VM14K, other topics", other, base, new)
    line("VM14K, names a trained disease", trained, base, new)
    line("VM14K, no trained disease", untrained, base, new)
    if moh:
        line("MoH held-out (never trained)", moh, base, new)
    print("PRIMARY   infectious - other:  %+.1f [%+.1f, %+.1f]" % contrast(infectious, other, base, new))
    print("SECONDARY trained - untrained: %+.1f [%+.1f, %+.1f]" % contrast(trained, untrained, base, new))


if __name__ == "__main__":
    # A gain confined to the inside group must give a positive contrast; identical runs give zero.
    a = {i: {"correct": False} for i in "abcd"}
    b = {**a, "a": {"correct": True}}
    assert contrast(["a", "b"], ["c", "d"], a, a)[0] == 0
    assert contrast(["a", "b"], ["c", "d"], a, b)[0] == 50
    assert TRAINED.search("benh lao phoi") and not TRAINED.search("nguoi lao dong")
    main()
