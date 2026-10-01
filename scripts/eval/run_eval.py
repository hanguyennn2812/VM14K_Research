#!/usr/bin/env python3
"""
run_eval.py — zero-shot MCQ evaluation of an LLM on VM14K.

Protocol follows the VM14K paper (arXiv 2506.01305, Appendix B / Fig. 6) so
numbers line up with its Tables 3-4: one fixed prompt for every model,
zero-shot, the model replies with a single option letter, scored as pass@1.

Deliberate differences from the paper:
  * dataset is data/cleaned/clean_final.jsonl scored on the frozen split
    (splits/split_v1.json, default: test), not the 12,488-row release;
  * decoding is greedy (temperature 0) so a rerun reproduces the same letter;
  * thinking is OFF unless --think (Ollama toggles it natively; for APIs pass
    the provider's switch through --extra-body).

Providers: Ollama (default; local models, and cloud models after
`ollama signin`) or any OpenAI-compatible API from PROVIDERS, keyed by the
matching environment variable.

Output: one JSONL row per question in reports/eval/runs/<run>.jsonl. Reruns
resume — ids that already have an error-free row are skipped — so a killed
run, or one stopped by a daily quota, just continues where it stopped.

    python scripts/eval/run_eval.py --model qwen3:8b --limit 20
    python scripts/eval/run_eval.py --model qwen3:8b
    python scripts/eval/run_eval.py --provider nvidia --model deepseek-ai/deepseek-v3.2 --rpm 35 --workers 4
    python scripts/eval/run_eval.py --provider groq --model openai/gpt-oss-120b --think on \\
        --extra-body '{"reasoning_effort": "low"}' --rpm 25
"""
import argparse
import concurrent.futures
import json
import os
import random
import re
import sys
import threading
import time
import urllib.error
import urllib.request

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DATA_PATH = os.path.join(REPO_ROOT, "data", "cleaned", "clean_final.jsonl")
SPLIT_PATH = os.path.join(REPO_ROOT, "splits", "split_v1.json")
RUNS_DIR = os.path.join(REPO_ROOT, "reports", "eval", "runs")

LETTERS = "ABCDEFG"

# OpenAI-compatible endpoints: name -> (base URL, API-key environment variable).
PROVIDERS = {
    "nvidia": ("https://integrate.api.nvidia.com/v1", "NVIDIA_API_KEY"),
    "groq": ("https://api.groq.com/openai/v1", "GROQ_API_KEY"),
    "cerebras": ("https://api.cerebras.ai/v1", "CEREBRAS_API_KEY"),
    "gemini": ("https://generativelanguage.googleapis.com/v1beta/openai", "GEMINI_API_KEY"),
    "openrouter": ("https://openrouter.ai/api/v1", "OPENROUTER_API_KEY"),
    "deepseek": ("https://api.deepseek.com", "DEEPSEEK_API_KEY"),
}

# Request fields that switch reasoning off, sent when --think is off and
# --extra-body is not given. Verified on NVIDIA (deepseek-v4.1-flash reasons
# by default and burns the token budget without them); chat templates ignore
# the kwarg they don't use, so both spellings go together.
NO_THINK_BODY = {
    "nvidia": {"chat_template_kwargs": {"thinking": False, "enable_thinking": False}},
}

# Fig. 6 of the paper, verbatim wording. The HTML rendering collapses
# whitespace, so the line breaks are our reconstruction.
PROMPTS = {
    "paper": (
        "{question}\n"
        "Choose the correct option from these answers:\n"
        "{options}\n"
        "Only response with 1 character\n"
        "Example: A"
    ),
    "vi": (
        "{question}\n"
        "Chọn đáp án đúng trong các phương án sau:\n"
        "{options}\n"
        "Chỉ trả lời đúng 1 ký tự là chữ cái của đáp án.\n"
        "Ví dụ: A"
    ),
}

_THINK_RE = re.compile(r"<think>.*?(?:</think>|$)", re.S | re.I)
_ANSWER_RE = re.compile(
    r"(?:đáp\s*án|answer)(?:\s*(?:đúng|correct))?\s*(?:là|is)?\s*[:\-]?\s*[*(\[]*\s*([A-G])(?!\w)",
    re.I,
)
_LETTER_RE = re.compile(r"(?<!\w)([A-G])(?!\w)")

# Stop the whole run on these instead of burning through every question.
FATAL_HTTP = ("HTTP 401", "HTTP 403", "HTTP 404", "HTTP 429")


def parse_letter(text, n_options):
    """First valid option letter in a reply, or None. Reasoning blocks are dropped."""
    if not text:
        return None
    text = _THINK_RE.sub("", text).strip()
    valid = LETTERS[:n_options]
    m = _ANSWER_RE.search(text)
    if m and m.group(1).upper() in valid:
        return m.group(1).upper()
    for m in _LETTER_RE.finditer(text):
        if m.group(1) in valid:
            return m.group(1)
    return None


def permute(row, shuffle_seed):
    """(options, gold_index, perm) as presented to the model.

    perm[i] is the original index of the option shown at position i. Seeded
    per question id, so every model sees the same order for the same seed.
    """
    n = len(row["options"])
    perm = list(range(n))
    if shuffle_seed is not None:
        random.Random(f"{shuffle_seed}:{row['id']}").shuffle(perm)
    options = [row["options"][i] for i in perm]
    return options, perm.index(row["answer_index"]), perm


def build_prompt(style, question, options):
    block = "\n".join(f"{LETTERS[i]}. {opt}" for i, opt in enumerate(options))
    return PROMPTS[style].format(question=question, options=block)


class Pacer:
    """Spaces request starts to stay under a requests-per-minute limit, across threads."""

    def __init__(self, rpm):
        self.interval = 60.0 / rpm if rpm else 0.0
        self.lock = threading.Lock()
        self.next_at = 0.0

    def wait(self):
        if not self.interval:
            return
        with self.lock:
            now = time.monotonic()
            start = max(now, self.next_at)
            self.next_at = start + self.interval
        time.sleep(start - now)


def _post(url, body, timeout, headers=None):
    req = urllib.request.Request(
        url,
        data=json.dumps(body).encode("utf-8"),
        headers={"Content-Type": "application/json", **(headers or {})},
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def post_with_retries(url, body, timeout, headers, pacer, retries):
    """(json, None) or (None, error string). Retries 429/5xx/network errors with backoff."""
    last_err = None
    for attempt in range(retries + 1):
        pacer.wait()
        wait = 3 * 2 ** attempt
        try:
            return _post(url, body, timeout, headers), None
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", "replace")[:300]
            last_err = f"HTTP {exc.code}: {detail}"
            if exc.code in (400, 401, 403, 404):
                break  # bad request / model name / key — retrying won't help
            retry_after = exc.headers.get("Retry-After") if exc.headers else None
            if retry_after and retry_after.replace(".", "", 1).isdigit():
                wait = float(retry_after)
        except (urllib.error.URLError, OSError, ValueError) as exc:
            last_err = repr(exc)
        if attempt < retries:
            time.sleep(min(wait, 120))
    return None, last_err


def ollama_capabilities(host, model):
    try:
        return set(_post(host.rstrip("/") + "/api/show", {"model": model}, 60).get("capabilities") or [])
    except (urllib.error.URLError, OSError, ValueError):
        return set()


def ask_ollama(cfg, prompt):
    body = {
        "model": cfg["model"],
        "messages": [{"role": "user", "content": prompt}],
        "stream": False,
        "keep_alive": "30m",
        "options": {"seed": 0, "num_predict": cfg["max_tokens"], "num_ctx": cfg["num_ctx"], **cfg["sampling"]},
        **cfg["extra_body"],
    }
    if cfg["think"] is not None:
        body["think"] = cfg["think"]
    resp, err = post_with_retries(cfg["host"].rstrip("/") + "/api/chat", body, cfg["timeout"], None,
                                  cfg["pacer"], cfg["retries"])
    if resp is None:
        return None, err
    msg = resp.get("message") or {}
    return {
        "raw": msg.get("content") or "",
        "reasoning_chars": len(msg.get("thinking") or ""),
        "done_reason": resp.get("done_reason"),
        "prompt_tokens": resp.get("prompt_eval_count"),
        "output_tokens": resp.get("eval_count"),
    }, None


def ask_openai(cfg, prompt):
    body = {
        "model": cfg["model"],
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": cfg["max_tokens"],
        **{k: v for k, v in cfg["sampling"].items() if k != "top_k"},  # top_k is not OpenAI-standard
        **cfg["extra_body"],
    }
    headers = {"Authorization": f"Bearer {cfg['api_key']}"}
    resp, err = post_with_retries(cfg["base_url"] + "/chat/completions", body, cfg["timeout"], headers,
                                  cfg["pacer"], cfg["retries"])
    if resp is None:
        return None, err
    choice = (resp.get("choices") or [{}])[0]
    msg = choice.get("message") or {}
    usage = resp.get("usage") or {}
    reasoning = msg.get("reasoning_content") or msg.get("reasoning") or ""
    return {
        "raw": msg.get("content") or "",
        "reasoning_chars": len(reasoning) if isinstance(reasoning, str) else 0,
        "done_reason": choice.get("finish_reason"),
        "prompt_tokens": usage.get("prompt_tokens"),
        "output_tokens": usage.get("completion_tokens"),
    }, None


def load_rows(split, limit, seed, data_path=DATA_PATH, ids=None):
    """Rows to score. With `ids`, exactly those ids from `data_path` and the split is
    ignored — that is how rows outside the cleaned split (raw release rows that
    cleaning removed) get scored."""
    with open(SPLIT_PATH, encoding="utf-8") as fh:
        split_of = json.load(fh)
    rows = []
    with open(data_path, encoding="utf-8") as fh:
        for line in fh:
            if not line.strip():
                continue
            r = json.loads(line)
            if ids is not None:
                if r["id"] not in ids:
                    continue
            elif split != "all" and split_of.get(r["id"]) != split:
                continue
            if r.get("contradiction_pending_review"):
                continue  # answer key unverified (BUG-2); never scored
            rows.append(r)
    if limit:
        rows = random.Random(seed).sample(rows, min(limit, len(rows)))
    return rows


def run_name(args):
    safe = re.sub(r"[^A-Za-z0-9._-]+", "_", args.model)
    scope = f"ids-{args.tag}" if args.ids else args.split
    parts = ([] if args.provider == "ollama" else [args.provider]) + [safe, args.prompt, scope]
    if args.think != "off":
        parts.append(f"think-{args.think}")
    if args.shuffle_seed is not None:
        parts.append(f"shuf{args.shuffle_seed}")
    if args.temperature:
        parts.append(f"t{args.temperature:g}")
    if args.limit:
        parts.append(f"n{args.limit}")
    return "__".join(parts)


def done_records(path):
    """{id: last error-free record} already in the output file."""
    if not os.path.exists(path):
        return {}
    ok = {}
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                rec = json.loads(line)
                if rec.get("error") is None:
                    ok[rec["id"]] = rec
    return ok


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--model", required=True, help="model id, e.g. qwen3:8b or deepseek-ai/deepseek-v3.2")
    ap.add_argument("--provider", default="ollama", choices=["ollama"] + sorted(PROVIDERS))
    ap.add_argument("--split", default="test", choices=["train", "val", "test", "all"])
    ap.add_argument("--data", default=DATA_PATH,
                    help="JSONL to score (default: cleaned dataset; e.g. data/raw/data-processed-shuffled0.jsonl)")
    ap.add_argument("--ids", default=None,
                    help="file with one question id per line: score exactly these, ignoring --split")
    ap.add_argument("--tag", default=None, help="run-name label for an --ids run (required with --ids)")
    ap.add_argument("--prompt", default="paper", choices=sorted(PROMPTS))
    ap.add_argument("--think", default="off", choices=["off", "on", "low", "medium", "high"],
                    help="thinking mode; also raises the token budget (default off)")
    ap.add_argument("--extra-body", default=None,
                    help='JSON merged into the request, e.g. \'{"reasoning_effort": "low"}\' '
                         '(default: the provider\'s no-think switch when --think is off)')
    ap.add_argument("--shuffle-seed", type=int, default=None,
                    help="permute options per question with this seed (paper's 'ensemble' uses 3 seeds)")
    ap.add_argument("--limit", type=int, default=0, help="random subsample of N rows (smoke tests)")
    ap.add_argument("--sample-seed", type=int, default=42)
    ap.add_argument("--workers", type=int, default=1, help="parallel requests (APIs / cloud models)")
    ap.add_argument("--rpm", type=float, default=0, help="max requests per minute (0 = unlimited)")
    ap.add_argument("--retries", type=int, default=5)
    ap.add_argument("--temperature", type=float, default=0.0,
                    help="default 0 (greedy, the protocol). Qwen3-style reasoning models loop under "
                         "greedy decoding; give their recommended sampling here and report it")
    ap.add_argument("--top-p", type=float, default=None)
    ap.add_argument("--top-k", type=int, default=None, help="Ollama only")
    ap.add_argument("--max-tokens", type=int, default=None)
    ap.add_argument("--num-ctx", type=int, default=None, help="Ollama context window")
    ap.add_argument("--timeout", type=int, default=600)
    ap.add_argument("--host", default=os.environ.get("OLLAMA_HOST_URL", "http://localhost:11434"))
    ap.add_argument("--out", default=None, help="override output JSONL path")
    args = ap.parse_args()

    thinking = args.think != "off"
    if args.extra_body is not None:
        extra_body = json.loads(args.extra_body)
    else:
        extra_body = {} if thinking else NO_THINK_BODY.get(args.provider, {})
    cfg = {
        "model": args.model,
        "max_tokens": args.max_tokens or (8192 if thinking else 32),
        "num_ctx": args.num_ctx or (16384 if thinking else 2048),
        "extra_body": extra_body,
        "sampling": {k: v for k, v in (("temperature", args.temperature), ("top_p", args.top_p),
                                       ("top_k", args.top_k)) if v is not None},
        "timeout": args.timeout,
        "retries": args.retries,
        "pacer": Pacer(args.rpm),
        "host": args.host,
        "think": None,
    }

    if args.provider == "ollama":
        ask = ask_ollama
        caps = ollama_capabilities(args.host, args.model)
        if "thinking" in caps:
            cfg["think"] = {"off": False, "on": True}.get(args.think, args.think)
        elif thinking:
            print(f"warning: {args.model} does not report 'thinking'; --think only raises the token budget",
                  file=sys.stderr)
        label = f"caps={sorted(caps) or '?'} think={cfg['think']}"
    else:
        ask = ask_openai
        cfg["base_url"], key_env = PROVIDERS[args.provider]
        cfg["api_key"] = os.environ.get(key_env)
        if not cfg["api_key"]:
            sys.exit(f"set {key_env} first (API key for {args.provider})")
        label = f"provider={args.provider} extra_body={cfg['extra_body']}"

    ids = None
    if args.ids:
        if not args.tag:
            sys.exit("--ids needs --tag (it names the run file)")
        with open(args.ids, encoding="utf-8") as fh:
            ids = {line.strip() for line in fh if line.strip()}
    rows = load_rows(args.split, args.limit, args.sample_seed, args.data, ids)
    out_path = args.out or os.path.join(RUNS_DIR, run_name(args) + ".jsonl")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    done = done_records(out_path)
    todo = [r for r in rows if r["id"] not in done]
    # The data file is grouped by topic; a seeded shuffle keeps partial results
    # (a quota cut-off, a killed run) representative of the whole split.
    random.Random(args.sample_seed).shuffle(todo)
    print(f"model={args.model} {label} split={args.split} rows={len(rows)} "
          f"done={len(rows) - len(todo)} todo={len(todo)}")
    print(f"out={os.path.relpath(out_path, REPO_ROOT)}")
    if not todo:
        prev = [done[r["id"]] for r in rows]
        print(f"finished: scored={len(prev)} acc={sum(p['correct'] for p in prev) / len(prev):.4f} "
              f"unparsed={sum(p['pred'] is None for p in prev)} errors=0 (already complete)")
        return

    lock = threading.Lock()
    stop = threading.Event()
    stats = {"n": 0, "correct": 0, "unparsed": 0, "truncated": 0, "errors": 0}
    t0 = time.time()

    def work(r):
        if stop.is_set():
            return None
        options, gold_idx, perm = permute(r, args.shuffle_seed)
        t = time.time()
        out, err = ask(cfg, build_prompt(args.prompt, r["question"], options))
        out = out or {}
        pred = parse_letter(out.get("raw"), len(options))
        gold = LETTERS[gold_idx]
        return {
            "id": r["id"],
            "provider": args.provider,
            "model": args.model,
            "prompt_style": args.prompt,
            "think": cfg["think"] if args.provider == "ollama" else args.think,
            "sampling": cfg["sampling"],
            "shuffle_seed": args.shuffle_seed,
            "split": f"ids-{args.tag}" if args.ids else args.split,
            "data": os.path.relpath(os.path.abspath(args.data), REPO_ROOT),
            "medical_topic": r["medical_topic"],
            "difficulty_level": r["difficulty_level"],
            "n_options": len(options),
            "perm": perm,
            "gold": gold,
            "pred": pred,
            "correct": pred == gold,
            "raw": out.get("raw", ""),
            "reasoning_chars": out.get("reasoning_chars", 0),
            "done_reason": out.get("done_reason"),
            "prompt_tokens": out.get("prompt_tokens"),
            "output_tokens": out.get("output_tokens"),
            "latency_s": round(time.time() - t, 3),
            "error": err,
        }

    def record(rec, fh):
        if rec is None:
            return
        with lock:
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
            fh.flush()
            if rec["error"]:
                stats["errors"] += 1
                if stats["errors"] == 1:
                    print(f"first error: {rec['error']}", file=sys.stderr, flush=True)
                if rec["error"].startswith(FATAL_HTTP) and not stop.is_set():
                    stop.set()
                    print(f"stopping: {rec['error'][:200]}\nrerun the same command later to resume.",
                          file=sys.stderr, flush=True)
            else:
                stats["n"] += 1
                stats["correct"] += rec["correct"]
                stats["unparsed"] += rec["pred"] is None
                stats["truncated"] += rec["pred"] is None and rec["done_reason"] == "length"
            k = stats["n"] + stats["errors"]
            if k % 25 == 0 or k == len(todo):
                rate = k / max(time.time() - t0, 1e-9)
                eta = (len(todo) - k) / rate if rate else 0
                acc = stats["correct"] / stats["n"] if stats["n"] else 0
                print(f"[{k}/{len(todo)}] acc={acc:.3f} unparsed={stats['unparsed']} "
                      f"errors={stats['errors']} {rate:.2f} q/s eta={eta / 60:.1f} min", flush=True)

    with open(out_path, "a", encoding="utf-8") as fh:
        if args.workers <= 1:
            for r in todo:
                if stop.is_set():
                    break
                record(work(r), fh)
        else:
            with concurrent.futures.ThreadPoolExecutor(args.workers) as pool:
                for rec in pool.map(work, todo):
                    record(rec, fh)

    n = stats["n"]
    print(f"finished: scored={n} acc={stats['correct'] / n if n else 0:.4f} "
          f"unparsed={stats['unparsed']} errors={stats['errors']} ({(time.time() - t0) / 60:.1f} min)")
    if stats["truncated"] > max(2, n // 20):
        print(f"hint: {stats['truncated']} replies hit the token limit before any letter — the model "
              f"probably reasons by default; rerun with --think on (or pass its no-think switch "
              f"via --extra-body).", file=sys.stderr)
    if stop.is_set():
        sys.exit(1)


if __name__ == "__main__":
    main()
