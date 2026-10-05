#!/usr/bin/env python3
"""Three-model coding of the r/singularity pilot's 140-post set (amendment section 9 as
ruled by John, 2026-10-03): Claude, Gemini and GPT code each post blind.

For each field it reports Cohen's kappa (agreement corrected for chance) for all three
pairs of models, sets the final code by majority vote, and applies John's reliability
test: a field is unreliable, and kept out of figures, if it is unresolved on more than 15%
of posts or if every pairwise kappa is below 0.6.

Unit: one post. Eligibility is compared on every post. The main claim's fields (claim_n 1)
and the post-level fields (title_only, extrapolates_to_horizon) are compared, for each pair,
on posts both models found eligible. Majority vote: eligibility by at least two of three;
for the other fields, a value needs at least two models to give it. A model that found the
post ineligible gives no value, so with one such model the other two must agree. Fields
are voted only for posts the majority finds eligible; otherwise the field is unresolved.

    python3 scripts/vanguard_three_way.py                 # the main codes
    python3 scripts/vanguard_three_way.py --rules-trial   # the codes made with trial rules
    python3 scripts/vanguard_three_way.py --compare       # before and after the trial rules,
                                                          # on the posts all three trial runs coded
    python3 scripts/vanguard_three_way.py --r1-split      # rules R1a (stance) and R1b (attribution),
                                                          # each trialled alone on the 112 posts
    python3 scripts/vanguard_three_way.py --full          # the full-sample run: all 390 posts, each
                                                          # model coding under the final codebook

"Whether the poster wants AI sped up or slowed down" (development_preference) is listed as
unreliable by John's ruling of 2026-10-03, whatever its kappas.

Writes data/vanguard/r-singularity-pilot-codes-majority.csv and
data/vanguard/three-model-reliability.csv (main codes), or the same names ending -full-final
(--full).
"""

import csv
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from vanguard_agreement import kappa  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
D = ROOT / "data" / "vanguard"
SUBSET = D / "second-coder-worksheet.csv"
MAIN = {"claude": [D / "r-singularity-pilot-codes.csv", D / "r-singularity-pilot-codes-claude-subset-supplement.csv"],
        "gemini": [D / "r-singularity-pilot-codes-crossfamily.csv"],
        "gpt": [D / "r-singularity-pilot-codes-gpt.csv"]}
TRIAL = {k: [D / f"r-singularity-pilot-codes-{k}-rules-trial.csv"] if k != "gemini"
         else [D / "r-singularity-pilot-codes-crossfamily-rules-trial.csv"] for k in MAIN}
FIELDS = ["claim_target", "temporal_status", "stance", "epistemic_qualification", "rhetorical_mode",
          "development_preference", "attribution", "title_only", "extrapolates_to_horizon"]
PAIRS = [("claude", "gemini"), ("claude", "gpt"), ("gemini", "gpt")]
UNRESOLVED_LIMIT, KAPPA_FLOOR = 0.15, 0.6
RULED_UNRELIABLE = {"development_preference": "ruled unreliable by John, 2026-10-03"}
R1_POSTS = D / "r1-split-trial-posts.csv"
FULL_POSTS = D / "full-run-posts.csv"
FULL = {m: [D / f"r-singularity-pilot-codes-{name}-full-final.csv"]
        for m, name in (("claude", "claude"), ("gemini", "crossfamily"), ("gpt", "gpt"))}
SPLIT = {tag: {"claude": [D / f"r-singularity-pilot-codes-claude-{tag}.csv"],
               "gemini": [D / f"r-singularity-pilot-codes-crossfamily-{tag}.csv"],
               "gpt": [D / f"r-singularity-pilot-codes-gpt-{tag}.csv"]} for tag in ("r1a-trial", "r1b-trial")}


def subset_ids():
    with SUBSET.open(newline="") as f:
        return [r["post_id"] for r in csv.DictReader(f)]


def load(paths, ids):
    """Post id -> main-claim row (with the post-level fields), for posts in the set."""
    out = {}
    for path in paths:
        with path.open(newline="") as f:
            for r in csv.DictReader(f):
                if r["post_id"] not in ids:
                    continue
                if r["post_id"] not in out or r["claim_n"] == "1":
                    out[r["post_id"]] = r
    return out


def value(row, field):
    return (row.get(field) or "").strip()


def pairwise(codes, ids):
    """{field: {pair: (n, agreement, kappa)}}"""
    res = {}
    for field in ["eligible"] + FIELDS:
        res[field] = {}
        for a, b in PAIRS:
            both = [i for i in ids if i in codes[a] and i in codes[b]]
            if field != "eligible":
                both = [i for i in both if value(codes[a][i], "eligible") == "yes" == value(codes[b][i], "eligible")]
            pairs = [(value(codes[a][i], field), value(codes[b][i], field)) for i in both]
            res[field][(a, b)] = (len(pairs), sum(x == y for x, y in pairs) / len(pairs) if pairs else None,
                                  kappa(pairs) if pairs else None)
    return res


def majority(codes, ids):
    """{post id: {field: value or "unresolved"}}"""
    final = {}
    for i in ids:
        votes = [codes[m][i] for m in codes if i in codes[m]]
        elig = Counter(value(r, "eligible") for r in votes).most_common(1)[0]
        post = {"eligible": elig[0] if elig[1] >= 2 else "unresolved"}
        voters = [r for r in votes if value(r, "eligible") == "yes"]
        for field in FIELDS:
            if post["eligible"] != "yes":
                post[field] = ""
                continue
            top = Counter(value(r, field) for r in voters).most_common(1)
            post[field] = top[0][0] if top and top[0][1] >= 2 else "unresolved"
        final[i] = post
    return final


def verdicts(res, final):
    eligible = [p for p in final.values() if p["eligible"] == "yes"]
    out = {}
    for field in ["eligible"] + FIELDS:
        pool = list(final.values()) if field == "eligible" else eligible
        unresolved = sum(p[field] == "unresolved" for p in pool) / len(pool)
        ks = [k for _, _, k in res[field].values() if k is not None]
        reasons = []
        if unresolved > UNRESOLVED_LIMIT:
            reasons.append(f"unresolved on {unresolved:.0%} of posts")
        if ks and all(k < KAPPA_FLOOR for k in ks):
            reasons.append("every pairwise kappa below 0.6")
        if field in RULED_UNRELIABLE:
            reasons.append(RULED_UNRELIABLE[field])
        out[field] = (unresolved, len(pool), "unreliable: " + "; ".join(reasons) if reasons else "reliable")
    return out


def report(label, codes, ids, write=None):
    """write: None, or (reliability file, majority file, post list giving quarter and sample)."""
    res = pairwise(codes, ids)
    final = majority(codes, ids)
    ver = verdicts(res, final)
    print(f"\n{label}: {len(ids)} posts; coded by claude {len(codes['claude'])}, gemini {len(codes['gemini'])}, "
          f"gpt {len(codes['gpt'])}; majority eligible {sum(p['eligible'] == 'yes' for p in final.values())}")
    print(f"{'field':26} " + " ".join(f"{a[:6]}-{b[:6]:>6} (n)  " for a, b in PAIRS) + " unresolved  verdict")
    rows = []
    for field in ["eligible"] + FIELDS:
        cells = []
        for pair in PAIRS:
            n, agree, k = res[field][pair]
            cells.append(f"{k:>6.2f} ({n:>3})   " if k is not None else f"{'-':>6} ({n:>3})   ")
        unresolved, pool, verdict = ver[field]
        print(f"{field:26} " + " ".join(cells) + f" {unresolved:>6.0%}     {verdict}")
        rows.append([field] + [x for pair in PAIRS for x in (res[field][pair][0],
                     round(res[field][pair][1], 3) if res[field][pair][1] is not None else "",
                     round(res[field][pair][2], 3) if res[field][pair][2] is not None else "")]
                    + [pool, round(unresolved, 3), verdict])
    if write:
        rel_path, maj_path, meta_path = write
        with rel_path.open("w", newline="") as f:
            w = csv.writer(f, lineterminator="\n")
            w.writerow(["field"] + [f"{a}_{b}_{x}" for a, b in PAIRS for x in ("n", "agreement", "kappa")]
                       + ["posts_voted", "unresolved_share", "verdict"])
            w.writerows(rows)
        with meta_path.open(newline="") as f:
            meta = {r["post_id"]: r for r in csv.DictReader(f)}
        types = {i: r["post_type"] for c in codes.values() for i, r in c.items()}
        with maj_path.open("w", newline="") as f:
            w = csv.writer(f, lineterminator="\n")
            w.writerow(["post_id", "quarter", "sample", "post_type", "eligible"] + FIELDS)
            for i in ids:
                m = meta[i]
                w.writerow([i, m["quarter"], m["sample"], m.get("post_type") or types.get(i, ""), final[i]["eligible"]]
                           + [final[i][fl] for fl in FIELDS])
    return res, final, ver


def main():
    ids = subset_ids()
    idset = set(ids)
    if "--r1-split" in sys.argv:
        with R1_POSTS.open(newline="") as f:
            r1ids = [r["post_id"] for r in csv.DictReader(f)]
        sets = {"before": MAIN, **SPLIT}
        loaded = {k: {m: load([q for q in p if q.exists()], set(r1ids)) for m, p in v.items()} for k, v in sets.items()}
        common = [i for i in r1ids if all(i in loaded[k][m] for k in loaded for m in loaded[k])]
        res = {k: report(f"{k} ({len(common)} posts)", {m: {i: c[i] for i in common} for m, c in v.items()}, common)[0]
               for k, v in loaded.items()}
        for rule, field, control in (("R1a", "stance", "r1b-trial"), ("R1b", "attribution", "r1a-trial")):
            tag = "r1a-trial" if rule == "R1a" else "r1b-trial"
            print(f"\n{rule} on {field}, {len(common)} posts: before (original codebook) / without {rule} "
                  f"(same codebook, other split's run) / with {rule}")
            for pair in PAIRS:
                k = [res[x][field][pair][2] for x in ("before", control, tag)]
                print(f"  {pair[0]}-{pair[1]}: " + " / ".join(f"{v:.2f}" if v is not None else "-" for v in k))
    elif "--compare" in sys.argv:
        trial = {m: load(p, idset) for m, p in TRIAL.items()}
        common = [i for i in ids if all(i in trial[m] for m in trial)]
        before = report("Before (main codes)", {m: load(p, set(common)) for m, p in MAIN.items()}, common)[0]
        after = report("After (trial rules)", {m: load(p, set(common)) for m, p in TRIAL.items()}, common)[0]
        print(f"\nKappa before -> after on the same {len(common)} posts")
        print(f"{'field':26} " + "  ".join(f"{a}-{b}" for a, b in PAIRS))
        for field in ["eligible"] + FIELDS:
            cells = []
            for pair in PAIRS:
                kb, ka = before[field][pair][2], after[field][pair][2]
                cells.append(f"{kb:.2f} -> {ka:.2f}" if kb is not None and ka is not None else "-")
            print(f"{field:26} " + "    ".join(cells))
    elif "--full" in sys.argv:
        missing = [str(p) for ps in FULL.values() for p in ps if not p.exists()]
        if missing:
            raise SystemExit("stopped: not all three models have coded the full sample yet: " + ", ".join(missing))
        with FULL_POSTS.open(newline="") as f:
            fids = [r["post_id"] for r in csv.DictReader(f)]
        codes = {m: load(p, set(fids)) for m, p in FULL.items()}
        short = {m: len(fids) - len(c) for m, c in codes.items() if len(c) < len(fids)}
        if short:
            print(f"note: posts not yet coded: {short}; the comparison uses the posts each pair shares")
        report("Full sample, final codebook", codes, fids,
               write=(D / "three-model-reliability-full-final.csv",
                      D / "r-singularity-pilot-codes-majority-full-final.csv", FULL_POSTS))
    elif "--rules-trial" in sys.argv:
        report("Trial rules", {m: load(p, idset) for m, p in TRIAL.items()}, ids)
    else:
        report("Main codes", {m: load(p, idset) for m, p in MAIN.items()}, ids,
               write=(D / "three-model-reliability.csv", D / "r-singularity-pilot-codes-majority.csv", SUBSET))


if __name__ == "__main__":
    main()
