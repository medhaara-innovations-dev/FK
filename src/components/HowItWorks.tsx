import Image from "next/image";
import { revealIndex } from "@/lib/motion";
import {
  ArrowRight,
  Camera,
  CircleCheck,
  Layers,
  ListChecks,
  Sparkles,
  type LucideIcon,
} from "lucide-react";

const ART_ALT =
  "Illustration of an Indian family at home: the father holds up a phone showing a scanned document with a check mark, the mother looks on beside him and their daughter stands close, with the original document on the table.";

/* Founder's wording (how-spec v3, Option A). */
const STEPS: { icon: LucideIcon; num: string; title: string; body: string }[] = [
  {
    icon: Camera,
    num: "Step 01",
    title: "Scan or Upload",
    body: "Upload documents, bills, policies, certificates and other family information.",
  },
  {
    icon: Sparkles,
    num: "Step 02",
    title: "AI Understands",
    body: "AI reads it, identifies the type, extracts the details and links it to the right family member.",
  },
  {
    icon: CircleCheck,
    num: "Step 03",
    title: "Review & Verify",
    body: "Check the extracted details against the original, and correct anything that needs attention.",
  },
  {
    icon: Layers,
    num: "Step 04",
    title: "Organized & Ready",
    body: "Confirmed information is organised for authorised family members, with reminders where they apply.",
  },
];

const FLOW: { icon: LucideIcon; label: string }[] = [
  { icon: Camera, label: "Scan" },
  { icon: Sparkles, label: "AI Organizes" },
  { icon: CircleCheck, label: "Verify" },
  { icon: Layers, label: "Confirm" },
];

/* How it works (#how-it-works) · how-spec v3, Option A. Static: nothing here is clickable.
   v18: below 1280 the copy wrapper dissolves (display:contents) so the order is head → art → steps → banner. */
export function HowItWorks() {
  return (
    <section id="how-it-works" className="how" aria-labelledby="how-title">
      <div className="how__inner">
        <figure className="how__art" data-reveal="art">
          <div className="how__panel">
            <Image
              src="/images/how-illustration.webp"
              width={864}
              height={1152}
              alt={ART_ALT}
              loading="lazy"
              decoding="async"
              sizes="(min-width:1280px) 580px, (min-width:768px) 760px, 100vw"
            />
          </div>
        </figure>

        <div className="how__copy">
          <div className="how__head">
          <p className="how__eyebrow" data-reveal="" style={revealIndex(0)}>How It Works</p>
          <h2
            className="how__title"
            id="how-title"
            data-reveal=""
            style={revealIndex(1)}
          >
            <span className="how__line">Simple for Your Family.</span>{" "}
            <span className="how__line">
              <span className="how__mark">Smart with AI.</span>
            </span>
          </h2>
          <p className="how__lede" data-reveal="" style={revealIndex(2)}>
            Four simple steps, from paper to perfectly organised.
          </p>
          </div>

          <ol className="how__grid" aria-label="Four steps" data-reveal="group">
            {STEPS.map(({ icon: Icon, num, title, body }, i) => (
              <li
                className="step"
                key={num}
                data-reveal-item=""
                style={revealIndex(i)}
              >
                <div className="step__head">
                  <span className="step__ic">
                    <Icon size={22} strokeWidth={1.75} aria-hidden="true" />
                  </span>
                  <span className="step__num">{num}</span>
                </div>
                <h3 className="step__title">{title}</h3>
                <p className="step__body">{body}</p>
              </li>
            ))}
          </ol>
        </div>

        <aside
          className="how__banner"
          aria-label="How FamilyKit helps"
          data-reveal=""
        >
          <span className="how__banner-ic" aria-hidden="true">
            <ListChecks size={28} strokeWidth={1.75} />
          </span>
          <span className="how__banner-rule" aria-hidden="true" />
          <div className="how__banner-copy">
            <ol className="how__flow">
              {FLOW.map(({ icon: Icon, label }, i) => (
                <li key={label} style={revealIndex(i)}>
                  <span className="how__pill">
                    <Icon strokeWidth={1.75} aria-hidden="true" />
                    {label}
                  </span>
                  {i < FLOW.length - 1 && (
                    <ArrowRight
                      className="how__arrow"
                      strokeWidth={2.25}
                      aria-hidden="true"
                    />
                  )}
                </li>
              ))}
            </ol>
            <p className="how__banner-text">
              Your family does not have to organize everything manually.
              FamilyKit helps do the work.
            </p>
          </div>
        </aside>
      </div>
    </section>
  );
}
