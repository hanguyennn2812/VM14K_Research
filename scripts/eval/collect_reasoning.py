#!/usr/bin/env python3
"""
collect_reasoning.py — re-ask chosen questions and keep the model's explanation.

The scored runs (run_eval.py) ask for a single letter with thinking off, so
they record no reasoning. This script re-asks a list of ids with a prompt that
asks the model to explain in Vietnamese and end with "Đáp án: X", optionally
with thinking on, and keeps the full text: the explanation (message content)
and the thinking trace (reasoning_content) when the provider returns one.

It is for manual review, not scoring: the prompt differs from the paper's, so
the letter can differ from the model's scored answer. Ids are read straight
from the cleaned dataset, so questions excluded from scoring (e.g.
contradiction_pending_review) can still be asked.

Each row has a status: "answered" (a valid letter on the final "Đáp án" line)
or "abstained" (the final line names no option, e.g. "không có phương án
đúng"). An empty or length-truncated reply is logged as an error, so a rerun
asks it again — raise --max-tokens if replies are being cut.

Output: one JSONL row per question in reports/eval/reasoning/<run>.jsonl.
Reruns resume, like run_eval.py. --reparse re-applies the answer parser to an
existing log without calling the API.

    python scripts/eval/collect_reasoning.py --provider nvidia --model deepseek-ai/deepseek-v4.1-flash \\
        --ids reports/eval/review/review_ids.txt --think on --rpm 30 --workers 4
"""
import argparse
import concurrent.futures
import json
import os
import re
import sys
import threading
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from run_eval import (  # noqa: E402
    DATA_PATH, FATAL_HTTP, LETTERS, NO_THINK_BODY, PROVIDERS, REPO_ROOT, Pacer, done_records,
    ollama_capabilities, post_with_retries, repair_partial_tail,
)

OUT_DIR = os.path.join(REPO_ROOT, "reports", "eval", "reasoning")

PROMPT = (
    "{question}\n"
    "Chọn đáp án đúng trong các phương án sau:\n"
    "{options}\n\n"
    "Hãy giải thích lập luận của bạn bằng tiếng Việt: xét từng phương án và nêu kiến thức y khoa, "
    "hướng dẫn hoặc phác đồ mà bạn dựa vào. Nếu câu hỏi mơ hồ, thiếu dữ kiện hoặc không có phương án "
    "nào đúng, hãy nói rõ.\n"
    "Dòng cuối cùng ghi đúng theo mẫu: Đáp án: X"
)

# Request fields that switch thinking on, the mirror of run_eval.NO_THINK_BODY.
THINK_BODY = {
    "nvidia": {"chat_template_kwargs": {"thinking": True, "enable_thinking": True}},
}

# A line that opens with the answer marker ("Đáp án:", "**Đáp án đúng là**", "> Đáp án -").
_MARKER_LINE_RE = re.compile(r"^[\s>*#_\-]*đáp\s*án(?:\s*đúng)?(?:\s*là)?\s*[*_]*\s*[:\-]?\s*(.*)$", re.I)
_LEADING_LETTER_RE = re.compile(r"^[*_(\[\s]*([A-G])(?!\w)")
_BARE_LETTER_RE = re.compile(r"[*_(\[\s]*([A-G])[*_.)\]\s]*")


def final_letter(text, n_options):
    """Letter on the LAST line that starts with 'Đáp án', or None when that line names no valid
    option (an abstention such as 'Đáp án: Không có phương án đúng'). Without such a line, only a
    last line that is a bare letter counts — explanations name other options all the way through."""
    valid = LETTERS[:n_options]
    lines = [line.strip() for line in (text or "").splitlines() if line.strip()]
    for line in reversed(lines):
        m = _MARKER_LINE_RE.match(line)
        if m:
            lm = _LEADING_LETTER_RE.match(m.group(1))
            return lm.group(1) if lm and lm.group(1) in valid else None
    if lines:
        m = _BARE_LETTER_RE.fullmatch(lines[-1])
        if m and m.group(1) in valid:
            return m.group(1)
    return None


def outcome(out, n_options, gold):
    """Fields derived from a reply: pred / correct / status, or an error for unusable replies."""
    if not (out.get("answer_text") or "").strip():
        return {"pred": None, "correct": False, "status": None, "error": "empty response"}
    if out.get("done_reason") == "length":
        return {"pred": None, "correct": False, "status": None, "error": "truncated (length)"}
    pred = final_letter(out["answer_text"], n_options)
    return {"pred": pred, "correct": pred == gold, "status": "answered" if pred else "abstained", "error": None}


def ask_ollama(cfg, prompt):
    """Native Ollama chat API: it returns the thinking trace as message.thinking."""
    body = {
        "model": cfg["model"],
        "messages": [{"role": "user", "content": prompt}],
        "stream": False,
        "keep_alive": "30m",
        "options": {"seed": 0, "temperature": 0, "num_predict": cfg["max_tokens"], "num_ctx": 8192},
    }
    if cfg["think"] is not None:
        body["think"] = cfg["think"]
    t0 = time.time()
    resp, err = post_with_retries(cfg["base_url"].rstrip("/") + "/api/chat", body, cfg["timeout"], None,
                                  cfg["pacer"], cfg["retries"])
    if resp is None:
        return None, err
    msg = resp.get("message") or {}
    return {
        "answer_text": msg.get("content") or "",
        "reasoning": msg.get("thinking") or "",
        "done_reason": resp.get("done_reason"),
        "prompt_tokens": resp.get("prompt_eval_count"),
        "output_tokens": resp.get("eval_count"),
        "max_tokens": cfg["max_tokens"],
        "latency_s": round(time.time() - t0, 2),
    }, None


def ask(cfg, prompt):
    if cfg["provider"] == "ollama":
        return ask_ollama(cfg, prompt)
    body = {
        "model": cfg["model"],
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": cfg["max_tokens"],
        "temperature": 0,
        **cfg["extra_body"],
    }
    headers = {"Authorization": f"Bearer {cfg['api_key']}"}
    t0 = time.time()
    resp, err = post_with_retries(cfg["base_url"] + "/chat/completions", body, cfg["timeout"], headers,
                                  cfg["pacer"], cfg["retries"])
    if resp is None:
        return None, err
    choice = (resp.get("choices") or [{}])[0]
    msg = choice.get("message") or {}
    usage = resp.get("usage") or {}
    reasoning = msg.get("reasoning_content") or msg.get("reasoning") or ""
    return {
        "answer_text": msg.get("content") or "",
        "reasoning": reasoning if isinstance(reasoning, str) else json.dumps(reasoning, ensure_ascii=False),
        "done_reason": choice.get("finish_reason"),
        "prompt_tokens": usage.get("prompt_tokens"),
        "output_tokens": usage.get("completion_tokens"),
        "max_tokens": cfg["max_tokens"],
        "latency_s": round(time.time() - t0, 2),
    }, None


def reparse(path):
    """Re-apply final_letter() to every error-free row of an existing log, in place."""
    with open(path, encoding="utf-8") as fh:
        recs = [json.loads(line) for line in fh if line.strip()]
    changed = 0
    for rec in recs:
        if rec.get("error") is not None:
            continue
        new = outcome(rec, rec["n_options"], rec["gold"])
        if (new["pred"], new["status"], new["error"]) != (rec.get("pred"), rec.get("status"), rec.get("error")):
            changed += 1
        rec.update(new)
    with open(path, "w", encoding="utf-8") as fh:
        for rec in recs:
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print(f"reparsed {os.path.relpath(path, REPO_ROOT)}: {changed} of {len(recs)} rows changed")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--model", required=True)
    ap.add_argument("--provider", default="nvidia", choices=["ollama"] + sorted(PROVIDERS))
    ap.add_argument("--host", default=os.environ.get("OLLAMA_HOST_URL", "http://localhost:11434"),
                    help="Ollama server (with --provider ollama)")
    ap.add_argument("--ids", required=True, help="text file, one question id per line")
    ap.add_argument("--think", default="on", choices=["on", "off"])
    ap.add_argument("--limit", type=int, default=0, help="only the first N ids (for a smoke test)")
    ap.add_argument("--max-tokens", type=int, default=0, help="default 8192 with thinking, 2048 without")
    ap.add_argument("--rpm", type=float, default=30)
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--timeout", type=float, default=300)
    ap.add_argument("--retries", type=int, default=4)
    ap.add_argument("--tag", help="run-name part (default: the ids file name); reuse a tag to add ids to "
                                  "an existing log")
    ap.add_argument("--reparse", action="store_true", help="re-parse the existing log, no API calls")
    args = ap.parse_args()

    thinking = args.think == "on"
    safe = re.sub(r"[^A-Za-z0-9._-]+", "_", args.model)
    tag = args.tag or os.path.splitext(os.path.basename(args.ids))[0]
    name = "__".join([args.provider, safe, "explain", tag] + (["think-on"] if thinking else []))
    out_path = os.path.join(OUT_DIR, f"{name}.jsonl")
    if args.reparse:
        reparse(out_path)
        return

    if args.provider == "ollama":
        base_url, api_key = args.host, None
        caps = ollama_capabilities(base_url, args.model)
        if not caps:
            sys.exit(f"Ollama at {base_url} does not answer for {args.model} — is the server running?")
        # Only send the think switch to models that support it; others just write the explanation.
        think_value = (args.think == "on") if "thinking" in caps else None
    else:
        base_url, key_var = PROVIDERS[args.provider]
        api_key = os.environ.get(key_var)
        if not api_key:
            sys.exit(f"{key_var} is not set")
        think_value = None
    with open(args.ids, encoding="utf-8") as fh:
        wanted = [line.strip() for line in fh if line.strip()]
    if args.limit:
        wanted = wanted[:args.limit]
    wanted_set = set(wanted)
    by_id = {}
    with open(DATA_PATH, encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                r = json.loads(line)
                if r["id"] in wanted_set:
                    by_id[r["id"]] = r
    missing = [i for i in wanted if i not in by_id]
    if missing:
        print(f"warning: {len(missing)} ids not in {os.path.relpath(DATA_PATH, REPO_ROOT)}, skipped: "
              + ", ".join(missing[:5]) + (" …" if len(missing) > 5 else ""), flush=True)
    rows = [by_id[i] for i in wanted if i in by_id]

    cfg = {
        "provider": args.provider, "think": think_value,
        "model": args.model, "base_url": base_url, "api_key": api_key,
        "max_tokens": args.max_tokens or (8192 if thinking else 2048),
        "extra_body": (THINK_BODY if thinking else NO_THINK_BODY).get(args.provider, {}),
        "timeout": args.timeout, "retries": args.retries, "pacer": Pacer(args.rpm),
    }
    os.makedirs(OUT_DIR, exist_ok=True)
    repair_partial_tail(out_path)
    done = done_records(out_path)
    todo = [r for r in rows if r["id"] not in done]
    print(f"{name}: {len(rows)} ids, {len(done)} done, {len(todo)} to ask", flush=True)

    lock = threading.Lock()
    stop = threading.Event()
    counts = {"ok": 0, "err": 0}

    def work(r):
        if stop.is_set():
            return
        options = r["options"]
        block = "\n".join(f"{LETTERS[i]}. {opt}" for i, opt in enumerate(options))
        out, err = ask(cfg, PROMPT.format(question=r["question"], options=block))
        rec = {"id": r["id"], "provider": args.provider, "model": args.model, "prompt_style": "explain",
               "think": cfg["think"] if args.provider == "ollama" else thinking,
               "gold": r["answer"], "n_options": len(options)}
        if out is None:
            rec.update({"pred": None, "correct": False, "status": None, "error": err})
        else:
            rec.update(out)
            rec.update(outcome(out, len(options), r["answer"]))
        with lock:
            with open(out_path, "a", encoding="utf-8") as fh:
                fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
            counts["err" if rec["error"] else "ok"] += 1
            n = counts["ok"] + counts["err"]
            if rec["error"] and any(rec["error"].startswith(f) for f in FATAL_HTTP):
                print(f"fatal: {rec['error']}", flush=True)
                stop.set()
            elif n % 10 == 0 or n == len(todo):
                print(f"  {n}/{len(todo)} (errors {counts['err']})", flush=True)

    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        list(pool.map(work, todo))
    print(f"done: {counts['ok']} ok, {counts['err']} errors -> {os.path.relpath(out_path, REPO_ROOT)}")
    if stop.is_set():
        sys.exit(1)


if __name__ == "__main__":
    main()
