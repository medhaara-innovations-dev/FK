# FamilyKit design documents

These are the design documents made by Rachana, the UI/UX designer. The founder has agreed the words, colours, and rules in them. Use them as written. If something is not covered, or you want to change it, ask the founder first.

## Where to look

**Brand rules.** Start with [brand/FamilyKit-Brand-Foundation-v1.pdf](brand/FamilyKit-Brand-Foundation-v1.pdf). The Word file next to it is the same guide. It covers who FamilyKit is for, the promise, key messages, tone of voice, colours, type, the logo, visual style, and the trust lines in section 09.

**Colours and tokens.** [palette/PALETTE.md](palette/PALETTE.md) explains the colour ramps. Use [palette/tokens.css](palette/tokens.css) and [palette/palette.json](palette/palette.json) for the values in code. `familykit-brand.css`, `familykit-colours.css`, and `familykit-typography.css` are the stylesheets. The PDF and Word files in that folder are the colour and type guides, and the PNG sheets are the visual reference. The small Python files there only rebuild those sheets. They are not brand rules.

**Logo files.** [logo/README.md](logo/README.md) is the index. This folder is the founder's official logo. The older redrawn logos are rejected and must never be used. Full-colour files are in `logo/png/`, one-colour vectors in `logo/svg/`, app icons and favicons in `logo/png/app-icon/` and `logo/png/favicon/`, and the review sheets in `logo/review/`.

**Approved navbar.** [website/navbar-mockup/](website/navbar-mockup/) is Rachana's approved navbar reference: plain HTML, CSS, and JS, with self-hosted Poppins and Mulish fonts and the logo. Open `index.html`. The desktop and mobile review sheets are in [website/review/](website/review/).

## Founder decisions for the website

These settle two open questions in Brand Foundation section 10:

- The main button label is **Get Early Access**.
- There is no pricing section, and no Pricing link, on the website for now.

The navbar mockup still has a Pricing link and an empty pricing placeholder from an earlier draft. Do not build those. The font for amount columns is still open (Brand Foundation section 10).

## Trust wording

Never claim end-to-end encryption or zero-knowledge.

Use these six lines from Brand Foundation section 09, exactly as written. Do not shorten, combine, or add to them.

1. Protected by AES-256, the same encryption banks use.
2. Your family's data stays in India.
3. Our AI never uses your documents to train.
4. AI suggests, you confirm. Nothing is saved without you.
5. Only the people you choose can see your documents.
6. We never sell or share your family's information.
