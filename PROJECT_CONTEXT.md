# FamilyKit Project Context

**Status:** The empty Next.js foundation and approved folders exist locally. Product behavior has not been built. No feature build starts until the founder explicitly says "start".  
**Version:** 1.2 · 8 November 2026 (v1.1 and v1.0 earlier)  
**Owner:** Medhaara Innovations Private Limited

This file summarizes the product and the current decision status for people building FamilyKit. It follows the reference documents already in this repository. It does not replace them.

The approved development direction is recorded below. A later, separate approval created the empty Next.js foundation and the approved folders (on the founder's local machine; not yet pushed to the `Dev_FK` branch). That approval does not cover database schemas, migrations, or product behavior.

| Reference | Role |
|---|---|
| `.cursor/architecture/FAMILYKIT_MASTER_ARCHITECTURE.md` | Readable architecture reference. Product direction is confirmed. Its approved development direction matches this file. |
| `.cursor/rules/familykit-core.mdc` | Always-on project rules for Cursor. |
| `.cursor/rules/FAMILYKIT_PROJECT_RULES.md` | Operational rules. |
| `PROJECT_CONTEXT.md` | Record of founder approvals and the Pending Approval register. |

Labels:

- **Confirmed** — settled in the product and architecture references.
- **Approved development direction** — approved for how FamilyKit will be built. This does not approve coding, schemas, providers, pricing, or deployment configuration.
- **Pending Approval** — still open. Cursor must not decide it.

## Changelog

### v1.2 · 8 November 2026

- Added **Bill Payments & Account Aggregator** capability as a key differentiator (V1.5): BBPS bill payments and recharges, FASTag, insurance premiums, utility renewals, and Account Aggregator data via an RBI-licensed partner. Provider is Pending Approval (Setu candidate; Decentro, Cashfree alternatives).
- Added the **Pre-build checklist**.

### v1.1 · 8 November 2026 (founder decisions)

- **Ownership model:** any member can create a family space. The person who uploads a record owns it and can grant or revoke access to any family member at any time. Replaces the earlier "Family Head manages access" model. The family creator manages membership and subscription only, not other members' records.
- **India-only data residency:** Supabase Mumbai (`ap-south-1`), Vercel functions in `bom1` (Mumbai), backups and logs in India. Any processor outside India (OpenAI, OCR) is Pending Approval; no raw document data leaves India without founder approval.
- **Encryption:** AES-256 at rest plus app-level AES-256-GCM envelope encryption for documents and sensitive fields; keys outside the database; TLS 1.2+.
- **India DPDP Act 2023:** consent, purpose limitation, data-principal rights, breach notification, retention, grievance officer. Legal review still required.
- **Authentication:** Google sign-in, or user ID and password, plus an app PIN. MFA-ready.
- **Added:** audit log for every grant, revoke, view, and download; optional expiring shares; RLS on every table; synthetic data only. Owner-leaves and deceased-owner succession is Pending Approval.
- **Build gate:** the Next.js foundation exists locally; stale "do not initialize Next.js" wording updated. No feature build until the founder says "start".
- Fixed text encoding (UTF-8).

## Product

FamilyKit is a private, AI-assisted family life management platform. It brings important people, documents, records, reminders, household information, and everyday utilities into one trusted family space.

It is not only a document store. It helps a family organize, understand, and manage information and everyday responsibilities.

Positioning:

- One Platform for Your Entire Family Life.
- Everything in Place.
- FamilyKit should organize the family, not make the family organize FamilyKit.

Confirmed product principles:

- Organize the family and avoid unnecessary data entry.
- One unified assistant connects authorized information across the product.
- Build for the full long-term vision, and release in controlled phases.
- FamilyKit organizes information. It does not directly sell insurance, investments, loans, or other financial products. It does not add stock-market features or commission-driven product recommendations.
- Personal and shared information may coexist. Privacy and permissions apply at family level and at individual-record level.
- Keep the product simple, useful, trustworthy, accessible, and affordable for ordinary families.
- Commercial relationships must be disclosed. Users control whether their information is shared with external partners. Do not claim a partnership or integration exists until it is formally established.

The confirmed document journey is one sequence, stated in two short forms:

- Scan → AI Organizes → Verify → Confirm.
- Upload → AI suggests → authorized user verifies → save and remind.

The detailed confirmed workflow is:

Upload → encrypted private storage (India) → OCR and type detection → field extraction → suggested owner, category, and links → authorized review and correction → verified record, source link, and reminders.

Extracted information starts as unverified. It becomes authoritative only after an authorized person confirms it. The original document and the extraction history stay available.

## Seven product systems

These seven systems are approved. One unified FamilyKit AI layer serves all of them. The assistant is not a separate product system and not a set of separate assistants.

| System | Place in the roadmap |
|---|---|
| Family Management | V1. Family space, members, relationships, family tree, and record-level access control. |
| Document Management | V1. Identity, certificates, property, vehicle, and education records. Upload, search, and review. |
| Finance & Insurance Management | V1 basic. Reference records, policies, premiums, deposits, investments, and linked documents. |
| Calendar, Reminders & Family Responsibilities | V1. Important dates, renewals, family tasks, and alerts. |
| Household Management | V1.5. Appliances, warranties, bills, expenses, and inventory. |
| Family Utilities | V1.5. Grocery lists, emergency contacts, and private or shared notes. |
| Bill Payments & Account Aggregator (within Finance & Insurance) | V1.5. **Key differentiator.** BBPS bill payments, recharges, FASTag, premiums, renewals; consented Account Aggregator data. |
| External Service Ecosystem | V2 and later. Travel, restaurants, entertainment, health, and local services. |

The architecture also names platform responsibilities that support these systems: notifications, subscription, and integrations. Those are part of the layered architecture. They are not extra product systems.

Roadmap milestones are scope, not promised dates:

| Phase | Outcome |
|---|---|
| V1.0 | Authenticated family spaces, owner-controlled permissions, family data, encrypted private documents, reviewable document intelligence, basic finance and insurance records, calendar and reminders, source-grounded AI. |
| V1.5 | Bill payments and Account Aggregator (key differentiator), household records, warranties, bills, expenses, grocery lists, shared tasks, and utilities. |
| V2.0 | Carefully selected external services. |
| V3.0 | Proactive intelligence, deeper automation, and advanced integrations. |

Build one module at a time, in this order (each only after the founder says "start"):

1. Project foundation and security.
2. Authentication and family creation.
3. Family members and permissions.
4. Document upload and AI processing.
5. Unified FamilyKit AI.
6. Family information and asset management.
7. Reminders and calendar.
8. Household management and everyday utilities.
9. External service integrations.

## Layered architecture

```text
People and experience
  Responsive web / PWA, dashboard, family, documents, AI, reminders
FamilyKit application
  Validation, workflows, APIs, server-side authorization
Core modules
  Family, Documents, Finance/Insurance, Household, Calendar/Tasks,
  Utilities, Notifications, Subscription, Integrations
Intelligence
  OCR/extraction, authorized search/retrieval, unified AI
Trusted data foundation (India region only)
  Identity, permissions, encryption, PostgreSQL records, private files, audit, background jobs
External services, only with consent and approved integrations
  Payments, email, WhatsApp, travel, health, shopping, bookings
```

Confirmed boundary: browsers and AI do not receive unrestricted access to family data. Controlled backend services check permission first.

The architecture diagram originally listed jobs beside intelligence. The approved folder layout places shared background jobs in the platform layer, because reminders, notifications, documents, and AI all need the same execution path. AI-specific extraction, retrieval, and the assistant stay in intelligence.

Approved development direction: one modular monolith, with a responsive web application and PWA first. Modules keep clear boundaries inside that application. Microservices, AWS, Redis, and Kubernetes are not the starting point. Add a separate service only when scale, reliability, or compliance shows a need, and only after explicit approval.

## Data principles

Confirmed:

- A family space is the primary boundary for isolation. Inside a family, the **record owner** (the person who uploaded or created it) is the boundary for access.
- Every account belongs to at least one identifiable family space. Any member can create a family space.
- A person, asset, document, record, and reminder can be connected. Each connection is explicit and permission-checked.
- Structured facts stay separate from original files. Facts need a source and a verification status.
- Private source files stay private and encrypted. Do not store private documents in public file locations.
- Preserve history: original file, extraction output, changes, verification result, and every access or permission event.

Approved development direction, through Supabase:

- PostgreSQL for structured data.
- Supabase private storage for PDFs, scans, and images.
- One database at the start, with clear table and domain boundaries.
- Row-level security enabled on **every** table, with no exceptions.

Intended domains, with the detailed schema still **Pending Approval**: identity, families and members, record ownership and access grants, documents, assets, finance and insurance, household, calendar and tasks, AI jobs, conversations and source references, consent, subscriptions, integrations, and audit.

## Data residency (India only)

Confirmed founder decision, 8 November 2026:

- Database, storage, and auth: Supabase project in **Mumbai (`ap-south-1`)**.
- Server functions: Vercel region **`bom1` (Mumbai)**.
- Backups, logs, and monitoring data stay in India.
- Any third-party processor outside India (for example OpenAI or an OCR provider) is **Pending Approval**. No raw document data or unmasked sensitive fields are sent outside India without explicit founder approval. Prefer minimized or masked data, or India-hosted options.

## Encryption

Confirmed founder decision, 8 November 2026:

- AES-256 encryption at rest for the database and storage (Supabase default).
- Application-level **AES-256-GCM envelope encryption** for uploaded documents and sensitive fields (Aadhaar, PAN, policy numbers, account numbers, and similar).
- Encryption keys are kept outside the database (a key management service or vault). The key provider is **Pending Approval**.
- TLS 1.2 or higher for all traffic.

## Security and permissions

Confirmed path:

Sign in → identify the user → check family membership → check the record owner's grant → allow only the minimum data or action → audit the event.

Confirmed rules:

- Any member can create a family space and invite members.
- The family creator manages membership and subscription only. The creator has no automatic access to other members' records.
- The person who uploads or creates a record is its **owner**. The owner can grant or revoke access to any family member at any time. Revocation takes effect immediately.
- Optional expiring shares: an owner may grant access that ends on a set date.
- Support different family-member relationships.
- Access is both role-based and record-level. Private, shared, and sensitive individual records need record-level checks.
- A family member must never access another family's private information.
- External-person documents are handled separately, with their own privacy controls.
- Shared documents follow the owner's grants.
- Audit log every grant, revoke, view, and download.
- Hiding something in the interface does not secure it. The server and the data layer enforce access.
- Use short-lived file links only after authorization.
- Store secrets only on server-side infrastructure. Never expose service-role keys, API secrets, encryption keys, or private credentials in frontend code or Git.
- Keep development, staging, and production separate.
- Use synthetic data only in development. Do not use real customer documents or production family data for development.
- Test that one family cannot access another family, and that a restricted record stays restricted inside a family.
- Production release, production data changes, and destructive database changes require explicit owner approval. Do not silently auto-release.

Authentication (confirmed):

- Google sign-in (OAuth), or user ID and password.
- Plus an app PIN for unlocking the app.
- MFA-ready design. The MFA method is **Pending Approval**.

Recommended safeguards:

- Server-side validation, audit logs, automated backups in India, and restore testing.
- An independent security review before public launch.

Supabase row-level security on every table, together with server checks, enforces family isolation and record ownership. The policies are not written. The exact roles and fine-grained sharing matrix are **Pending Approval**. What happens when an owner leaves the family or passes away (succession and nominee access) is **Pending Approval**. The principles above are confirmed.

## Privacy and DPDP compliance

FamilyKit must follow the India Digital Personal Data Protection Act, 2023:

- Clear consent before collecting personal data, with the purpose stated.
- Purpose limitation: use data only for the purpose consented to.
- Users can access, correct, delete, and export their data.
- Breach notification to affected users and the Data Protection Board as the Act requires.
- Defined retention periods; delete data when the purpose ends or consent is withdrawn.
- A named grievance officer and contact.

Specialist legal review is still required (**Pending Approval**).

## Bill Payments & Account Aggregator

Bill Payments & Account Aggregator (**key differentiator**, V1.5). Families pay many mobiles, DTH, FASTag, insurance premiums and utilities across separate company apps; FamilyKit lets them do it from one place.

- **Bill payments via BBPS** (Bharat Bill Payment System) through an RBI-licensed partner: bill payments, mobile/DTH recharges, FASTag, insurance premiums, utility renewals.
- **Account Aggregator** (RBI AA framework, Sahamati ecosystem): FamilyKit acts as a Financial Information User (FIU) through a partner, for consented financial data (deposits, policies, investments) only.
- FamilyKit **never holds funds** and **never stores card or UPI data**. Payment instruments stay with the licensed partner.
- Every payment needs a per-payment PIN/OTP confirmation. Consent is explicit, purpose-bound, time-limited, and revocable at any time.
- India data residency applies to partner data and FamilyKit records.
- Audit log every payment attempt, success, failure, consent grant, and consent revoke.
- Reminders link to renewal and due dates in Documents and Finance & Insurance records.
- Provider choice is **Pending Approval**: Setu is the candidate; alternatives Decentro and Cashfree. Licences, partner agreements, and legal review are required before build.

## Unified AI

FamilyKit has one assistant. It answers from information in the signed-in user's FamilyKit account, and only from information that user is allowed to access.

Confirmed behavior:

Question → permission check → retrieve authorized, relevant records → answer only from retrieved sources → show the source and any uncertainty.

Confirmed AI rules:

- AI never has unrestricted database access.
- Permission checking happens before retrieval, not after the answer is generated.
- AI suggestions stay unverified until an authorized person confirms them.
- Do not guess missing facts. Say when information is absent, unavailable, or unverified.
- Ground factual answers in FamilyKit records or documents and link the source where possible.
- Document text and AI output are untrusted. They cannot change access rights or override system instructions.
- Send an external AI provider only the minimum information needed for that task, masked where possible, and only within the data-residency rule above.
- Keep personal-record questions, live external discovery, and bookings or payments separate.
- Ask before sharing data, booking, paying, or taking any other consequential external action.
- Examples of questions the assistant should be able to answer from authorized records: find a health insurance policy, when vehicle insurance is due, a refrigerator warranty period, property documents, and important family expenses due this month.

OpenAI is the approved development direction for the assistant API, but sending data to it outside India is **Pending Approval**. OCR provider, region, and provider retention terms are **Pending Approval**. The behavior rules above stay in force either way.

## Integrations and consent

FamilyKit owns the family experience, identity, permissions, and information structure. Specialist providers deliver specialist services.

Confirmed:

- Every provider receives only the data needed for a user-approved action.
- Booking, payment, sharing, or sending messages to others needs the appropriate user confirmation.

Pending Approval:

- Which providers to support first, whether their APIs allow the use case, and what consent wording is required.
- Payment gateway. Razorpay is a candidate only.
- Messaging provider. Email plus an approved WhatsApp provider is the direction. The provider is not selected.

## Approved development direction

Approved on 7 November 2026 as the initial way to build FamilyKit, updated 8 November 2026. This is not permission to start feature coding.

| Area | Direction |
|---|---|
| Product scope | Seven product systems and one unified AI layer |
| Application | Next.js and TypeScript |
| Interface | Tailwind CSS. Responsive web application and PWA first |
| Data, authentication, private storage | Supabase (Mumbai, `ap-south-1`): PostgreSQL, Supabase Auth, private storage |
| Authentication | Google OAuth, or user ID and password, plus app PIN. MFA-ready |
| Encryption | AES-256 at rest plus app-level AES-256-GCM envelope encryption; TLS 1.2+ |
| AI | OpenAI API, with authorization-aware retrieval (cross-border data flow Pending Approval) |
| Deployment target | Vercel, functions in `bom1` (Mumbai) |
| Source control | Private GitHub (`medhaara-innovations-dev/FK`, branch `Dev_FK`) |
| Application shape | Modular monolith |
| Environments | Separate development, staging, and production |
| Folder layout | The tree in this file. Each business module uses `src/modules/<name>/components/`, `src/modules/<name>/services/`, `src/modules/<name>/types/`, `src/modules/<name>/validation/`, and `src/modules/<name>/tests/` |
| Background work | Shared jobs in `src/platform/jobs/`: browser-independent execution, safe retries, and failure handling |

Still required with that direction:

- Long-running work must continue after the person closes the browser and must be safe to retry. This includes large file processing, OCR, extraction, reminders, and notifications.
- Job state must stay clear: pending, processing, complete, failed, retry.
- The queue or worker product is **Pending Approval**.
- Vercel, Supabase, and GitHub project configuration are **Pending Approval**, except the India regions above.
- Typed, simple, maintainable code with clear module boundaries.
- Validate inputs on the server, including document extraction and AI output.
- Show errors and loading states. Support mobile and desktop. Follow accessibility practices.
- Avoid unnecessary dependencies and premature optimization.
- Do not rewrite working modules or delete existing behavior without approval.

## Repository

What exists now is the empty Next.js application at the repository root, the approved folders below, and these foundation documents, on the founder's local machine. The local shell is not yet pushed to GitHub `Dev_FK`. No environment files, database schema, or product behavior have been created.

### Approved folder structure

This layout is created. It is one Next.js application at the repository root, with module boundaries inside it. It is not a multi-application repository, and it is not a set of separately deployed services.

Routes and modules are different. A route is the user-facing page. A module holds the business behavior. `src/app/(app)/finance/` is the Finance & Insurance screen. `src/modules/finance-insurance/` is the business module behind that screen. The same split applies to the other systems: the route stays short and user-facing, and the module keeps the domain name.

```text
FamilyKit/
├── PROJECT_CONTEXT.md
├── .cursor/
│   ├── architecture/
│   └── rules/
├── public/
├── src/
│   ├── app/
│   │   ├── (public)/
│   │   ├── (app)/
│   │   │   ├── family/
│   │   │   ├── documents/
│   │   │   ├── finance/
│   │   │   ├── household/
│   │   │   ├── calendar/
│   │   │   ├── utilities/
│   │   │   └── assistant/
│   │   └── api/
│   ├── modules/
│   │   ├── family/
│   │   ├── documents/
│   │   ├── finance-insurance/
│   │   ├── household/
│   │   ├── calendar/
│   │   ├── utilities/
│   │   ├── notifications/
│   │   ├── subscription/
│   │   └── integrations/
│   ├── intelligence/
│   │   ├── extraction/
│   │   ├── retrieval/
│   │   └── assistant/
│   ├── platform/
│   │   ├── auth/
│   │   ├── permissions/
│   │   ├── audit/
│   │   ├── storage/
│   │   ├── config/
│   │   └── jobs/
│   ├── components/
│   └── lib/
├── supabase/
└── tests/
    └── security/
```

`public/` holds static files, including later PWA assets. `src/app/` holds thin routes and layouts. `src/app/api/` holds thin handlers, and the business rules stay in the modules. `src/intelligence/extraction/` covers OCR, type detection, and field extraction. `src/intelligence/retrieval/` is authorized search. `src/intelligence/assistant/` is the one FamilyKit assistant. `src/platform/storage/` is encrypted private files and short-lived links. `src/platform/config/` selects the active environment and stores no secrets. `src/platform/jobs/` is shared background work for every system. `src/components/` is the shared interface. `src/lib/` holds shared helpers. `supabase/` is reserved for the local Supabase project. `tests/security/` holds cross-family, record-ownership, and revocation checks.

Each business module keeps its own components, services, types, validation, and tests. Those inner folders now exist and contain no business behavior. Shared interface pieces that truly belong to more than one module stay in `src/components`. Cross-family and record-level security checks stay in `tests/security`.

`src/modules/<name>/services/` executes securely on the server. It contains server-side business workflows, authorization, and data access. Browser-side code must not import it, call it directly, or receive its private operations. A browser may call an approved route or server entry point. That entry point calls the service only after authorization.

```text
src/modules/<name>/
├── components/
├── services/
├── types/
├── validation/
└── tests/
```

How this matches the architecture:

| Architecture layer | Folder |
|---|---|
| People and experience | `src/app/`, `src/modules/<name>/components/`, `src/components/`, `public/` |
| FamilyKit application | `src/app/api/`, `src/modules/<name>/services/`, `src/modules/<name>/validation/` |
| Core modules | `src/modules/<name>/` |
| Intelligence | `src/intelligence/extraction/`, `src/intelligence/retrieval/`, `src/intelligence/assistant/` |
| Trusted data foundation and shared jobs | `src/platform/`, including `src/platform/jobs/`, and `supabase/` |
| External services | `src/modules/integrations/` |

Route and module names:

| User-facing route | Business module |
|---|---|
| `src/app/(app)/family/` | `src/modules/family/` |
| `src/app/(app)/documents/` | `src/modules/documents/` |
| `src/app/(app)/finance/` | `src/modules/finance-insurance/` |
| `src/app/(app)/household/` | `src/modules/household/` |
| `src/app/(app)/calendar/` | `src/modules/calendar/` |
| `src/app/(app)/utilities/` | `src/modules/utilities/` |
| `src/app/(app)/assistant/` | `src/intelligence/assistant/` |

`notifications`, `subscription`, and `integrations` are platform and ecosystem modules. They do not have approved user-facing routes yet.

Background work:

- Shared job execution lives in `src/platform/jobs/`, because documents, reminders, notifications, and AI all use it.
- A job starts in the module that owns the work, then is recorded by `src/platform/jobs/`.
- The worker entry does not live under `src/app`, so closing the browser does not own the work.
- Every job keeps a state: pending, processing, complete, failed, or retry.
- Failed work must be safe to run again.
- The queue or worker product is **Pending Approval**. No worker tool is chosen by this folder.

Environments:

- Development, staging, and production stay separate, all in India regions.
- Secrets stay in each environment's own configuration, not in Git.
- No environment files are created at this step.
- Deployment configuration is **Pending Approval**, except the India regions.

`supabase/` is only a reserved place. No schema, policies, or migrations are included. The database schema and permission matrix remain **Pending Approval**.

## Pre-build checklist

All must be complete, with founder sign-off, before the founder says "start" for a feature that depends on them.

1. **Legal and licences:** company legal review; confirm FamilyKit needs no own RBI licence when using a licensed BBPS / AA partner; partner agreements signed; terms of service and privacy policy drafted.
2. **DPDP Act 2023:** consent notices and flows, purpose register, data-principal rights process (access, correction, deletion, export), breach response plan, retention schedule, grievance officer named.
3. **Vendor residency and DPAs:** written confirmation of India data residency and a signed data processing agreement from every vendor (Supabase, Vercel, AI/OCR, payment/AA partner, messaging).
4. **Final decisions:** close the Pending Approval items needed for the next module (sharing matrix, schema, key provider, MFA, succession, providers) and provide the UX screens.
5. **Environments:** separate development and production Supabase projects in Mumbai (`ap-south-1`), plus staging when approved; no production data in development.

## Decision protection

Cursor (and any other coding agent) must follow these rules for every **Pending Approval** item:

- Never independently decide a Pending Approval item.
- When a decision is needed, present the options and explain the trade-offs.
- Wait for explicit founder approval before implementing that decision.
- The Next.js foundation and approved folders already exist. Do not re-initialize or restructure them.
- Never interpret architectural approval as permission to install packages, create new folders, create database schemas or migrations, or write application code.
- **Build gate:** no feature build, Supabase project change, or coding-agent run starts until the founder explicitly says "start".

## Decisions still requiring approval

These remain **Pending Approval**. The approved development direction above does not decide them.

| Decision | Current position |
|---|---|
| OCR provider, region, and retention terms | Not selected. Must respect India-only residency. |
| Cross-border AI processing (OpenAI) | OpenAI is the assistant API direction. Sending data outside India needs founder approval; prefer masked data or India-hosted options. |
| Encryption key provider (KMS / vault) | Not selected. Keys must stay outside the database. |
| MFA method | Design is MFA-ready. Method not chosen. |
| Owner leaves / deceased owner succession | Not decided (nominee or successor access). |
| Payment gateway | Razorpay is a candidate only. |
| BBPS / Account Aggregator partner | Setu is the candidate; Decentro and Cashfree are alternatives. Licences and legal review required. |
| Messaging provider | Email and WhatsApp provider are not selected. |
| Roles and fine-grained sharing matrix | Ownership principles are confirmed. The matrix is not finalized. |
| Detailed database schema | Not designed. |
| Subscription plans, limits, and pricing | Draft ideas only. |
| Which external partners launch first | Undecided. |
| Legal, privacy, and DPDP compliance | Specialist review still required. |
| Deployment configuration | Separate environments and India regions are approved. Vercel project settings, domains, and promotion flow are not. |
| Background-job product | Browser-independent execution, safe retries, and failure handling are approved. The tool is not selected. |
| UX screens | Not yet provided by the founder. |
| Product behavior | The empty Next.js foundation and approved folders exist. Business workflows and product screens are not built. |

The next step waits for the founder's "start".
