# FamilyKit Master Architecture

**Purpose:** the readable, authoritative reference for FamilyKit and Cursor.  
**Status:** Product direction confirmed. Approved development direction recorded on 7 November 2026 and updated on 8 November 2026. Unresolved choices are marked Pending Approval. The empty Next.js foundation and approved folders exist locally. Architectural approval is not permission to install packages, create new folders, create schemas, or write application code. No feature build starts until the founder says "start".  
**Version:** 1.2 · 8 November 2026

## 1. FamilyKit in one sentence

FamilyKit is a private, AI-assisted family life management platform: it brings important people, documents, records, reminders, household information and everyday utilities into one trusted family space.

### Confirmed product principles

- Organize the family; do not make the family do unnecessary data entry.
- Core document journey: **Upload → AI suggests → authorized user verifies → save and remind**.
- One unified assistant connects authorized information across the product.
- Build for the full long-term vision, but release in controlled phases.
- FamilyKit organizes information; it does **not** directly sell insurance, investments, loans, or other financial products.
- Personal and shared information may coexist; privacy and permissions apply at family and individual-record level.

## 2. The layered architecture

```text
┌──────────────────────────────────────────────────────────────────────────┐
│ PEOPLE & EXPERIENCE                                                      │
│ Responsive web / PWA · dashboard · family · documents · AI · reminders   │
├──────────────────────────────────────────────────────────────────────────┤
│ FAMILYKIT APPLICATION                                                    │
│ Validation · workflows · APIs · server-side authorization                │
├──────────────────────────────────────────────────────────────────────────┤
│ CORE MODULES                                                             │
│ Family | Documents | Finance/Insurance | Household | Calendar/Tasks      │
│ Utilities | Notifications | Subscription | Integrations                  │
├──────────────────────────────────────────────────────────────────────────┤
│ INTELLIGENCE                                                             │
│ OCR/extraction · authorized search/retrieval · unified AI                │
├──────────────────────────────────────────────────────────────────────────┤
│ TRUSTED DATA FOUNDATION (India region only)                              │
│ Identity · permissions · encryption · records · private files · audit    │
├──────────────────────────────────────────────────────────────────────────┤
│ EXTERNAL SERVICES (only with consent and approved integrations)          │
│ payments · email · WhatsApp · travel · health · shopping · bookings      │
└──────────────────────────────────────────────────────────────────────────┘
```

**Boundary rule (Confirmed):** browsers and AI do not receive unrestricted access to family data. Controlled backend services check permission first.

### Approved application shape

One modular monolith, delivered as a responsive web application and PWA first. Shared background jobs live in `src/platform/jobs/`, because documents, reminders, notifications, and AI use the same execution path. Job state is pending, processing, complete, failed, or retry. The worker does not live under the browser route. The queue or worker product is Pending Approval.

Each business module uses:

```text
src/modules/<name>/
├── components/
├── services/
├── types/
├── validation/
└── tests/
```

`src/modules/<name>/services/` executes securely on the server. It contains server-side business workflows, authorization, and data access. Browser-side code must not import it, call it directly, or receive its private operations.

`src/app/(app)/finance/` is the user-facing route. `src/modules/finance-insurance/` is the business module. The same split applies to the other systems: the route stays short, and the module keeps the domain name.

The same document journey is also stated as Scan → AI Organizes → Verify → Confirm. Unified AI is one assistant layer across the seven product systems. It is in the V1 scope. It is not an eighth product system.

## 3. Product modules

| Module | What it covers | Delivery |
|---|---|---|
| Family | family space, members, relationships, family tree, record-level access control | V1 |
| Documents | identity, certificates, property, vehicle, education; upload, search, review | V1 |
| Finance & insurance | reference records, policies, premiums, deposits, investments, linked documents | V1 basic |
| Calendar & reminders | important dates, renewals, family tasks and alerts | V1 |
| Unified AI | authorized questions, source-grounded answers, document intelligence | V1 |
| Bill payments & Account Aggregator | **key differentiator**: BBPS bills, recharges, FASTag, premiums, renewals; consented AA data via licensed partner | V1.5 |
| Household | appliances, warranties, bills, expenses, inventory | V1.5 |
| Utilities | grocery lists, emergency contacts, private/shared notes | V1.5 |
| Service ecosystem | travel, restaurants, entertainment, health, local services | V2+ |

## 4. Data and database principles

### Confirmed

- A **family space** is the primary boundary for isolation. Inside it, the **record owner** (uploader or creator) controls access.
- Any member can create a family space.
- A person, asset, document, record and reminder can be connected, but each connection is explicit and permission-checked.
- Keep structured facts separate from original files. Facts need source and verification status.
- Keep private source files private and encrypted; do not store private documents in public file locations.
- Preserve history: original file, extraction output, changes, verification result, and every access/permission event.

### Approved development direction

- Supabase PostgreSQL for structured data, in Mumbai (`ap-south-1`).
- Supabase private storage for PDFs, scans, and images, in Mumbai.
- One database at the start, with clear table and domain boundaries.
- Row-level security on **every** table, together with server checks. The policies are not written.
- Add a separately deployed service only when scale, reliability, or compliance proves a need, and only after explicit founder approval.

### Data residency (Confirmed, 8 November 2026)

- Supabase `ap-south-1` (Mumbai); Vercel functions `bom1` (Mumbai); backups, logs, and monitoring in India.
- Any processor outside India (OpenAI, OCR) is Pending Approval. No raw document data leaves India without founder approval. Prefer minimized or masked data, or India-hosted options.

### Encryption (Confirmed, 8 November 2026)

- AES-256 at rest for database and storage (Supabase default).
- App-level AES-256-GCM envelope encryption for documents and sensitive fields (Aadhaar, PAN, policy and account numbers).
- Keys outside the database (KMS or vault; provider Pending Approval). TLS 1.2+ in transit.

### Pending Approval

The detailed schema for these intended domains: identity, families and members, record ownership and access grants, documents, assets, finance and insurance, household, calendar and tasks, AI conversations and source references, consent, subscriptions, integrations, and audit.

## 5. Security and permissions

```text
Sign in → identify user → check family membership → check record owner's grant
        → allow only the minimum required data/action → audit the event
```

### Confirmed rules

- Any member can create a family space. The creator manages membership and subscription only, not other members' records.
- The uploader of a record is its owner and can grant or revoke access to any family member at any time; revocation is immediate.
- Optional expiring shares are supported.
- Access is not only role-based: private, shared and sensitive individual records need record-level checks.
- Audit log every grant, revoke, view, and download.
- A user interface that hides something does not secure it; the server and data layer enforce access.
- Use short-lived file links only after authorization.
- Store secrets and encryption keys only on server-side infrastructure.
- Test that one family cannot access another family, that a restricted record remains restricted within a family, and that revoked access stops immediately.
- Maintain separate development, staging and production environments; use synthetic data only in development.

### Authentication (Confirmed)

- Google OAuth, or user ID and password, plus an app PIN. MFA-ready; the MFA method is Pending Approval.

### Privacy and DPDP Act 2023

- Consent before collection, purpose limitation, access/correction/deletion/export, breach notification, defined retention, and a grievance officer. Specialist legal review is Pending Approval.

### Pending Approval

- Owner leaves the family or passes away: succession and nominee access.
- Roles and fine-grained sharing matrix.

### Recommended safeguards

- Server-side validation, audit logs, automated backups in India, and restore testing.
- Independent security review before public launch.

## 6. Unified AI behavior

FamilyKit has **one assistant**, not separate assistants for documents, insurance and household matters.

```text
Question → permission check → retrieve authorized, relevant records
         → answer only from retrieved sources → show source / uncertainty
```

### Confirmed AI rules

- AI never has unrestricted database access.
- Permission checking happens before retrieval, not after generation.
- Do not guess missing facts; say when information is absent or unverified.
- Ground factual answers in FamilyKit records/documents and link the source where possible.
- Document text and AI output are untrusted; AI cannot change access rights.
- Send the minimum, masked information needed for each AI task to an external provider, and only within the India residency rule.

## 7. Document workflow

```text
Upload → encrypted private storage (India) → OCR/type detection → field extraction
       → suggested owner/category/links → authorized review & correction
       → verified record + source link + reminders
```

**Confirmed:** the uploader owns the document. Extracted information starts as *unverified*. It becomes authoritative only after an authorized user confirms it. The original document and extraction history remain available for traceability.

## 8. Integrations and consent

FamilyKit owns the family experience, identity, permissions and information structure. Specialist providers deliver specialist services.

### Confirmed

- Every provider receives only the data needed for a user-approved action.
- Booking, payment, sharing, or sending messages to others needs appropriate user confirmation.
- Never claim a partnership or integration exists until formally established.

### Open decisions

- Which providers to support first, whether their APIs permit the use case, and what consent wording is required.
- Payment gateway and messaging provider selection.

## 8a. Bill Payments & Account Aggregator

```text
Reminder (due/renewal date) → user opens bill → fetch via BBPS partner → confirm with PIN/OTP
       → partner processes payment (FamilyKit holds no funds, no card/UPI data) → receipt + audit log
```

Bill Payments & Account Aggregator (**key differentiator**, V1.5). Families pay many mobiles, DTH, FASTag, insurance premiums and utilities across separate company apps; FamilyKit lets them do it from one place.

- **Bill payments via BBPS** (Bharat Bill Payment System) through an RBI-licensed partner: bill payments, mobile/DTH recharges, FASTag, insurance premiums, utility renewals.
- **Account Aggregator** (RBI AA framework, Sahamati ecosystem): FamilyKit acts as a Financial Information User (FIU) through a partner, for consented financial data (deposits, policies, investments) only.
- FamilyKit **never holds funds** and **never stores card or UPI data**. Payment instruments stay with the licensed partner.
- Every payment needs a per-payment PIN/OTP confirmation. Consent is explicit, purpose-bound, time-limited, and revocable at any time.
- India data residency applies to partner data and FamilyKit records.
- Audit log every payment attempt, success, failure, consent grant, and consent revoke.
- Reminders link to renewal and due dates in Documents and Finance & Insurance records.
- Provider choice is **Pending Approval**: Setu is the candidate; alternatives Decentro and Cashfree. Licences, partner agreements, and legal review are required before build.

## 9. Deployment and environments

```text
Development (synthetic data, localhost) → automated checks → Staging → approval → Production
```

### Confirmed

- Development, staging and production are separate, all in India regions.
- Test on localhost first; push to Vercel only when a feature is final.
- Production release requires owner approval; never silently auto-release.
- Long-running work—large file processing, OCR, extraction, reminders, notifications—must survive a user closing the browser and be retried safely.

### Approved development direction

- Shared job execution lives in `src/platform/jobs/`.
- Long-running work must survive the browser closing and must be safe to retry.
- Job state remains pending, processing, complete, failed, or retry.

### Pending Approval

The managed queue or worker product, selected only after reliability, cost, retry behavior, India hosting, and hosting limits are reviewed and the founder approves it.

## 10. Technology direction

| Area | Direction | Status |
|---|---|---|
| App | Next.js and TypeScript | Approved development direction. Foundation exists locally. |
| UI | Tailwind CSS. Responsive web application and PWA first | Approved development direction |
| Data, authentication, private storage | Supabase PostgreSQL, Supabase Auth, private storage in Mumbai (`ap-south-1`) | Approved development direction |
| Authentication | Google OAuth, or user ID and password, plus app PIN; MFA-ready | Confirmed. MFA method Pending Approval. |
| Encryption | AES-256 at rest + app-level AES-256-GCM envelope encryption; TLS 1.2+ | Confirmed. Key provider Pending Approval. |
| AI | OpenAI API with authorization-aware retrieval | Approved development direction. Cross-border data flow Pending Approval. Behavior rules are confirmed. |
| Deployment target | Vercel, functions in `bom1` (Mumbai) | Approved development direction |
| Source control | Private GitHub | Approved development direction |
| Application shape | Modular monolith | Approved development direction |
| Environments | Separate development, staging, and production | Approved development direction |
| Payments | Razorpay | Pending Approval. Candidate only. |
| Notifications | Email and an approved WhatsApp provider | Pending Approval. Provider not selected. |
| Bill payments / AA partner | Setu (candidate); Decentro, Cashfree alternatives | Pending Approval. Licences and legal review required. |
| Background-job product | A managed queue or worker | Pending Approval. The behavior and `src/platform/jobs/` location are approved. |

Approved development direction is not permission to install packages, create new folders, create schemas or migrations, or write application code. The Next.js foundation already exists; do not re-initialize it. Avoid AWS, Redis, Kubernetes, and separately deployed services until a measured need is approved.

## 11. Phased roadmap

| Phase | Outcome |
|---|---|
| V1.0 | authenticated family spaces, owner-controlled permissions, family data, encrypted private documents, reviewable document intelligence, basic finance/insurance records, calendar/reminders, source-grounded AI |
| V1.5 | bill payments and Account Aggregator (key differentiator), household records, warranties, bills, expenses, grocery lists, shared tasks, utilities |
| V2.0 | carefully selected external services: travel, restaurants, entertainment, health, local/lifestyle services |
| V3.0 | proactive intelligence, deeper automation and advanced integrations |

These are scope milestones, not promised release dates.

## 12. Decisions needing approval

| Decision | Current position | Why approval is needed |
|---|---|---|
| OCR provider, region, and retention terms | Not selected. Must respect India residency. | Privacy, quality, and compliance |
| Cross-border AI processing | OpenAI is the assistant direction; data outside India needs approval | Data residency and DPDP |
| Encryption key provider | Not selected; keys outside the database | Security and operations |
| MFA method | Design is MFA-ready | Security and usability |
| Owner leaves / deceased succession | Not decided | Family privacy and legal implications |
| Payment gateway | Razorpay is only a candidate | Commercial and operational impact |
| BBPS / AA partner | Setu candidate; Decentro, Cashfree alternatives | RBI licensing, compliance, cost |
| Messaging provider | Email and WhatsApp provider are not selected | Template, cost, and consent constraints |
| Roles and fine-grained sharing matrix | Ownership principles confirmed. The matrix is not finalized. | Defines the family privacy experience |
| Detailed database schema | Not designed | The domains are known. The tables are not. |
| Subscription plans, limits, pricing | Draft ideas only | Commercial validation required |
| Which external partners launch first | Undecided | API access, economics, and support vary |
| Legal, privacy, and DPDP compliance | Require specialist review | Sensitive personal and financial data |
| Deployment configuration | Separate environments and India regions are approved. Project settings, domains, and promotion are not. | Operational impact |
| Background-job product | Behavior and `src/platform/jobs/` are approved. The tool is not selected. | Reliability, cost, and hosting limits |
| UX screens | Not yet provided | Defines the product experience |
| Product behavior | The empty Next.js foundation and approved folders exist. Business workflows are not built. | Build starts only when the founder says "start" |

Before build, complete the Pre-build checklist in `PROJECT_CONTEXT.md` (legal/licences, DPDP, vendor residency and DPAs, final decisions, separate dev/prod Supabase in Mumbai).

## 13. Cursor build rules (short form)

1. Treat Confirmed, Approved development direction, and Pending Approval as binding.
2. No feature build, Supabase change, or coding-agent run until the founder says "start".
3. Never independently decide a Pending Approval item. Present the options and trade-offs, then wait for explicit founder approval.
4. Never interpret architectural approval as permission to install packages, create new folders, create schemas or migrations, or write application code. Do not re-initialize the existing Next.js foundation.
5. Build modules with clear boundaries inside one application. `services/` means the server-side module folder, not a separately deployed service.
6. RLS on every table. Enforce family isolation and record ownership in the server and data layer, not only in the interface.
7. Keep all data in India; encrypt documents and sensitive fields with AES-256-GCM; keep keys outside the database.
8. Keep files private, and verify access before issuing temporary links. Audit every grant, revoke, view, and download.
9. Validate all inputs, including document extraction and AI output.
10. Preserve verification status and source traceability for extracted facts.
11. AI answers must be authorized, grounded, and explicit about uncertainty.
12. Use synthetic data only outside production, and require approval for production deploys.

The operational rules are `.cursor/rules/FAMILYKIT_PROJECT_RULES.md`. The approval record is `PROJECT_CONTEXT.md`.
