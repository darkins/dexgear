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

## Project layout (key files/folders)

- `src/` : site source — pages, layouts, components, and styles
  - `src/pages/` : Astro page routes (see `src/pages/gear/[slug].astro`)
  - `src/content/gear/` : markdown content used by the site
  - `src/layouts/` : page layouts (e.g. `MainLayout.astro`)
  - `src/styles/` : global CSS (Tailwind config)
- `content/gear/` : additional or canonical markdown content (mirrors site content)
- `public/` : static assets (images, `robots.txt`, etc.)
- `pdf/` : PDF source files, reference docs, and scripts for generating PDFs
  - `pdf/scripts/` : utility scripts for extracting and manipulating PDFs
- `package.json`, `astro.config.mjs`, `tailwind.config.cjs`, `tsconfig.json` : build and config files

## Adding or editing gear pages

- Add or edit markdown files in `src/content/gear/` (or `content/gear/` if you prefer). Each gear MD file corresponds to a gear page.
- The route for gear pages is `/gear/[slug]` and is rendered by `src/pages/gear/[slug].astro`.

## Notes

- The site uses TypeScript and Tailwind; edit `tailwind.config.cjs` and `tsconfig.json` as needed.
- PDF-related sources and scripts live under `pdf/` and are separate from the Astro site build.
