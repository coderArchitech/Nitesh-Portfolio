# Nitesh Kumar | Portfolio

Personal site for Nitesh Kumar, engineering leader targeting Engineering Manager roles (platforms, developer productivity and distributed systems), based in Bengaluru.

## Sections

- **Hero and At a glance:** role, team size and the headline metrics
- **How I lead:** people and hiring, delivery, reliability, developer productivity and AI
- **Impact:** selected outcomes in numbers
- **Experience:** recent manager roles split into leadership and engineering work, with earlier roles in brief
- **Personal projects:** [Sidekick](https://github.com/coderArchitech/Sidekick) and [Flipbook](https://github.com/coderArchitech/flipbook)
- **Skills:** six engineering-leadership areas first (people, delivery, technical leadership, operations, stakeholders, culture and productivity), then technical depth
- **Education and contact**

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

## Motion and interaction

- Staggered load-in for the hero, with a rotating word in the headline (reliable, scalable, observable)
- Hero glow that follows the cursor over a dot grid, and a gentle 3D tilt on the "At a glance" card
- Numbers count up when they scroll into view
- Cursor-aware spotlight and border glow on cards
- Scroll-linked experience timeline, top progress bar, and a back-to-top button with a progress ring
- Nav indicator that slides to the hovered or current section
- Project screenshots with parallax depth, hover lift, and a click-to-zoom lightbox
- Circular reveal when switching between light and dark themes
- "Copy email address" button with a confirmation toast
- Company names in a slow marquee that pauses on hover

All motion is turned off for visitors who set "reduce motion" in their OS. Content stays fully visible without JavaScript.

## Notes

- Light and dark themes follow the system setting; the toggle in the nav overrides it and remembers the choice.
- Fonts: Instrument Serif, Geist and Geist Mono, loaded from Google Fonts.
- Responsive down to 320px wide; respects `prefers-reduced-motion`; has a print stylesheet.
- To update the résumé, replace `assets/Nitesh-Kumar-Resume.pdf` and keep the same file name.
