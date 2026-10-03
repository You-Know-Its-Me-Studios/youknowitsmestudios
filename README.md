
# You Know Its Me Studios

Static HTML, shared CSS and a small navigation script. No build step or runtime dependencies.

## Local preview

From the parent `GitHub Site` directory, run:

```powershell
python -m http.server 4173 --bind 127.0.0.1
```

Open `http://127.0.0.1:4173/youknowitsmestudios/`. Serving the parent directory tests the same project-path layout used by GitHub Pages.

## Maintenance

- `index.html`: studio homepage.
- `strata/index.html`, `bodyhub/index.html`: product presentations.
- `support/strata/`, `privacy/strata/`, and the four Body Hub resource pages retain their public routes and original substantive content.
- `styles.css`: shared tokens, layouts, controls and responsive styles.
- `script.js`: progressive mobile navigation and copyright year.
- `tools/sync_chrome.py`: source for the static shared header/footer. After changing it, run `python tools/sync_chrome.py` and commit the resulting HTML. Navigation and resource links work without JavaScript.
- `assets/README.md`: image and font provenance.
- `design-qa.md`: verification status and outstanding checks.

The homepage verification meta tag, `.nojekyll`, and existing deployment configuration are preserved. All website assets and internal links are relative to support GitHub Pages project paths.

## Content follow-up

Strata icon and screenshots were unavailable and omitted at the owner's direction. Its presentation uses text rather than invented app imagery. Add approved assets when available.

The existing Body Hub support, privacy and terms pages describe on-device AI, and the privacy page describes optional Health Connect background refresh. These existing statements were preserved verbatim, not validated as release commitments during this visual redesign. Confirm them against the intended release separately. Product marketing does not advertise smart/background AI features.
