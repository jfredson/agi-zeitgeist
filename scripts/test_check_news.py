#!/usr/bin/env python3
"""Checks for scripts/check_news.py (the news posts; tracker pattern, rule 4.16).

    python3 scripts/test_check_news.py
"""
from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_news  # noqa: E402

AMEND = {"A25": ["2026-10-17"]}
GOOD = ("---\ntitle: The headline moves\ndate: 2026-10-18\nkind: headline-moved\nsummary: It moved.\nrecords: [A25]\n"
        "sources:\n  - label: The changelog\n    url: https://example.org/amendments\n---\n\n## What happened\n\n"
        "On 17 October 2026 John ruled it ([the changelog](https://example.org/amendments)).\n")


class NewsPosts(unittest.TestCase):
    def run_check(self, text, name="2026-10-18-the-headline-moves.md"):
        with tempfile.TemporaryDirectory() as tmp:
            d = Path(tmp); (d / name).write_text(text, encoding="utf-8")
            problems, n = check_news.check(d, AMEND, None)
        return problems

    def test_a_good_post_passes(self):
        self.assertEqual(self.run_check(GOOD), [])

    def test_a_figure_without_a_link_is_refused(self):
        bad = GOOD.replace("([the changelog](https://example.org/amendments))", "")
        self.assertTrue(any("states a figure with no link" in p for p in self.run_check(bad)))

    def test_an_unknown_amendment_is_refused(self):
        self.assertTrue(any("not in docs/amendments.md" in p for p in self.run_check(GOOD.replace("[A25]", "[A99]"))))

    def test_a_date_mismatch_is_refused(self):
        self.assertTrue(any("differs from the file name" in p for p in self.run_check(GOOD, name="2026-10-01-the-headline-moves.md")))

    def test_an_amendment_with_no_date_near_the_post_is_refused(self):
        far = GOOD.replace("date: 2026-10-18", "date: 2026-12-30")
        self.assertTrue(any("carries no date within" in p for p in self.run_check(far, name="2026-12-30-the-headline-moves.md")))

    def test_no_source_is_refused(self):
        bad = GOOD.replace("sources:\n  - label: The changelog\n    url: https://example.org/amendments\n", "")
        self.assertTrue(any("cites no source" in p for p in self.run_check(bad)))

    def test_the_opener_need_not_name_a_record(self):
        opener = GOOD.replace("kind: headline-moved", "kind: start-here").replace("records: [A25]\n", "")
        self.assertEqual(self.run_check(opener, name="2026-10-18-start-here.md"), [])

    def test_a_missing_card_is_refused(self):
        with tempfile.TemporaryDirectory() as tmp:
            d = Path(tmp); (d / "2026-10-18-the-headline-moves.md").write_text(GOOD, encoding="utf-8")
            problems, _ = check_news.check(d, AMEND, d)
        self.assertTrue(any("no card beside it" in p for p in problems))


class OpenChecks(unittest.TestCase):
    """Rule 3.3 part 4: no post while any claim carries an open check (added 2026-11-09)."""
    def claims(self, d, verify):
        line = f'verify = "{verify}"\n' if verify is not None else ""
        (d / "2025-01-01-x-a-claim.toml").write_text(f'[claim]\nid = "2025-01-01-x-a-claim"\n{line}', encoding="utf-8")

    def run_with(self, verify):
        with tempfile.TemporaryDirectory() as tmp:
            d = Path(tmp); posts = d / "news"; claims = d / "claims"; posts.mkdir(); claims.mkdir()
            (posts / "2026-10-18-the-headline-moves.md").write_text(GOOD, encoding="utf-8")
            self.claims(claims, verify)
            problems, _ = check_news.check(posts, AMEND, None, check_news.open_checks(claims))
        return problems

    def test_an_open_check_refuses_the_post(self):
        problems = self.run_with("Whether the quote matches the recording.")
        self.assertTrue(any("carry an open check" in p for p in problems))
        self.assertTrue(any("Whether the quote matches the recording." in p for p in problems))

    def test_no_check_lets_the_post_through(self):
        self.assertEqual(self.run_with(None), [])

    def test_an_unreadable_claim_counts_as_open(self):
        with tempfile.TemporaryDirectory() as tmp:
            d = Path(tmp); (d / "broken.toml").write_text("[claim\n", encoding="utf-8")
            self.assertEqual(len(check_news.open_checks(d)), 1)

    def test_the_live_record_has_no_open_check(self):
        self.assertEqual(check_news.open_checks(check_news.ROOT / "data" / "claims"), [])


if __name__ == "__main__":
    unittest.main()
