// Serves the static site from the assets binding. Any name other than the main one
// (www, or the Sentient Horizons subdomain) is sent to agizeitgeist.com so the site has
// one address to cite.
const MAIN = "agizeitgeist.com";

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.hostname !== MAIN) {
      url.hostname = MAIN;
      return Response.redirect(url.toString(), 301);
    }
    return env.ASSETS.fetch(request);
  },
};
