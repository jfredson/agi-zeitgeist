// Makes the social preview image, site/social-preview.png (1200 by 630): the picture link previews
// on iMessage, Slack, X, Reddit and the rest show when the AGI Zeitgeist Tracker is shared. Drawn in the "Gazette" skin's own tokens (site/skin.css): newsprint, ink, the
// six faint column rules of the backdrop, the monospace dateline in red, the serif for the question,
// and the four gauge tracks with the red tick each part of the test has to reach. The tracks are
// empty on purpose: the picture is static, so it carries no number that would go stale.
//
// Run from the repository root after changing the skin or the home-page question:
//   npm install --no-save --prefix /tmp/social-image sharp
//   NODE_PATH=/tmp/social-image/node_modules node scripts/social-image.mjs
// (This repository has no Node project; the site is built by scripts/site.py, so sharp is fetched
// on the side only when the picture is remade, and the PNG is committed.)
import { createRequire } from 'node:module';
import { fileURLToPath } from 'node:url';

const require = createRequire(import.meta.url);
const sharp = require('sharp');

const W = 1200, H = 630;
const SANS = "'Helvetica Neue', Helvetica, Arial, sans-serif";
const SERIF = "Georgia, 'Iowan Old Style', 'Times New Roman', serif";
const MONO = "Menlo, 'SF Mono', Consolas, monospace";
const bg = '#f2f1ec', text = '#171614', soft = '#363430', muted = '#686661', accent = '#b8322a', data = '#4f6d8a';
const lineFaint = 'rgba(23,22,20,0.13)', lineStrong = 'rgba(23,22,20,0.24)';

// The backdrop: six column rules across the page, fading out toward the bottom.
let cols = '';
for (let i = 1; i < 6; i++) cols += `<line x1="${(W / 6) * i}" x2="${(W / 6) * i}" y1="0" y2="${H}"/>`;

// The four gauges: empty tracks, a red tick at the right edge of each (the line to reach).
const gx0 = 72, gx1 = W - 72, gap = 28, n = 4;
const gw = (gx1 - gx0 - gap * (n - 1)) / n;
let gauges = '';
for (let i = 0; i < n; i++) {
  const x = gx0 + i * (gw + gap), y = 478;
  gauges += `<rect x="${x}" y="${y}" width="${gw}" height="16" rx="2" fill="${data}" fill-opacity="0.14" stroke="${data}" stroke-opacity="0.5" stroke-width="1"/>`;
  gauges += `<line x1="${x + gw}" x2="${x + gw}" y1="${y - 9}" y2="${y + 25}" stroke="${accent}" stroke-width="3.5"/>`;
}

const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}">
<defs>
<linearGradient id="fade" x1="0" y1="0" x2="0" y2="1"><stop offset="0.45" stop-color="#fff"/><stop offset="1" stop-color="#000"/></linearGradient>
<mask id="m"><rect width="${W}" height="${H}" fill="url(#fade)"/></mask>
</defs>
<rect width="${W}" height="${H}" fill="${bg}"/>
<g mask="url(#m)" stroke="${lineFaint}" stroke-width="1.5">${cols}</g>
<text x="72" y="96" font-family="${MONO}" font-size="28" font-weight="700" letter-spacing="4" fill="${accent}">AGI ZEITGEIST TRACKER</text>
<g stroke="${lineStrong}" stroke-width="1"><line x1="72" x2="${W - 72}" y1="124" y2="124"/><line x1="72" x2="${W - 72}" y1="129" y2="129"/></g>
<text x="72" y="244" font-family="${SERIF}" font-size="96" font-weight="700" letter-spacing="-1.5" fill="${text}">Are we in the</text>
<text x="72" y="344" font-family="${SERIF}" font-size="96" font-weight="700" letter-spacing="-1.5" fill="${text}">singularity?</text>
<text x="72" y="410" font-family="${SANS}" font-size="27" fill="${soft}">Checks whether the singularity has started, and records when people expect AGI.</text>
${gauges}
<text x="72" y="568" font-family="${MONO}" font-size="26" fill="${muted}">agizeitgeist.com</text>
</svg>`;

const out = fileURLToPath(new URL('../site/social-preview.png', import.meta.url));
await sharp(Buffer.from(svg)).png({ compressionLevel: 9 }).toFile(out);
console.log('wrote', out);
