# Portfolio — Jakub [Priezvisko]

Personal portfolio / CV. Plain HTML + CSS, no framework, no build step, no JavaScript.

```
index.html              main page (CV): about, experience, projects, skills, education, contact
projects/*.html         one page per project
projects/_template.html copy this to add a project
assets/css/style.css    all styling — colours and fonts are variables at the top
assets/fonts/           self-hosted Inter + IBM Plex Mono (no Google requests → no cookie banner)
assets/img/             images (WebP, ≤ ~300 kB each) + favicon.svg
cv.pdf                  your CV (add it — see "PDF CV" below)
404.html                "No signal." page
tools/                  image optimiser + pre-commit size guard
```

## Publish on GitHub Pages

1. Create a **public** repository named exactly `<username>.github.io`.
2. Push this folder to it:
   ```sh
   git init && git add . && git commit -m "Initial site"
   git branch -M main
   git remote add origin https://github.com/<username>/<username>.github.io.git
   git push -u origin main
   ```
3. On GitHub: **Settings → Pages → Build and deployment → Source: Deploy from a branch → `main` / `(root)`**.
4. After ~1 minute the site is live at `https://<username>.github.io`.

Every later `git push` redeploys automatically. Quick text fixes also work directly in the
GitHub web editor (press `.` on the repo page to open it).

## Edit content

| What | Where |
|---|---|
| Name, tagline, links | `index.html` → `<header class="panel">` |
| Experience / education entry | copy one `<article class="entry">` block |
| New project | copy `projects/_template.html`, then add an `<a class="project">` row in `index.html` |
| Colours | `assets/css/style.css` → `:root` (`--panel`, `--accent`, …) |

Search the files for `[` to find every placeholder still left to fill in.

## Images

Never commit raw phone photos — git keeps every version forever.

```sh
pip install pillow
python tools/optimize_images.py ~/Pictures/rig.jpg      # → assets/img/rig.webp (~200 kB)
cp tools/pre-commit .git/hooks/pre-commit && chmod +x .git/hooks/pre-commit   # blocks files > 500 kB
```

Videos → YouTube/Vimeo embed. KiCad projects, Gerbers, raw data → their own repositories, linked from the project page.

## PDF CV

The main page has a print stylesheet: open it in a browser → **Print → Save as PDF** (A4) and you get
a clean one-file CV without the navigation or colours. Save it as `cv.pdf` in the repo root.

## Custom domain later

1. Buy the domain (e.g. `priezvisko.eu`).
2. Add a file `CNAME` in the repo root containing just `priezvisko.eu`.
3. At the registrar, add DNS records:
   - `A` → `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   - `CNAME www` → `<username>.github.io`
4. GitHub → Settings → Pages → Custom domain → `priezvisko.eu`, then tick **Enforce HTTPS**.

## Licences

Inter and IBM Plex Mono are under the SIL Open Font License (see `assets/fonts/LICENSE-*.txt`).
