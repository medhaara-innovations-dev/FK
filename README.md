# FK

FamilyKit is a private, AI-assisted family life management platform from Medhaara Innovations Private Limited.

Product direction, founder approvals, and the pending-approval register live in [`PROJECT_CONTEXT.md`](./PROJECT_CONTEXT.md). Architecture and Cursor rules live in [`.cursor/`](./.cursor/).

This repository is one Next.js application at the repository root. The current application is the FamilyKit marketing landing page. It does not include a backend, Supabase, or the authenticated app shell.

## Marketing site

Next.js (App Router, TypeScript) and Tailwind CSS, with the approved navbar and landing sections.

### Stack

- Next.js (App Router) + React + TypeScript
- Tailwind CSS v4, with FamilyKit brand tokens as CSS variables
- Self-hosted Poppins (headings, buttons, nav) and Mulish (body) via `next/font/local`
- Outlined Lucide icons (`lucide-react`)
- Founder logo (horizontal, on light), favicons, and app icons from the founder logo pack

### Run locally

```bash
npm ci
npm run dev
```

Then open [http://localhost:3000](http://localhost:3000).

```bash
npm run lint
npx tsc --noEmit
npm run build
npm start
```

### What’s in this build

- Desktop and mobile navbar
- Primary button is **Get Early Access**; there is no Pricing link
- Sections for why FamilyKit, how it works, uses, security, and early access
- Security copy is limited to the approved promise: “Your family's data stays in India.” The site does not claim end-to-end encryption or zero-knowledge.
