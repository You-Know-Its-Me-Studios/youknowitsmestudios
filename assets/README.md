# Asset provenance

- `mountain-valley.webp`: artwork-only crop of the owner-supplied approved mockup (`codex-clipboard-M4Ldha.png`, 1672 × 941). Crop: left 780, top 78, right 1380, bottom 451. Excludes interface text, icons and product cards. The orbital outline is part of the supplied artwork; the hero headline and annotations are HTML. WebP quality 94.
- `favicon.svg`: legacy cyan mark, retained but no longer referenced by the website.
- `studio-logo.png`: unchanged copy of the owner-supplied `C:/Users/Josh/Desktop/You Know Its Me Studios/Images/YKIM Studios.png`, used as the browser tab icon and studio mark in the shared header and footer. The original file remains in place.
- `bodyhub-icon.svg`: exact path/fill conversion from `BodyHub/app/src/main/res/drawable/ic_bodyhub.xml`, without redesigning the actual app icon.
- `bodyhub-today.webp`: `BodyHub/artifacts/play-store/review/today-overview.png`.
- `bodyhub-workout.webp`: `BodyHub/artifacts/play-store/review/workout-edit.png`.
- Body Hub screenshots are real captured app UI with fictional demonstration records, documented in the Android checkout's `artifacts/play-store/INDEX.md` and capture manifest. Reduced proportionally to 720 × 1280, WebP quality 94. No UI was composited or generated. The homepage card displays a partial view of the full screenshot; the product page displays full images.
- `icons/`: Tabler outline icons, downloaded from the official `tabler/tabler-icons` repository, colored cyan. MIT license included.
- `nadir/icon.svg`: exact path/fill conversion of `Nadir/app/src/main/res/drawable/ic_nadir.xml`, with the app's `#041423` launcher background. No replacement icon was generated.
- `nadir/wordmark.svg`: exact path/stroke conversion of the current wordmark in `Nadir/app/src/main/java/com/nadir/app/ui/NadirBrand.kt`, including its cyan horizon. This is the app identity, not a new website logo.
- `nadir/instruments.webp`: authentic `.local-validation/corrective-pass/phone-main-portrait.png` from the separate Nadir Android project. Current Instruments UI on the ground, with current branding and no debug panel or precise coordinates. Proportionally reduced from 1440 × 3120 to 720 × 1560, WebP quality 92. The product page labels its on-ground state and links to the full web image.
- `nadir/offline-map.webp`: authentic `.local-validation/map-position/panned-follow-off.png` from Nadir. Crop `(0, 140, 1440, 1780)` removes the Android status bar and the lower live-position area, leaving an offline-world overview and airport markers. Reduced to 900 × 1025, WebP quality 92. Caption explicitly identifies the crop and retains OpenStreetMap, Protomaps, OpenMapTiles and OpenFreeMap attribution. No route, telemetry or interface was added.
- Nadir sources are in the separate `C:/Users/Josh/Desktop/Software Dev/Nadir` project, inspected October 7, 2026. Only the four web-facing files above were copied/converted; their combined size is approximately 133 KiB. The Android source and original captures were left unchanged.
- `fonts/`: Manrope 400/500/600/700/800 from Google Fonts, converted losslessly from TTF to WOFF2. SIL Open Font License included. All fonts are served locally; no Google Fonts request occurs in visitors' browsers. Italic display styling is synthesized from Manrope.

Strata assets were unavailable and omitted at the owner's direction. The mockup's sample app icon and interface were not used.
