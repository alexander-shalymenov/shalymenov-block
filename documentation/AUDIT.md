# Technical audit — Shalymenov Block 1.102

The complete FontBakery Google Fonts profile reports **0 FAIL, 0 FATAL and
0 ERROR**, with 593 PASS, 20 WARN,
251 SKIP and 29 INFO. No exclusions or
status overrides were used. This is not Google Fonts acceptance.

## Repairs

- Correct RIBBI style linking, weight metadata, OFL text, copyright, embedding
  permissions, script metadata, smart dropout and reproducible timestamps.
- Compact weight-specific accents, shared mark/mark-to-mark anchors, proper side
  carons, dotless j and contextual dot removal even with intervening below-marks.
- Repaired Light Æ needle, rounding steps, brace stems and Ł edge alignment.
- Connected currency-sign spokes; repaired Ə/ə counters, Ð/Đ crossbars, Ħ/ħ bar
  separation, Ŋ/ŋ returns and the feminine ordinal ª.
- Added missing Cyrillic and auxiliary Latin letters; removed the soft-hyphen
  encoding and its unreachable glyph. Full-stroke division dots have clear gaps.
- 828 encoded characters, 834 glyphs per weight. Exact
  coverage is in coverage.json; no claim of every historical Unicode character.
- In 1.102: i/j and related dot tops align to 800 in every weight; W/w are
  mirror-symmetric with level top terminals; V/W/Y pairs use shape-aware corner
  spacing. Capital bodies remain 800 and lowercase bodies 640.

## Validation

All four TTFs and WOFF2s pass OpenType Sanitizer. All supported canonical
compositions have matching NFC/NFD shaping. TTF and WOFF2 outlines and layout
tables match. Four editable UFO masters rebuild through fontmake without the
historical pipeline; a separate public-source build produced byte-identical
TTF and WOFF2 files. The family has no variable or italic font.

Browser checks cover all four real web fonts, editable text, sizes 6–240px,
leading, tracking, alignment, kerning, all character groups, grid inspection,
dark form controls and 320/390px layouts. Visual review covered compact marks,
stacked accents and repaired counters in Light and ExtraBold. This is display
type, not a pixel-font or a guarantee of readability at 6px.

## Metrics

UPM 1000; cap-height 800; x-height 640. Shared hhea/Typo ascender 1044,
descender -244, lineGap 0: **1.288em**, within the recommended 1.2–1.3em interval.
WinAscent 1232 and WinDescent 256 cover
all outlines. USE_TYPO_METRICS is enabled. Text with exceptional symbols or
stacked marks can still need greater CSS line-height; the specimen measures it.
Main letter strokes remain 96/120/160/176 units. Compact accent strokes are
46/58/77/84 units; accents are a separate, consistent construction class.

## Remaining warnings — retained in the original report

| Check | Count | Disposition |
| --- | ---: | --- |
| contour_count | 4 | Eight base designs differ from statistical contour counts: b has two bowls, g/ǥ are open, r has an R bowl, ß/ẞ have closed upper bowls, ħ has a second crossbar, and the dotted circle uses eight square dots. Other entries are accented composites with independent mark contours. These are mapped to the correct Unicode characters. |
| googlefonts/metadata/designer_profiles | 4 | The author is not in the Google Fonts designer catalogue. A supplied photograph and short biography are now prepared in catalog/designers/alexandershalymenov/. The catalogue designer name is Alexander Shalymenov. Upstream profile registration remains pending; preparing local files does not resolve this online warning. |
| googlefonts/metadata/unreachable_subsetting | 4 | The complete TTF/WOFF2 deliver all encoded characters. Google Fonts subset definitions omit some characters; documentation/subset-request.json specifies the requested coverage. Upstream acceptance is required before claiming identical Google Fonts API coverage. |
| outline_alignment_miss | 4 | These coordinates belong to accents, including stacked marks. They are near cap-height or the ascender by coincidence; neither line is an alignment target for those accent points. Moving individual points would deform the shared mark or break composed/decomposed consistency. |
| googlefonts/vendor_id | 4 | SHAL is not registered in the Microsoft vendor list. Retain the actual foundry code and request registration separately; do not impersonate an existing vendor. |

The detailed warning review lists every flagged contour and verifies that all
near-alignment warnings are accent points above correctly aligned base bodies.
It does not rewrite FontBakery's results. The subset proposal remains unresolved
for Google Fonts delivery; complete local WOFF2/TTF files do not have that gap.

## Intake status

The public GitHub project exists. The MediaDesign specimen is prepared locally,
not deployed to hosting. The family was submitted for review on 30 October 2026:
[google/fonts#11201](https://github.com/google/fonts/issues/11201). Catalogue
acceptance is pending. The individual CLA submission is confirmed by the author;
GitHub association still requires Google verification. The designer profile and supplied
portrait are prepared in catalog/designers/alexandershalymenov/, with a matching
catalogue designer name in METADATA.pb and AUTHORS.txt. Profile
registration, vendor registration and subset coordination remain separate actions. The name
also remains subject to editorial review. METADATA.pb is a draft: date_added is
a proposed intake date, to be replaced by Google with the actual date.

## Official references

- https://googlefonts.github.io/gf-guide/requirements.html
- https://googlefonts.github.io/gf-guide/statics
- https://googlefonts.github.io/gf-guide/metrics.html
- https://googlefonts.github.io/gf-guide/onboarding.html
- https://googlefonts.github.io/gf-guide/build.html
