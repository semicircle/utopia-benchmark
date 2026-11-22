"""A macOS Seatbelt (sandbox-exec) wrapper for scaffolds that have no sandbox
of their own, or whose own sandbox is not used here (Claude Code, Kimi).

The whole scaffold process runs inside it, so everything it starts (the
model's shell commands included) inherits the same limits:

- writes only in the workspace, the scaffold's own state folders and the
  temp folders;
- this repository cannot be read at all, so the hidden tests and reference
  solutions are out of reach;
- network is NOT blocked: the scaffold itself needs it to reach the model.
  Shell commands that use the network are flagged by each runner's audit.

sandbox-exec is deprecated by Apple but still ships with macOS. On other
systems, or when UTOPIA_NO_SEATBELT=1, commands run unwrapped and the run's
meta.json says so.
"""

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BIN = "/usr/bin/sandbox-exec"


def available():
    return sys.platform == "darwin" and os.path.exists(BIN) and os.environ.get("UTOPIA_NO_SEATBELT") != "1"


def _q(path):
    return '"' + str(path).replace("\\", "\\\\").replace('"', '\\"') + '"'


def _paths(paths):
    out = []
    for p in paths:
        p = Path(p).expanduser()
        for v in {str(p), os.path.realpath(p)}:
            if v not in out:
                out.append(v)
    return out


def profile(writable, unreadable=(ROOT,), writable_files=()):
    tmp = [os.environ.get("TMPDIR") or "/tmp", "/private/tmp", "/private/var/folders", "/dev",
           Path.home() / "Library" / "Caches"]
    allow = " ".join(f"(subpath {_q(p)})" for p in _paths([*writable, *tmp]))
    # Files written by atomic rename (name.tmp.123 -> name) need a prefix match.
    allow += "".join(f' (regex #"^{_re(p)}")' for p in _paths(writable_files))
    deny = " ".join(f"(subpath {_q(p)})" for p in _paths(unreadable))
    rules = ["(version 1)", "(allow default)", '(deny file-write* (subpath "/"))', f"(allow file-write* {allow})"]
    if deny:
        rules.append(f"(deny file-read* file-write* {deny})")
    return "\n".join(rules)


def _re(path):
    return "".join("\\" + c if c in ".^$*+?()[]{}|\\" else c for c in str(path))


def wrap(cmd, writable, unreadable=(ROOT,), writable_files=()):
    """(command, description). The description goes into meta.json."""
    if not available():
        return list(cmd), None
    return [BIN, "-p", profile(writable, unreadable, writable_files), *cmd], {
        "kind": "seatbelt", "writable": _paths(writable), "unreadable": _paths(unreadable), "network": "allowed"}

