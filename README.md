# Nitesh Kumar | Portfolio

Personal site for Nitesh Kumar, Engineering Manager (platforms, developer productivity and distributed systems), based in Bengaluru.

## Sections

- **Hero and At a glance:** role, team size and the headline metrics
- **How I lead:** people and hiring, delivery, reliability, developer productivity and AI
- **Impact:** selected outcomes in numbers
- **Experience:** recent manager roles split into leadership and engineering work, with earlier roles in brief
- **Personal projects:** [Sidekick](https://github.com/coderArchitech/Sidekick) and [Flipbook](https://github.com/coderArchitech/flipbook)
- **Skills, education and contact**

## Structure

```
index.html                      single-page site (HTML, CSS and JS inline, no build step)
assets/Nitesh-Kumar-Resume.pdf  downloadable résumé
assets/projects/*.webp          project screenshots
vercel.json                     Vercel config
```

## Local preview

```bash
npx serve .
```

## Deploy

Push to the connected GitHub repository and Vercel deploys it (framework preset: **Other**). Or run `vercel` from this folder.

## Notes

- Light and dark themes follow the system setting; the toggle in the nav overrides it and remembers the choice.
- Fonts: Instrument Serif, Geist and Geist Mono, loaded from Google Fonts.
- Responsive down to 320px wide; respects `prefers-reduced-motion`; has a print stylesheet.
- To update the résumé, replace `assets/Nitesh-Kumar-Resume.pdf` and keep the same file name.
