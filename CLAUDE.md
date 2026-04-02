# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Static brochure website for Southern Park Music School (Charlotte, NC). Deployed via **Cloudflare Workers Assets** (`wrangler.jsonc`). No build step — all files are served as-is.

## Development & Deployment

```bash
# Preview locally (requires Wrangler CLI)
npx wrangler dev

# Deploy to Cloudflare
npx wrangler deploy
```

There are no tests, linters, or build commands. Open HTML files directly in a browser or use `wrangler dev` for local preview.

## Architecture

| File | Purpose |
|------|---------|
| `index.html` | Home page — hero carousel, sections, footer |
| `faculty.html` | Faculty cards with live search/filter |
| `policies.html` | Static text policies page |
| `calendar.html` | Embedded Google Calendar |
| `gallery.html` | Photo gallery (admin-populated) |
| `404.html` | Custom error page |
| `style.css` | All custom CSS (Tailwind-first; overrides only) |
| `scripts.js` | Faculty card flip logic, search filter, navbar scroll |
| `sitemap.xml` | SEO sitemap |

**CSS stack:** Tailwind CSS (CDN), supplemented by `style.css` for custom components. Bootstrap (`bootstrap/`) is vendored locally but largely superseded by Tailwind — prefer Tailwind utilities.

**Fonts:** Playfair Display (headings) + Poppins (body) via Google Fonts.

**Brand colors:**
- Accent: `#C2410C` (orange-red), hover: `#9A3412`
- Background: off-white / warm neutrals
- CSS vars: `--accent`, `--accent-h`, `--radius`, `--shadow`, `--shadow-lg`

## Images

Files in `images/` with UUID names (e.g. `722e990b-...png`) are AI-generated placeholders and can be freely replaced. Named files (`amy.jpeg`, `gregory.avif`, `michael.jpg`, etc.) are real faculty/staff photos — do not remove them.

Logo files: `images/logo.png` (primary), `images/logo.gif`, `images/SPMS_542_icon.gif`.

## Design Principles

- Professional yet warm/inviting tone for a music school audience
- Maintain brown/off-white/orange color scheme; modernize aesthetics as needed
- Avoid code duplication — the navbar is shared via a common pattern across pages
- Keep files static; no server-side rendering or JS frameworks
