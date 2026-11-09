#!/usr/bin/env python3
"""Fact-pair probe: did training raise recall of trained facts more than of untrained control facts?

Written before any pair result was seen. Primary: gain on new facts (in trained chunks, not asked by a trained
question) minus gain on control facts (val documents, never trained). Secondary: the same for seen facts, and
VM14K val as a forgetting check. Runs are read from their records' own `split` field.

    python scripts/eval/analyze_pairs.py --base RUN.jsonl --new RUN.jsonl
"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from analyze_moh_train import contrast, line, read  # noqa: E402


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--base", required=True)
    ap.add_argument("--new", required=True)
    args = ap.parse_args()
    base, new = read(args.base), read(args.new)
    shared = sorted(set(base) & set(new))
    group = {name: [i for i in shared if base[i]["split"] == name] for name in ("new", "seen", "control", "val")}
    print(f"shared {len(shared)} of base {len(base)}, new {len(new)}")
    for name, label in (("new", "Pairs: new facts, trained chunks"), ("seen", "Pairs: seen facts, trained chunks"),
                        ("control", "Pairs: control, untrained documents"), ("val", "VM14K val")):
        if group[name]:
            line(label, group[name], base, new)
    print("PRIMARY   new - control:  %+.1f [%+.1f, %+.1f]" % contrast(group["new"], group["control"], base, new))
    print("SECONDARY seen - control: %+.1f [%+.1f, %+.1f]" % contrast(group["seen"], group["control"], base, new))


if __name__ == "__main__":
    main()
