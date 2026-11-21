// Serves the static site from the assets binding. Any name other than the main one
// (www, or the Sentient Horizons subdomain) is sent to agizeitgeist.com so the site has
// one address to cite.
const MAIN = "agizeitgeist.com";

// Pages whose address changed after they were published. The old address forwards to the new
// one for good (301), so no link breaks. The news post on the lead-author rule was retitled
// under the title rules on 2026-11-20, the day it went up, on John's instruction.
const MOVED = {
  "/news/2026-11-20-a-jointly-written-piece-now-counts-only-for-its-lead-author/":
    "/news/2026-11-20-whose-agi-forecast-is-it-when-several-people-sign-it/",
  "/news/2026-11-20-a-jointly-written-piece-now-counts-only-for-its-lead-author-card.png":
    "/news/2026-11-20-whose-agi-forecast-is-it-when-several-people-sign-it-card.png",
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
      url.pathname = MOVED[path];
      return Response.redirect(url.toString(), 301);
    }
    return env.ASSETS.fetch(request);
  },
};
