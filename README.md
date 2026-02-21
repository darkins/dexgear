# DexGear — Documentation site

This repository contains the source for the DexGear documentation site, built with Astro, TypeScript, and Tailwind.

## Quick start

Install dependencies and run the dev server from the repository root:

```bash
npm install
npm run dev
```

Build for production and preview the build:

```bash
npm run build
npm run preview
```

## Requirements

- Node.js 18 or later is recommended (Astro v5+ works best on Node 18+).
- If you use TypeScript/content types, run Astro's sync to generate types (see below).

## Useful scripts

- **Dev:** `npm run dev` — starts the Astro dev server
- **Build:** `npm run build` — produce a production build
- **Preview:** `npm run preview` — preview the production build locally
- **Astro CLI:** `npm run astro -- <cmd>` — run an `astro` subcommand (e.g. `npm run astro -- sync`)

You can also run `npx astro sync` to generate/update auto-generated types when content or schemas change.

## Project layout (key files/folders)

- `src/` : site source — pages, layouts, components, and styles
  - `src/pages/` : Astro page routes (see `src/pages/gear/[slug].astro`)
  - `src/content/gear/` : markdown content used by the site
  - `src/layouts/` : page layouts (e.g. `MainLayout.astro`)
  - `src/styles/` : global CSS (Tailwind config)
- `content/gear/` : additional or canonical markdown content (mirrors site content). The site uses the content in `src/content/` at build time; `content/` is a canonical or auxiliary copy.
- `public/` : static assets (images, `robots.txt`, etc.)
- `pdf/` : PDF source files, reference docs, and scripts for generating PDFs
  - `pdf/scripts/` : utility scripts for extracting and manipulating PDFs
- `package.json`, `astro.config.mjs`, `tailwind.config.cjs`, `tsconfig.json` : build and config files

## Adding or editing gear pages

- Add or edit markdown files in `src/content/gear/` (or `content/gear/` if you prefer). Each gear MD file corresponds to a gear page.
- The route for gear pages is `/gear/[slug]` and is rendered by `src/pages/gear/[slug].astro`.

Notes:

- If you add or change content schemas, run `npx astro sync` (or `npm run astro -- sync`) to update generated TypeScript types.
- Use `src/content/gear/` for content you want published by the site; `content/gear/` can be used as a canonical source or for non-site workflows.

## Notes

- The site uses TypeScript and Tailwind; edit `tailwind.config.cjs` and `tsconfig.json` as needed.
- PDF-related sources and scripts live under `pdf/` and are separate from the Astro site build.
