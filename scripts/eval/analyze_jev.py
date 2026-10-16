#!/usr/bin/env python3
"""
analyze_jev.py — the weekend Jev experiments (E1–E5) on the VM14K test split.

  E1  Qwen3.5-2B + LoRA (shuffled-option training), logit-scored     baseline
  E2  Jev alone, one Choice question per item                      run_jev.py
  E3  E1 and E2 fused: average of their option probabilities        no new calls
  E4  Jev answers when confident, the rest goes to DeepSeek         no new calls
  E5  Jev with options presented in a shuffled order               run_jev.py --shuffle-seed 1

Writes reports/eval/JEV.md. Runs that are missing are reported as missing.

    python scripts/eval/analyze_jev.py                                          # hosted Jev
    python scripts/eval/analyze_jev.py --s1 jev9b__autotrust_JEV-9B__choice__test  # open stand-in (kaggle_jev9b.py)
"""
import argparse
import os
import sys

HERE = os.path.dirname(__file__)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "training"))
from analyze_finetune import acc_at_coverage, conf, ece, paired_row, pct, table  # noqa: E402
from run_eval import LETTERS, RUNS_DIR, load_rows  # noqa: E402
from summarize_eval import load_run  # noqa: E402

OUT_MD = os.path.join(RUNS_DIR, "..", "JEV.md")
RUNS = {
    "E1": "hf-logit__Qwen_Qwen3.5-2B+q35-2b-sft-shuf__paper__test",
    "E2": "typesafe__jev-latest__choice__test",
    "E5": "typesafe__jev-latest__choice__test__shuf1",
    "DeepSeek": "nvidia__deepseek-ai_deepseek-v4.1-flash__paper__test",
    "9B": "hf-logit__Qwen_Qwen3.5-9B__paper__test",  # JEV-9B's backbone alone, when present
}
HDR = ["comparison (A → B)", "n", "A %", "B %", "B − A", "only A right", "only B right", "p"]


def load(name):
    path = os.path.join(RUNS_DIR, name + ".jsonl")
    return {r["id"]: r for r in load_run(path)} if os.path.exists(path) else None


def fuse(a, b, ids):
    """Average of two runs' option probabilities, both in the original option order."""
    out = {}
    for i in ids:
        pa, pb = a[i]["probs"], b[i].get("probs_orig") or b[i]["probs"]
        p = [(x + y) / 2 for x, y in zip(pa, pb)]
        k = p.index(max(p))
        out[i] = dict(a[i], pred=LETTERS[k], correct=LETTERS[k] == a[i]["gold"], probs=p)
    return out


def routing_rows(run, big, ids):
    order = sorted(ids, key=lambda i: conf(run[i]))  # least confident first
    acc_small = sum(run[i]["correct"] for i in ids) / len(ids)
    acc_big = sum(big[i]["correct"] for i in ids) / len(ids)
    rows = []
    for share in (0.0, 0.25, 0.5, 0.75):
        routed = set(order[:round(share * len(ids))])
        acc = sum(big[i]["correct"] if i in routed else run[i]["correct"] for i in ids) / len(ids)
        rows.append([f"{100 * share:.0f}%", f"{100 * acc:.1f}",
                     f"{100 * ((1 - share) * acc_small + share * acc_big):.1f}"])
    return rows


STRONG = [  # (label, run, how it was scored); every run covers the full test split
    ("Gemma-4-31B", "nvidia__google_gemma-4-31b-it__paper__test", "generation"),
    ("DeepSeek-v4.1-flash", "nvidia__deepseek-ai_deepseek-v4.1-flash__paper__test", "generation"),
    ("Nemotron-3-Ultra 550B-A55B", "nvidia__nvidia_nemotron-3-ultra-550b-a55b__paper__test", "generation"),
    ("Qwen3.5-9B + LoRA", "hf-logit__Qwen_Qwen3.5-9B+q35-9b-sft-shuf__paper__test", "letter probabilities"),
    ("Qwen3.5-9B", "qwen3.5_9b__paper__test", "generation"),
    ("Llama-3.2-90B", "nvidia__meta_llama-3.2-90b-vision-instruct__paper__test", "generation"),
    ("Nemotron-3-Super 120B-A12B", "nvidia__nvidia_nemotron-3-super-120b-a12b__paper__test", "generation"),
    ("Nemotron-3.5-Lightning 30B-A3B", "nvidia__nvidia_nemotron-3.5-lightning-30b-a3b__paper__test", "generation"),
]


def strong_models_section(s1, s1_name):
    """The System One run against the strong models, on the items both answered."""
    ids = list(s1)
    top = set(sorted(ids, key=lambda i: conf(s1[i]), reverse=True)[:len(ids) // 2])
    rows = [[f"{s1_name} (System One head)", len(ids), pct(sum(s1[i]["correct"] for i in ids), len(ids)), "–", "–", "–",
             f"{100 * sum(s1[i]['correct'] for i in top) / len(top):.1f}"]]
    for label, name, how in STRONG:
        run = load(name)
        if run is None:
            continue
        both = [i for i in ids if i in run]
        x = sum(s1[i]["correct"] and not run[i]["correct"] for i in both)
        y = sum(run[i]["correct"] and not s1[i]["correct"] for i in both)
        from compare_runs import mcnemar_exact
        agree = sum(run[i]["pred"] == s1[i]["pred"] for i in both) / len(both)
        t = [i for i in both if i in top]
        rows.append([f"{label} ({how})", len(both), pct(sum(run[i]["correct"] for i in both), len(both)),
                     f"{100 * (sum(run[i]['correct'] for i in both) - sum(s1[i]['correct'] for i in both)) / len(both):+.1f}",
                     f"{mcnemar_exact(x, y):.2g}", f"{100 * agree:.1f}",
                     f"{100 * sum(run[i]['correct'] for i in t) / len(t):.1f}"])
    rows[1:] = sorted(rows[1:], key=lambda r: -float(r[2].split()[0]))
    out = [f"## {s1_name} against the strong models", "",
           "Same 1,658 test questions. Generation-scored runs answer with a letter that is parsed "
           "(`run_eval.py`, thinking off); the others read option probabilities, so treat small gaps across "
           f"scoring methods with care. Last column: accuracy on the half of the questions {s1_name} is most sure "
           "of.", ""]
    out += table(["model", "n", "accuracy [95% CI]", f"vs {s1_name}", "p (McNemar)", f"same answer as {s1_name} %",
                  f"on {s1_name}'s surest 50%"], rows)
    out += ["The VM14K paper's numbers (GPT-4o 72.7, Claude 3.5 Sonnet 71.5, Gemini 2.0 Flash 75.7, DeepSeek-R1 "
            "78.2, Qwen3-32B 72.5) are on the uncleaned 12,488-row release and are not on these questions.", ""]
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--s1", default=RUNS["E2"], help="System One run used as E2; E5 is the same name + __shuf1")
    args = ap.parse_args()
    RUNS["E2"], RUNS["E5"] = args.s1, args.s1 + "__shuf1"
    runs = {k: load(v) for k, v in RUNS.items()}
    if runs["9B"] is None:
        del runs["9B"]
    missing = [f"{k} ({RUNS[k]})" for k, v in runs.items() if v is None]
    s1_name = RUNS["E2"].split("__")[1]
    ids = [r["id"] for r in load_rows("test", None, 0)]
    lines = [f"# VM14K: System One experiments (E1–E5), E2 = {s1_name}", "",
             "Generated by `scripts/eval/analyze_jev.py`. Test split, 1,658 questions. Jev runs come from "
             "`scripts/eval/run_jev.py` (one Choice question per item: state = question, criteria = option "
             "letters → option texts). E1 is the LoRA model from `FINETUNE.md`.", ""]
    if missing:
        lines += ["Missing runs: " + "; ".join(missing) + ".", ""]
    e1, e2, e5, ds = runs["E1"], runs["E2"], runs["E5"], runs["DeepSeek"]
    if e1 and e2:
        ids = [i for i in ids if i in e1 and i in e2]
        e3 = fuse(e1, e2, ids)
        rows = []
        rows_spec = [("E1 Qwen3.5-2B + LoRA", e1), (f"E2 {s1_name}", e2), ("E3 fused E1 + E2", e3)]
        if runs.get("9B"):
            rows_spec.append(("Qwen3.5-9B letter probabilities (JEV-9B backbone, no head)", runs["9B"]))
        for label, run in rows_spec:
            recs = [run[i] for i in ids]
            k = sum(r["correct"] for r in recs)
            rows.append([label, len(recs), pct(k, len(recs)),
                         f"{100 * sum(r['pred'] == 'A' for r in recs) / len(recs):.1f}",
                         f"{100 * ece(recs):.1f}", f"{100 * acc_at_coverage(recs, 0.5):.1f}"])
        lines += ["## E1–E3: accuracy and calibration", ""]
        lines += table(["run", "n", "accuracy [95% CI]", "picks A %", "ECE %", "acc. on 50% most confident"], rows)
        pairs = [paired_row("E1 → E2", e1, e2, ids), paired_row("E1 → E3", e1, e3, ids),
                 paired_row("E2 → E3", e2, e3, ids)]
        if runs.get("9B"):
            pairs.append(paired_row("Qwen3.5-9B letter probabilities → E2", runs["9B"], e2, ids))
        lines += table(HDR, pairs)
        if ds:
            r_ids = [i for i in ids if i in ds]
            lines += ["## E4: answer when confident, otherwise ask DeepSeek-v4.1-flash", "",
                      "The least confident share goes to DeepSeek (its zero-shot answers). `random` sends the "
                      "same share at random (expected accuracy).", ""]
            jr, qr = routing_rows(e2, ds, r_ids), routing_rows(e1, ds, r_ids)
            lines += table(["sent to DeepSeek", f"{s1_name} confidence", f"random ({s1_name})", "Qwen-2B confidence",
                            "random (Qwen-2B)"], [[a[0], a[1], a[2], b[1], b[2]] for a, b in zip(jr, qr)])
            rows = []
            for share in (0.25, 0.5):
                top = sorted(r_ids, key=lambda i: conf(e2[i]), reverse=True)[:round(share * len(r_ids))]
                rows.append([f"{100 * share:.0f}% most confident", len(top),
                             f"{100 * sum(e2[i]['correct'] for i in top) / len(top):.1f}",
                             f"{100 * sum(ds[i]['correct'] for i in top) / len(top):.1f}"])
            lines += [f"On the items {s1_name} is most sure of, how does it compare with DeepSeek on the same items?", ""]
            lines += table(["items", "n", f"{s1_name} %", "DeepSeek %"], rows)
    if e2 and e5:
        s_ids = [i for i in ids if i in e2 and i in e5]
        same = sum(e5[i]["perm"][LETTERS.index(e5[i]["pred"])] == LETTERS.index(e2[i]["pred"]) for i in s_ids)
        lines += ["## E5: does the option order change Jev's answer?", "",
                  f"Shuffled options: accuracy {pct(sum(e5[i]['correct'] for i in s_ids), len(s_ids))} against "
                  f"{pct(sum(e2[i]['correct'] for i in s_ids), len(s_ids))} in the original order. Jev picks the "
                  f"same option (by content) in {100 * same / len(s_ids):.1f}% of items. Presented letter A: "
                  f"picked {100 * sum(e5[i]['pred'] == 'A' for i in s_ids) / len(s_ids):.1f}%, key "
                  f"{100 * sum(e5[i]['gold'] == 'A' for i in s_ids) / len(s_ids):.1f}%.", ""]
        lines += table(HDR, [paired_row("E2 original order → E5 shuffled", e2, e5, s_ids)])
    if e2:
        lines += strong_models_section(e2, s1_name)
    with open(OUT_MD, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))
    print("\n".join(lines))


if __name__ == "__main__":
    main()
