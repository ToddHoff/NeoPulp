# Neopulp — asset pack

Direction 1a, "The Mark". A format mark others apply to their own work, plus a reader promise.

## Files

| File | Use |
|---|---|
| `neopulp-wordmark-black.svg` | Primary wordmark, light surfaces |
| `neopulp-wordmark-reversed.svg` | Dark surfaces. NEO drops to stock white, PULP stays black on acid |
| `neopulp-wordmark-mono.svg` | One-ink print, embossing, legal/copyright pages. No highlight |
| `neopulp-stamp-full.svg` | Format stamp with reader promise. **34mm wide and up** |
| `neopulp-stamp-full-reversed.svg` | Same, dark covers |
| `neopulp-stamp-compact.svg` | Promise dropped. 22–34mm |
| `neopulp-stamp-badge.svg` | Smallest lockup. Spines, thumbnails, storefronts under 22mm |
| `neopulp-seal-square.svg` | Avatars, favicons, app tiles, die-cut stickers |
| `png/` | Rasterised at 4× for slides, social, and anything that won't take SVG |

## Ink

    #0D0C0B   press black    text, rules, stamp keyline
    #E8FF4D   signal acid    highlight and seed square ONLY — never type, never a field larger than the stamp
    #F2F0EB   bright white   stock

Two inks plus stock. No third colour, no tints, no gradients, no glow.

## Type

    Archivo 900     wordmark, titles, the reader promise
    Archivo 700     bylines
    JetBrains Mono  numbering, disclosure, all small caps-and-letterspaced text

## Rules

1. **One word.** NEOPULP — never spaced, never camel-cased, never hyphenated. Lowercase "neopulp" in body copy, because it is a common noun.
2. **The highlight sits behind PULP only.** The insult is the part that gets highlighted. Never behind the whole word.
3. **Clear space** = the cap-height of the wordmark on all four sides. Nothing enters it.
4. **Minimum sizes.** Stamp 22mm wide in print, 96px on screen. Below that, use the badge. Wordmark never below 11px.
5. **The acid square is fixed.** Same size relative to the wordmark's cap-height, always top-right of the stamp, always keylined.
6. **Never rotate the stamp.** It is not a sticker. (That is Slopcore's job, and Slopcore never touches a product.)
7. **Never lock up with Slopcore.** Not in the same file, not on the same surface, not in the same week's campaign asset.

## Locked wording

**Reader promise** — on the stamp, back cover, and storefront line:

> A human vision, perfected.

**Credit line** — title page, at byline scale, above the fold:

> Seeded by [name]
>
> The premise, structure and direction of this book are hers.
> The sentences were written by a machine at her instruction.

**Shelf / search language:** idea-first fiction.

**Never:** "AI-assisted", "co-created", "in collaboration with", "AI-generated", or any sentence beginning "While some may…".

## Series numbering

`№ 004` in JetBrains Mono, head of the spine or top-left of the cover. Roman numerals are direction 1c's convention — not used here.

## Font note

The SVGs reference Archivo and JetBrains Mono by name (both open-licence, Google Fonts). Convert text to outlines before sending to a printer, or install the fonts. Widths are pinned with `textLength`, so the lockups stay dimensionally correct even if a fallback font substitutes.
