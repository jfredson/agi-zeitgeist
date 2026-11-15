#!/usr/bin/env python3
"""Checks for the "Recent news" list beside each news post (scripts/site.py, recent_news; John, 2026-11-14).

    python3 scripts/test_recent_news.py
"""
from __future__ import annotations

import importlib.util
import re
import sys
import unittest
from pathlib import Path

# Loaded by its path: "site" is also the name of a module Python itself loads at start-up.
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
_spec = importlib.util.spec_from_file_location("zeitgeist_site", HERE / "site.py")
zsite = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(zsite)


def post(slug, date, title, kind="claim"):
    return {"slug": slug, "fm": {"date": date, "title": title, "kind": kind}}


OPENER = post("2026-10-18-start-here", "2026-10-18", "Where the test stands", kind="start-here")
DATED = [post(f"2026-11-{d:02d}-post-{d}", f"2026-11-{d:02d}", f"Post {d} & more") for d in range(10, 2, -1)]  # newest first


def titles(html):
    return re.findall(r'class="side-news-title" href="/news/([^/]+)/"', html)


class RecentNews(unittest.TestCase):
    def test_five_newest_other_posts_newest_first(self):
        html = zsite.recent_news(DATED, OPENER, DATED[1]["slug"])
        self.assertEqual(titles(html), [DATED[i]["slug"] for i in (0, 2, 3, 4, 5)])

    def test_the_post_being_read_is_left_out(self):
        html = zsite.recent_news(DATED, OPENER, DATED[0]["slug"])
        self.assertNotIn(DATED[0]["slug"], titles(html))
        self.assertEqual(len(titles(html)), 5)

    def test_date_written_out_and_title_escaped(self):
        html = zsite.recent_news(DATED, OPENER, OPENER["slug"])
        self.assertIn('<time datetime="2026-11-10">10 November 2026</time>', html)
        self.assertIn("Post 10 &amp; more", html)

    def test_a_labelled_navigation_region_headed_recent_news(self):
        html = zsite.recent_news(DATED, OPENER, DATED[0]["slug"])
        self.assertTrue(html.startswith('<nav class="side-news recent-news" aria-labelledby="recent-news-title">'))
        self.assertIn('<h2 id="recent-news-title">Recent news</h2>', html)
        self.assertIn('<a href="/news/">All news</a>', html)

    def test_start_here_link_shown_except_on_the_start_here_post(self):
        self.assertIn(f'href="/news/{OPENER["slug"]}/">Start with', zsite.recent_news(DATED, OPENER, DATED[0]["slug"]))
        on_opener = zsite.recent_news(DATED, OPENER, OPENER["slug"])
        self.assertNotIn("Start with", on_opener)
        self.assertIn("All news", on_opener)
        self.assertNotIn("Start with", zsite.recent_news(DATED, None, DATED[0]["slug"]))

    def test_start_here_post_is_never_in_the_list(self):
        self.assertNotIn(OPENER["slug"], titles(zsite.recent_news(DATED, OPENER, DATED[0]["slug"])))

    def test_nothing_when_there_is_no_other_post(self):
        self.assertEqual(zsite.recent_news(DATED[:1], OPENER, DATED[0]["slug"]), "")


if __name__ == "__main__":
    unittest.main()
