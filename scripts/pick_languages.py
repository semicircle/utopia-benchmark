#!/usr/bin/env python3
"""Pick the two fixed languages of a Utopia release, by a rule anyone can rerun.

The rule looks only at the generated dialects, never at any model's results:

1. Candidates are seeds 100-999 with false friends on (`-semantics random`).
   Seeds below 100 are left for exploration and probes.
2. Each language on its own has 4 to 6 false friends: a setting that differs
   from the conventional one (`-semantics standard`).
3. Together the two cover every false friend: each setting differs from the
   conventional one in at least one of them. Division rounds toward negative
   infinity in one and toward positive infinity in the other; one groups
   operators flat from the left and the other flat from the right.
4. They look different: the function, if, switch and loop styles differ in
   every slot.
5. The first pair in seed order wins: the smallest first seed, then the
   smallest second seed.

    go build -o /tmp/utopia ./cmd/utopia
    python3 scripts/pick_languages.py /tmp/utopia
"""

import json
import subprocess
import sys

STANDARD = {
    "ArgOrder": "left-to-right", "OperandOrder": "left-to-right", "Div": "toward-zero",
    "IndexBase": 0, "OutOfRange": "error", "CountInclusive": True, "ShortCircuit": True,
    "SwitchFallthrough": False, "ListEqStructural": True, "Prec": "standard",
}


def info(exe, seed):
    out = subprocess.run([exe, "info", "-seed", str(seed), "-semantics", "random"],
                         capture_output=True, text=True, check=True).stdout
    return json.loads(out)


def friends(d):
    return {k for k, v in d["semantics"].items() if STANDARD[k] != v}


def pair_ok(a, b):
    fa, fb = friends(a), friends(b)
    if not (4 <= len(fa) <= 6 and 4 <= len(fb) <= 6):
        return False
    if fa | fb != set(STANDARD):
        return False
    divs = {a["semantics"]["Div"], b["semantics"]["Div"]}
    precs = {a["semantics"]["Prec"], b["semantics"]["Prec"]}
    if divs != {"toward-negative-infinity", "toward-positive-infinity"}:
        return False
    if precs != {"flat-left", "flat-right"}:
        return False
    return all(a["styles"][k] != b["styles"][k] for k in a["styles"])


def main():
    exe = sys.argv[1] if len(sys.argv) > 1 else "utopia"
    ds = {s: info(exe, s) for s in range(100, 1000)}
    ok = [s for s, d in ds.items() if 4 <= len(friends(d)) <= 6]
    for i, a in enumerate(ok):
        for b in ok[i + 1:]:
            if pair_ok(ds[a], ds[b]):
                for s in (a, b):
                    d = ds[s]
                    print(f"seed {s}: {d['name']} (.{d['ext']}) styles={d['styles']}")
                    print("  false friends: " + ", ".join(f"{k}={d['semantics'][k]}" for k in sorted(friends(d))))
                return
    raise SystemExit("no pair satisfies the rule")


if __name__ == "__main__":
    main()
