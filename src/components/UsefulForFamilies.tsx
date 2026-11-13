import Image from "next/image";
import {
  ChevronRight,
  GraduationCap,
  HeartHandshake,
  HeartPulse,
  House,
  Plane,
  type LucideIcon,
} from "lucide-react";
import { revealIndex } from "@/lib/motion";

const ART_ALT =
  "Illustration of an Indian family of three generations at home, with icons above them for school records, health, home papers and travel documents, each marked safely kept.";

const USES: { icon: LucideIcon; title: string; body: string }[] = [
  {
    icon: GraduationCap,
    title: "Parents & Kids",
    body: "School records, birth certificates, vaccinations, and IDs.",
  },
  {
    icon: HeartPulse,
    title: "Senior Parents",
    body: "Medical reports, prescriptions, pensions, and health policies.",
  },
  {
    icon: House,
    title: "Home & Vehicles",
    body: "Property papers, utility bills, RC books, and insurance renewals.",
  },
  {
    icon: Plane,
    title: "Trips & Milestones",
    body: "Passports, visas, bookings, and private family memories.",
  },
];

/* Useful for Families (#uses) · uses-spec v1 + founder's left illustration (v14).
   From 1280 the art sits left via grid areas. v18: below 1280 the copy wrapper dissolves (display:contents)
   so the order is header → art → cards → banner, like Why, How and Security. Cards are static.
   v19: Option 1 closing banner (uses-spec v2), its pill links to #security. */
export function UsefulForFamilies() {
  return (
    <section id="uses" className="uses" aria-labelledby="uses-title">
      <div className="uses__inner">
        <div className="uses__copy">
          <header className="uses__header">
            <p className="uses__eyebrow" data-reveal="" style={revealIndex(0)}>
              <HeartHandshake size={16} strokeWidth={1.75} aria-hidden="true" />
              Useful for Families
            </p>
            <h2
              className="uses__title"
              id="uses-title"
              data-reveal=""
              style={revealIndex(1)}
            >
              <span className="uses__line">Made for every family.</span>{" "}
              <span className="uses__line">
                <span className="uses__mark">Ready for everyday life.</span>
              </span>
            </h2>
          </header>

          <ul
            className="uses__grid"
            aria-label="Who FamilyKit is useful for"
            data-reveal="group"
          >
            {USES.map(({ icon: Icon, title, body }, i) => (
              <li
                className="use-card"
                key={title}
                data-reveal-item=""
                style={revealIndex(i)}
              >
                <span className="use-card__ic" aria-hidden="true">
                  <Icon size={22} strokeWidth={1.75} aria-hidden="true" />
                </span>
                <h3 className="use-card__title">{title}</h3>
                <p className="use-card__body">{body}</p>
              </li>
            ))}
          </ul>
        </div>

        <figure className="uses__art" data-reveal="art">
          <div className="uses__panel">
            <Image
              src="/images/uses-illustration.webp"
              width={864}
              height={1152}
              alt={ART_ALT}
              loading="lazy"
              decoding="async"
              sizes="(min-width:1280px) 520px, (min-width:1024px) 760px, (min-width:768px) 688px, 100vw"
            />
          </div>
        </figure>
        {/* v2 Option 1 closing banner (uses-spec v2): same component as security__banner; the pill hands off to #security. */}
        <aside
          className="uses__banner"
          aria-label="Shared family space"
          data-reveal=""
        >
          <span className="uses__banner-ic" aria-hidden="true">
            <HeartHandshake size={28} strokeWidth={1.75} />
          </span>
          <span className="uses__banner-rule" aria-hidden="true" />
          <div className="uses__banner-copy">
            <p className="uses__banner-title">
              One shared space for every generation.
            </p>
            <p className="uses__banner-text">
              From school records to senior care, everything stays ready for the
              family members who need it.
            </p>
          </div>
          <a className="uses__banner-btn" href="#security">
            See how it&apos;s protected
            <ChevronRight size={16} strokeWidth={2} aria-hidden="true" />
          </a>
        </aside>
      </div>
    </section>
  );
}
