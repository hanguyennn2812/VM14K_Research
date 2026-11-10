#!/usr/bin/env python3
"""Shorten tracked file paths longer than LIMIT characters by cutting the file stem at an underscore.

Keeps the start of the name (decision number, date, title) and any _partNN suffix, renames with `git mv`, and
rewrites every tracked text file that quotes an old path or old file name. MoH chunk ids are content hashes, so
they do not change. Dry run by default.

    python scripts/analysis/shorten_long_paths.py            # show the plan
    python scripts/analysis/shorten_long_paths.py --apply
"""
import argparse
import re
import subprocess
from pathlib import Path, PurePosixPath

LIMIT = 200
TEXT_EXT = {".tex", ".json", ".jsonl", ".md", ".csv", ".txt", ".py", ".yaml", ".yml"}


def git(*args):
    return subprocess.run(["git", "-c", "core.quotepath=false", *args], capture_output=True, text=True,
                          encoding="utf-8", check=True).stdout


def short_name(path, limit=LIMIT):
    p = PurePosixPath(path)
    m = re.search(r"(_part\d+)$", p.stem)
    suffix = (m.group(1) if m else "") + p.suffix
    stem = p.stem[:m.start()] if m else p.stem
    room = limit - len(str(p.parent)) - 1 - len(suffix)
    assert room >= 20, f"folder too long for {path}"
    cut = stem[:room]
    if len(stem) > room and "_" in cut:
        cut = cut[:cut.rindex("_")]
    return str(p.parent / (cut.rstrip("_") + suffix))


def plan(files):
    renames = {f: short_name(f) for f in files if len(f) > LIMIT}
    targets = list(renames.values())
    assert len(set(targets)) == len(targets), "two files would get the same name"
    assert not set(targets) & set(files), "a new name already exists"
    assert all(len(t) <= LIMIT for t in targets)
    return renames


def selfcheck():
    long = "data/Chuyên khoa/HIV/" + "Quyet_dinh_so_2834_" + "abc_" * 60 + "part01.pdf"
    s = short_name(long)
    assert len(s) <= LIMIT and s.endswith("_part01.pdf") and s.startswith("data/Chuyên khoa/HIV/Quyet_dinh_so_2834_"), s
    assert short_name("a/b.pdf") == "a/b.pdf"


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    selfcheck()
    files = git("ls-files", "-z").split("\0")
    files = [f for f in files if f]
    renames = plan(files)
    for old, new in renames.items():
        print(f"{len(old)} -> {len(new)}  {PurePosixPath(new).name}")
    texts = [f for f in files if PurePosixPath(f).suffix in TEXT_EXT and f not in renames]
    # Ignored corpus caches (moh_corpus_audit output) quote file names too.
    texts += [str(p.as_posix()) for p in Path("data/interim").glob("moh_corpus_*.jsonl")]
    pairs = [(o, n) for o, n in renames.items()] + [(PurePosixPath(o).name, PurePosixPath(n).name)
                                                     for o, n in renames.items()]
    pairs += [(PurePosixPath(o).stem, PurePosixPath(n).stem) for o, n in renames.items()]
    touched = {}
    for f in texts:
        try:
            body = open(f, encoding="utf-8").read()
        except (UnicodeDecodeError, FileNotFoundError):
            continue
        new = body
        for o, n in pairs:  # full paths first, then names, then stems
            new = new.replace(o, n)
        if new != body:
            touched[f] = new
    print(f"{len(renames)} files to rename; {len(touched)} text files to update: {sorted(touched)}")
    if not args.apply:
        return
    for old, new in renames.items():
        git("mv", old, new)
    for f, body in touched.items():
        with open(f, "w", encoding="utf-8", newline="") as fh:
            fh.write(body)
    left = [f for f in git("ls-files", "-z").split("\0") if len(f) > LIMIT]
    assert not left, left
    print("done; longest tracked path now", max(len(f) for f in git("ls-files", "-z").split("\0") if f))


if __name__ == "__main__":
    main()
