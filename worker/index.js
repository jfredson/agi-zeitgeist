// Serves the static site from the assets binding. Any name other than the main one
// (www, or the Sentient Horizons subdomain) is sent to agizeitgeist.com so the site has
// one address to cite.
const MAIN = "agizeitgeist.com";

// Pages taken down or moved after they were published. Each old address forwards for good (301),
// so no link breaks. The news post on the lead-author rule (amendment A37) went up on 2026-11-20,
// was retitled the same evening, and was then taken off the site on John's ruling that the rule is
// part of settling the first version of the method, not news. Its addresses, and its cards, now
// forward to the rule itself on the amendments page.
const RULE = "/docs/amendments#a37-only-the-lead-author-of-a-jointly-written-piece-is-recorded";
const MOVED = {
  "/news/2026-11-20-a-jointly-written-piece-now-counts-only-for-its-lead-author/": RULE,
  "/news/2026-11-20-a-jointly-written-piece-now-counts-only-for-its-lead-author-card.png": RULE,
  "/news/2026-11-20-whose-agi-forecast-is-it-when-several-people-sign-it/": RULE,
  "/news/2026-11-20-whose-agi-forecast-is-it-when-several-people-sign-it-card.png": RULE,
};

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.hostname !== MAIN) {
      url.hostname = MAIN;
      return Response.redirect(url.toString(), 301);
    }
    const path = url.pathname.endsWith(".png") || url.pathname.endsWith("/") ? url.pathname : url.pathname + "/";
    if (MOVED[path]) {
      return Response.redirect(new URL(MOVED[path], url.origin).toString(), 301);
    }
    return env.ASSETS.fetch(request);
  },
};
