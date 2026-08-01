# Neopulp — static site

Deployable as-is. No build step, no dependencies, no JavaScript.

    site/
      index.html      the landing page
      rules.html      full mark rules (replaces the old ASSETS.md)
      assets/         8 SVGs
      assets/png/     matching 4× PNGs

Drop the folder on any static host (Netlify, Cloudflare Pages, GitHub Pages, S3, plain nginx). `index.html` is the entry point; all links and asset paths are relative, so it also works opened straight from disk.

Typefaces (Archivo, JetBrains Mono) load from Google Fonts. To self-host, download both, drop the files in `assets/fonts/`, and swap the two `<link>` tags in each page for an `@font-face` block.

Asset tiles use `<a download>`, so clicking saves the file rather than opening it. Each tile downloads the SVG; the small PNG link inside downloads the 4× raster.
