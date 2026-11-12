# FamilyKit colour palette v1.0

Built 11 Nov 2026 from the founder's colour document. All ramps are built in **OKLCH**, so each step is an even jump in perceived lightness, then output as sRGB hex. **DOC** marks a value copied unchanged from the document. primary-700 is the one exception: it's the current landing button colour, kept as is.

Files in this folder:
- `tokens.css`: CSS variables (ramps, then role tokens, then remapped legacy landing tokens).
- `palette.json`: every step with its OKLCH values, contrast against white (`cw`) and against black (`ck`), and the role map.
- `01–06@2x.png`: one spec sheet per section.
- `build.py`, `pages.py`, `render.py`: the scripts that regenerate everything.

> The doc says its hex values were sampled from an image and are approximate. I kept them exactly as anchors so they stay recognisable. If the brand file has the true values, swap them into `build.py` and rerun it.

## 1. Primary: Royal Purple
| Step | Hex | OKLCH L / C / H | vs white | Source |
|---|---|---|---|---|
| primary-50 | `#F7F5FD` | 0.974 / 0.011 / 298 | 1.08:1 | generated |
| primary-100 | `#EBE6F7` | 0.934 / 0.023 / 299 | 1.22:1 | **DOC** Primary 10 |
| primary-200 | `#D9D0F3` | 0.876 / 0.049 / 297 | 1.47:1 | generated |
| primary-300 | `#C2B0F0` | 0.795 / 0.091 / 297 | 1.95:1 | generated |
| primary-400 | `#A78EE7` | 0.704 / 0.129 / 296 | 2.74:1 | generated |
| primary-500 | `#8B6ADA` | 0.609 / 0.165 / 295 | 4.06:1 | generated |
| primary-600 | `#7543C7` | 0.514 / 0.195 / 296 | 6.21:1 | **DOC** Doc text colour |
| primary-700 | `#4A13B7` | 0.405 / 0.221 / 286 | 10.15:1 | **DOC** Kept: current landing button |
| primary-800 | `#2D0B84` | 0.313 / 0.175 / 282 | 14.07:1 | **DOC** Primary Main |
| primary-900 | `#21025E` | 0.245 / 0.140 / 285 | 17.0:1 | generated |
| primary-950 | `#130438` | 0.183 / 0.093 / 287 | 19.05:1 | **DOC** Primary 100 |

## 2. Accents
### Lavender (Accent 2)
| Step | Hex | OKLCH L / C / H | vs white | Source |
|---|---|---|---|---|
| lavender-50 | `#F7F5FF` | 0.975 / 0.013 / 295 | 1.08:1 | generated |
| lavender-100 | `#EEE9FF` | 0.944 / 0.030 / 296 | 1.18:1 | generated |
| lavender-200 | `#DDD3FF` | 0.889 / 0.061 / 296 | 1.42:1 | generated |
| lavender-300 | `#C8B5FF` | 0.815 / 0.104 / 296 | 1.82:1 | generated |
| lavender-400 | `#B294FF` | 0.737 / 0.153 / 295 | 2.45:1 | **DOC** Accent 2 Lavender |
| lavender-500 | `#996DF8` | 0.646 / 0.199 / 295 | 3.56:1 | generated |
| lavender-600 | `#8049E3` | 0.555 / 0.220 / 294 | 5.28:1 | generated |
| lavender-700 | `#6634BD` | 0.470 / 0.200 / 294 | 7.52:1 | generated |
| lavender-800 | `#4D2793` | 0.391 / 0.165 / 293 | 10.36:1 | generated |
| lavender-900 | `#361A6A` | 0.310 / 0.130 / 293 | 13.88:1 | generated |

### Lime (Accent 1). The doc's Yellow is now lime-400.
| Step | Hex | OKLCH L / C / H | vs white | Source |
|---|---|---|---|---|
| lime-50 | `#F9FFDF` | 0.987 / 0.042 / 116 | 1.03:1 | generated |
| lime-100 | `#EFFF94` | 0.965 / 0.133 / 116 | 1.08:1 | **DOC** Accent 1 Lime |
| lime-200 | `#EAF17D` | 0.929 / 0.140 / 112 | 1.21:1 | generated |
| lime-300 | `#E3E26D` | 0.890 / 0.140 / 108 | 1.37:1 | generated |
| lime-400 | `#DAD05A` | 0.843 / 0.139 / 104 | 1.6:1 | **DOC** Accent 1 Yellow |
| lime-500 | `#BEB542` | 0.759 / 0.134 / 105 | 2.13:1 | generated |
| lime-600 | `#9E9621` | 0.660 / 0.130 / 105 | 3.07:1 | generated |
| lime-700 | `#7F7800` | 0.561 / 0.119 / 106 | 4.58:1 | generated |
| lime-800 | `#605B00` | 0.461 / 0.098 / 106 | 7.01:1 | generated |
| lime-900 | `#433F00` | 0.360 / 0.077 / 106 | 10.77:1 | generated |

## 3. Neutrals (purple-tinted, hue ≈ 298)
| Step | Hex | OKLCH L / C / H | vs white | Source |
|---|---|---|---|---|
| neutral-0 | `#FFFFFF` | 1.000 / 0.000 / 90 | 1.0:1 | **DOC** White |
| neutral-50 | `#F7F6FA` | 0.975 / 0.005 / 298 | 1.08:1 | generated |
| neutral-100 | `#EDEAF3` | 0.942 / 0.012 / 301 | 1.19:1 | **DOC** Light Grey |
| neutral-200 | `#DCD9E2` | 0.890 / 0.013 / 301 | 1.39:1 | generated |
| neutral-300 | `#BFBCC7` | 0.801 / 0.016 / 298 | 1.87:1 | generated |
| neutral-400 | `#9D99A6` | 0.690 / 0.019 / 300 | 2.78:1 | generated |
| neutral-500 | `#827D8D` | 0.599 / 0.025 / 300 | 3.99:1 | generated |
| neutral-600 | `#6B6677` | 0.521 / 0.027 / 299 | 5.54:1 | generated |
| neutral-700 | `#4D485A` | 0.414 / 0.030 / 298 | 8.79:1 | **DOC** Dark Grey |
| neutral-800 | `#322C40` | 0.308 / 0.036 / 298 | 13.38:1 | generated |
| neutral-900 | `#1B132A` | 0.210 / 0.045 / 298 | 17.9:1 | generated |
| neutral-950 | `#050011` | 0.097 / 0.052 / 298 | 20.7:1 | **DOC** Black |

## 4. Semantic
Every semantic ramp uses the same steps:
- **50**: banner and background tint.
- **100–200**: borders and chips.
- **500**: the doc's base colour, used for icons, charts and illustrations, not text.
- **600**: solid fills with white text (all ≥ 4.5:1).
- **700**: text and foreground (all ≥ 6:1 on white and on their 50 tint).
- **900**: the doc's dark value.

### Success
| Step | Hex | OKLCH L / C / H | vs white | Source |
|---|---|---|---|---|
| success-50 | `#F2FFF3` | 0.987 / 0.021 / 148 | 1.03:1 | **DOC** Success 10 |
| success-100 | `#E3F7E4` | 0.956 / 0.033 / 147 | 1.12:1 | generated |
| success-200 | `#C3EAC5` | 0.899 / 0.064 / 146 | 1.32:1 | generated |
| success-300 | `#91D994` | 0.820 / 0.120 / 145 | 1.67:1 | generated |
| success-500 | `#0FB21D` | 0.663 / 0.217 / 143 | 2.84:1 | **DOC** Success base |
| success-600 | `#008816` | 0.544 / 0.178 / 144 | 4.63:1 | generated |
| success-700 | `#006C12` | 0.461 / 0.150 / 144 | 6.66:1 | generated |
| success-900 | `#125C19` | 0.416 / 0.122 / 144 | 8.17:1 | **DOC** Success 100 |

### Error
| Step | Hex | OKLCH L / C / H | vs white | Source |
|---|---|---|---|---|
| error-50 | `#FFF8F8` | 0.985 / 0.007 / 17 | 1.05:1 | generated |
| error-100 | `#FFEBEB` | 0.956 / 0.022 / 18 | 1.15:1 | **DOC** Error 10 |
| error-200 | `#FFD1D0` | 0.900 / 0.052 / 20 | 1.37:1 | generated |
| error-300 | `#FFAAA7` | 0.820 / 0.101 / 22 | 1.82:1 | generated |
| error-500 | `#C71010` | 0.526 / 0.209 / 28 | 5.98:1 | **DOC** Error base |
| error-600 | `#B40706` | 0.486 / 0.196 / 29 | 7.06:1 | generated |
| error-700 | `#970400` | 0.426 / 0.173 / 30 | 9.0:1 | generated |
| error-900 | `#5C1B12` | 0.325 / 0.097 / 31 | 12.96:1 | **DOC** Error 100 |

### Warning
| Step | Hex | OKLCH L / C / H | vs white | Source |
|---|---|---|---|---|
| warning-50 | `#FFF8F2` | 0.983 / 0.011 / 63 | 1.05:1 | **DOC** Warning 10 |
| warning-100 | `#FDEDDF` | 0.955 / 0.025 / 64 | 1.14:1 | generated |
| warning-200 | `#F8D7BD` | 0.900 / 0.051 / 60 | 1.36:1 | generated |
| warning-300 | `#F3B589` | 0.820 / 0.093 / 56 | 1.78:1 | generated |
| warning-500 | `#DC680F` | 0.647 / 0.168 / 49 | 3.48:1 | **DOC** Warning base |
| warning-600 | `#BD5900` | 0.578 / 0.151 / 51 | 4.57:1 | generated |
| warning-700 | `#964700` | 0.490 / 0.126 / 52 | 6.57:1 | generated |
| warning-900 | `#5C3212` | 0.364 / 0.075 / 55 | 10.94:1 | **DOC** Warning 100 |

### Info
| Step | Hex | OKLCH L / C / H | vs white | Source |
|---|---|---|---|---|
| info-50 | `#F2FDFF` | 0.986 / 0.012 / 210 | 1.04:1 | **DOC** Info 10 |
| info-100 | `#E3F4F7` | 0.955 / 0.018 / 209 | 1.13:1 | generated |
| info-200 | `#C4E5EC` | 0.900 / 0.036 / 212 | 1.33:1 | generated |
| info-300 | `#93CFDF` | 0.819 / 0.065 / 216 | 1.72:1 | generated |
| info-500 | `#0BA2C4` | 0.659 / 0.119 / 220 | 3.01:1 | **DOC** Info base |
| info-600 | `#00809A` | 0.554 / 0.100 / 219 | 4.61:1 | generated |
| info-700 | `#00667A` | 0.471 / 0.084 / 217 | 6.6:1 | generated |
| info-900 | `#124E5C` | 0.394 / 0.063 / 217 | 9.25:1 | **DOC** Info 100 |


## 5. Role tokens
Components should use these, never raw ramp steps.

| Role | Ramp step | Hex |
|---|---|---|
| `--fk-bg` | neutral-0 | `#FFFFFF` |
| `--fk-bg-subtle` | neutral-50 | `#F7F6FA` |
| `--fk-surface` | neutral-0 | `#FFFFFF` |
| `--fk-surface-raised` | primary-50 | `#F7F5FD` |
| `--fk-surface-tint` | primary-100 | `#EBE6F7` |
| `--fk-surface-inverse` | primary-950 | `#130438` |
| `--fk-border` | neutral-200 | `#DCD9E2` |
| `--fk-border-strong` | neutral-300 | `#BFBCC7` |
| `--fk-border-focus` | lavender-500 | `#996DF8` |
| `--fk-text-primary` | neutral-900 | `#1B132A` |
| `--fk-text-secondary` | neutral-700 | `#4D485A` |
| `--fk-text-muted` | neutral-600 | `#6B6677` |
| `--fk-text-disabled` | neutral-400 | `#9D99A6` |
| `--fk-text-heading` | primary-800 | `#2D0B84` |
| `--fk-text-link` | primary-700 | `#4A13B7` |
| `--fk-text-on-primary` | neutral-0 | `#FFFFFF` |
| `--fk-text-on-accent` | primary-950 | `#130438` |
| `--fk-text-on-inverse` | neutral-0 | `#FFFFFF` |
| `--fk-primary` | primary-700 | `#4A13B7` |
| `--fk-primary-hover` | primary-800 | `#2D0B84` |
| `--fk-primary-pressed` | primary-900 | `#21025E` |
| `--fk-primary-subtle` | primary-100 | `#EBE6F7` |
| `--fk-focus-ring` | lavender-500 | `#996DF8` |
| `--fk-accent` | lime-100 | `#EFFF94` |
| `--fk-accent-hover` | lime-200 | `#EAF17D` |
| `--fk-accent-strong` | lime-400 | `#DAD05A` |
| `--fk-accent-2` | lavender-400 | `#B294FF` |
| `--fk-accent-2-subtle` | lavender-100 | `#EEE9FF` |
| `--fk-disabled-bg` | neutral-100 | `#EDEAF3` |
| `--fk-disabled-fg` | neutral-500 | `#827D8D` |
| `--fk-success-fg` | success-700 | `#006C12` |
| `--fk-success-bg` | success-50 | `#F2FFF3` |
| `--fk-success-border` | success-200 | `#C3EAC5` |
| `--fk-success-solid` | success-600 | `#008816` |
| `--fk-success-icon` | success-600 | `#008816` |
| `--fk-success-strong` | success-900 | `#125C19` |
| `--fk-error-fg` | error-700 | `#970400` |
| `--fk-error-bg` | error-50 | `#FFF8F8` |
| `--fk-error-border` | error-200 | `#FFD1D0` |
| `--fk-error-solid` | error-600 | `#B40706` |
| `--fk-error-icon` | error-600 | `#B40706` |
| `--fk-error-strong` | error-900 | `#5C1B12` |
| `--fk-warning-fg` | warning-700 | `#964700` |
| `--fk-warning-bg` | warning-50 | `#FFF8F2` |
| `--fk-warning-border` | warning-200 | `#F8D7BD` |
| `--fk-warning-solid` | warning-600 | `#BD5900` |
| `--fk-warning-icon` | warning-600 | `#BD5900` |
| `--fk-warning-strong` | warning-900 | `#5C3212` |
| `--fk-info-fg` | info-700 | `#00667A` |
| `--fk-info-bg` | info-50 | `#F2FDFF` |
| `--fk-info-border` | info-200 | `#C4E5EC` |
| `--fk-info-solid` | info-600 | `#00809A` |
| `--fk-info-icon` | info-600 | `#00809A` |
| `--fk-info-strong` | info-900 | `#124E5C` |

### How this maps to the current landing tokens
| Landing token (v1) | Was | Now | Change |
|---|---|---|---|
| `--fk-heading` | #2D0B84 | primary-800 #2D0B84 | none |
| `--fk-primary` (button) | #4A13B7 | primary-700 #4A13B7 | **Stays.** It fits the ramp exactly at 700, so it's now part of the system and not a one-off. |
| `--fk-primary-hover` | #3A0E94 | primary-800 #2D0B84 | hover goes to the brand Main colour |
| `--fk-primary-pressed` | #2E0B78 | primary-900 #21025E | pressed is one step darker |
| `--fk-ink` | #21123F | neutral-900 #1B132A | very close, now on the neutral ramp |
| `--fk-body` | #4B4560 | neutral-700 #4D485A (doc Dark Grey) | visually the same, now a doc colour |
| `--fk-muted` | #6B6585 | neutral-600 #6B6677 | 5.5:1, same role |
| `--fk-focus` | #8B5CF6 | lavender-500 #996DF8 | 3.6:1 on white (passes 3:1), on the lavender ramp |
| `--fk-dark` | #25056D | primary-950 #130438 (doc Primary 100) | dark bands use the doc's darkest purple |
| `--fk-lav-50…300` | ad-hoc tints | primary-50, lavender-100/200/300 | on the ramps |

The legacy names are aliased at the bottom of `tokens.css`, so the current landing page keeps working without changes.

## 6. Changes from the doc, and why
1. **Primary ramp put in order.** The doc's "75" #3D2184 is lighter than Main (OKLCH L 0.35 vs 0.31), so the ramp went dark, lighter, darker. I removed it. "25" #AC9FCC was much greyer than its neighbours (chroma 0.07), so it's replaced by primary-300/400. Main, 10 and 100 are kept exactly as 800, 100 and 950. The ramp now has 11 even steps (50–950).
2. **Main purple is step 800, not 500.** #2D0B84 is very dark (L 0.31, 14:1 on white). It's great for headings but too heavy to be the only action colour. The current button #4A13B7 sits exactly at 700, and the stray doc text colour #7543C7 sits at 600, so both are now part of the ramp.
3. **The two "Accent 1" colours merged.** Lime #EFFF94 and Yellow #DAD05A were both called Accent 1 and are only 11° apart in hue, which reads as a mistake when they're side by side. Yellow is now **lime-400**, a deeper step of the same family, used for lime borders, hover and illustration shading. Neither works as text on white (1.1:1 and 1.6:1), so lime is fill only, with primary-950 text on it (17.6:1).
4. **Grey is purple-tinted and kept off text.** The doc's Grey #9B9B9D was the only colour with no tint, and it fails as text (2.77:1). It's replaced by neutral-400 #9D99A6 (same lightness, tinted), which is for icons, placeholders and disabled states only. The lightest allowed text is neutral-600 #6B6677 (5.5:1).
5. **Accessible semantic text colours added.** The doc's base colours for success #0FB21D (2.84:1), warning #DC680F (3.48:1) and info #0BA2C4 (3.01:1) all fail as text on white. Each family now has a **600** step for solid fills with white text (≥ 4.6:1) and a **700** step for text (≥ 6.2:1 on its tint): success-700 #006C12, warning-700 #964700, info-700 #00667A, error-700 #970400. Error's base #C71010 already passes (5.98:1), but text still uses error-700 so all four behave the same way.
6. **Error tint moved.** The doc's Error 10 #FFEBEB is noticeably darker than the other three tints (L 0.96 vs about 0.985), so an error banner would look heavier than the others. It's now error-100, and a lighter error-50 #FFF8F8 is the banner background, matching the other three.

## 7. Usage rules
- **Text on white or light tints:** use neutral-600 or darker, or primary-600 or darker. Never use 400–500 steps, lime, lavender-400 or a doc semantic base for text.
- **Headings:** primary-800 only. **Body text:** neutral-700. **Strong UI text:** neutral-900.
- **There's one primary action per view:** primary-700 at rest, 800 on hover, 900 when pressed. The focus ring is a 3px lavender-500 ring with a 3px white gap.
- **Lime is for highlights only:** badges, one accent button on dark bands, illustration. Text on lime is always primary-950, never white (1.08:1).
- **Lavender** is for soft surfaces (100), avatars and illustration (400), and the focus ring (500). Don't use it as a second button colour, because it competes with the primary.
- **Status colours:** use the -bg, -border and -fg roles for banners and chips, and -solid only for filled buttons or icons. Never rely on colour alone: always pair it with an icon and a label.
- **Dark sections:** primary-950 background with white text (19:1). Use primary-200 for secondary text on dark.
- Use role tokens in components. Raw ramp steps are only for illustrations and charts.

## 8. Contrast summary (WCAG 2.2)
See `05-roles-contrast@2x.png`. Every role used for text passes AA, and most pass AAA. These pairings fail, and aren't allowed for text:
- Doc Grey #9B9B9D on white: 2.77:1.
- neutral-400 on white: 2.78:1 (disabled only).
- success-500 on white: 2.84:1.
- info-500 on white: 3.01:1.
- warning-500 on white: 3.48:1.
- White on lime-100: 1.08:1.

## 9. Open decisions for the founder
1. Are the doc's hex values final, or were they sampled from an image as the note says? If there's a master brand file, those values should replace the anchors.
2. Should the primary button stay **#4A13B7** (primary-700, brighter, 10.2:1), or should buttons use the brand Main **#2D0B84** (primary-800)? I recommend 700 for buttons and 800 for headings and hover, which is what the current landing page already does.
3. Is it OK to fold the Yellow #DAD05A into lime as lime-400? The alternative is keeping it as a separate third accent, which I don't recommend.
4. Is it OK to drop doc "75" #3D2184 and "25" #AC9FCC?
5. Is lime-100 OK as the accent button on dark bands, for example "Send invite"? On white backgrounds, lime only works with a lime-400 border.
