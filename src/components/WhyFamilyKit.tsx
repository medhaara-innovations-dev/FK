import Image from "next/image";
import { revealIndex } from "@/lib/motion";
import {
  CalendarClock,
  Files,
  FolderSearch,
  LayoutGrid,
  LifeBuoy,
  Users,
  type LucideIcon,
} from "lucide-react";

const ART_ALT =
  "Illustration of an Indian family at home, each searching in a different place: the father digs through a drawer of papers, the mother checks messages on her phone and the daughter looks through a folder, while loose papers, an email and a calendar with a circled date float around them.";

/* The founder's wording, word for word (why-spec v5). */
const PROBLEMS: { icon: LucideIcon; title: string }[] = [
  { icon: Files, title: "Documents scattered everywhere" },
  { icon: CalendarClock, title: "Important dates are easily forgotten" },
  { icon: FolderSearch, title: "Nobody knows where everything is" },
  { icon: Users, title: "Family responsibilities become difficult to manage" },
  { icon: LayoutGrid, title: "Too many apps, no single picture" },
  { icon: LifeBuoy, title: "What happens during an emergency?" },
];

/* Why FamilyKit (#why) · why-spec v5: problems, not features. Static rows; v6: bridge line removed, closing banner added.
   v18: below 1280 the copy wrapper dissolves (display:contents) so the order is head → art → rows → banner. */
export function WhyFamilyKit() {
  return (
    <section id="why" className="why" aria-labelledby="why-title">
      <div className="why__inner">
        <figure className="why__art" data-reveal="art">
          <div className="why__panel">
            <Image
              src="/images/why-illustration.webp"
              width={864}
              height={1152}
              alt={ART_ALT}
              loading="lazy"
              decoding="async"
              sizes="(min-width:1280px) 580px, (min-width:768px) 760px, 100vw"
            />
          </div>
        </figure>

        <div className="why__copy">
          <div className="why__head">
          <p className="why__eyebrow" data-reveal="" style={revealIndex(0)}>Why FamilyKit</p>
          <h2
            className="why__title"
            id="why-title"
            data-reveal=""
            style={revealIndex(1)}
          >
            <span className="why__line">
              Your family&apos;s life is connected.
            </span>{" "}
            <span className="why__line">
              But its{" "}
              <span className="why__mark">information is scattered.</span>
            </span>
          </h2>
          <p className="why__lede" data-reveal="" style={revealIndex(2)}>
            Important family information is spread across phones, WhatsApp
            messages, emails, paper files, different apps and people&apos;s
            memories. Finding the right information at the right time becomes
            difficult.
          </p>
          </div>
          <ul className="why__list" data-reveal="group">
            {PROBLEMS.map(({ icon: Icon, title }, i) => (
              <li
                className="prob"
                key={title}
                data-reveal-item=""
                style={revealIndex(i)}
              >
                <span className="prob__ic">
                  <Icon size={22} strokeWidth={1.75} aria-hidden="true" />
                </span>
                <h3 className="prob__title">{title}</h3>
              </li>
            ))}
          </ul>
        </div>
        <div className="why__banner" data-reveal="">
          <span className="why__banner-ic" aria-hidden="true">
            <Users size={28} strokeWidth={1.75} />
          </span>
          <span className="why__banner-rule" aria-hidden="true" />
          <div className="why__banner-copy">
            <p className="why__banner-title">
              Your family shouldn&apos;t have to search everywhere for what
              matters.
            </p>
            <p className="why__banner-text">
              It&apos;s time to bring your family&apos;s scattered information
              and everyday responsibilities together.
            </p>
          </div>
        </div>
      </div>
    </section>
  );
}
