
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
- `about/index.html`: studio background, products and principles, based on existing published copy.
- `support/index.html`, `support/support.js`: shared support form and product preselection. Use `support/?product=bodyhub`, `support/?product=strata` or `support/?product=nadir` for product contact links.
- `strata/index.html`, `bodyhub/index.html`, `nadir/index.html`: product presentations.
- `nadir/privacy.html`: Nadir's current location, storage, export and online-provider disclosures. Product help is in `nadir/#help`.
- `support/strata/`, `privacy/strata/`, and the four Body Hub resource pages retain their public routes and original substantive content.
- `styles.css`: shared tokens, layouts, controls and responsive styles.
- `script.js`: progressive mobile navigation and copyright year.
- `tools/sync_chrome.py`: source for the static shared header/footer. After changing it, run `python tools/sync_chrome.py` and commit the resulting HTML. Navigation and resource links work without JavaScript.
- `assets/README.md`: image and font provenance.
- `design-qa.md`: verification status and outstanding checks.

The homepage verification meta tag, `.nojekyll`, and existing deployment configuration are preserved. All website assets and internal links are relative to support GitHub Pages project paths.

## Support form status

Online submission is intentionally unavailable, at the owner's direction. No form service, backend, service account or credentials have been created. The form visibly explains that it cannot deliver messages, its submit button is disabled, and its script prevents submission without sending or saving entered data. It does not show a submitting or success state because there is no delivery service.

The existing public contact address remains `youknowitsmestudios@gmail.com`. Company and contact details remain in the policies. All contact actions lead to the new form; the old product help pages and their section anchors remain available for troubleshooting and content ratings.

Enabling delivery later requires an explicitly approved service connected to that mailbox, provider spam protection, server-side validation, appropriate privacy disclosures, real submission/error handling and a verified end-to-end delivery check. Adding an endpoint alone is not sufficient. Never put private credentials in this static site.

## Checks and publishing

There is no package build. Refresh shared HTML with `python tools/sync_chrome.py`, then run `python tools/check_site.py` and `node --check support/support.js`. The link check covers every HTML page, local asset and fragment under `/youknowitsmestudios/`.

GitHub Pages publishes the root of `main` using the repository's existing **pages build and deployment** workflow. Do not move hosting or remove `.nojekyll`. `bodyhub/foreground-health-demo.mp4` is the existing public review video and must remain available.

## Content follow-up

Strata icon and screenshots were unavailable and omitted at the owner's direction. Its presentation uses text rather than invented app imagery. Add approved assets when available.

Nadir is presented as **in development for Android**. The separate `Software Dev/Nadir` Android project was inspected on October 7, 2026: README, DATA_SOURCES, RELEASE_AUDIT, Android manifest/dependencies, location/recording/map/provider/storage implementations and current UI. No public store listing was found in those sources. Do not add pricing, a download button or a release date without a verified public release. The website includes authentic Instruments and cropped offline-map captures; no flight track or in-flight sample was invented. Source details are in `assets/README.md`. The website has no runtime dependency on the Android project, and no Android files were changed.

Nadir copy distinguishes phone observations, the airport-to-airport reference route, offline maps and fresh online enrichment. Recheck the privacy notice when changing online providers, default settings, permissions, backups or storage. The existing support form remains intentionally unavailable for every product, including Nadir.

Body Hub resource copy was reconciled with the 0.10 Android implementation. Personal insights, independent background preferences, optional digests and cache deletion are documented. The approved layout, navigation and removed homepage hero/menu controls are preserved. No local preview, browser session or website screenshot session was run during this copy pass.
