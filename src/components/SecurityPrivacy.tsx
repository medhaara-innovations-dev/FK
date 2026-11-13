import Image from "next/image";
import {
  Ban,
  ChevronRight,
  Lock,
  MapPin,
  Shield,
  ShieldCheck,
  type LucideIcon,
} from "lucide-react";
import { revealIndex } from "@/lib/motion";

const ART_ALT =
  "Illustration of an Indian family standing calmly beside a large purple shield with a lock, with their document folders stacked safely at its base.";

/* Lucide has no "sparkles-off": the site's AI sparkle with a diagonal slash (security-spec v2, §7). */
function SparklesOff(props: { size?: number; strokeWidth?: number }) {
  const { size = 22, strokeWidth = 1.75 } = props;
  return (
    <svg
      viewBox="0 0 24 24"
      width={size}
      height={size}
      fill="none"
      stroke="currentColor"
      strokeWidth={strokeWidth}
      strokeLinecap="round"
      strokeLinejoin="round"
      aria-hidden="true"
    >
      <path d="M9.937 15.5A2 2 0 0 0 8.5 14.063l-6.135-1.582a.5.5 0 0 1 0-.962L8.5 9.936A2 2 0 0 0 9.937 8.5l1.582-6.135a.5.5 0 0 1 .963 0L14.063 8.5A2 2 0 0 0 15.5 9.937l6.135 1.581a.5.5 0 0 1 0 .964L15.5 14.063a2 2 0 0 0-1.437 1.437l-1.582 6.135a.5.5 0 0 1-.963 0z" />
      <path d="M20 3v4" />
      <path d="M22 5h-4" />
      <path d="M2 2 22 22" />
    </svg>
  );
}

/* Founder-approved promises (security-spec v2). Only AES-256 bank-level encryption and data kept in India:
   never end-to-end or zero-knowledge. */
const PROMISES: {
  icon: LucideIcon | typeof SparklesOff;
  title: string;
  body: string;
}[] = [
  {
    icon: Lock,
    title: "Bank-level AES-256 encryption",
    body: "Your family's documents and records are encrypted at rest and in transit.",
  },
  {
    icon: MapPin,
    title: "Your data stays in India",
    body: "Stored strictly on secure servers in India and never moved outside.",
  },
  {
    icon: Ban,
    title: "We never sell your data",
    body: "Your information is never sold or shared with advertisers or third parties.",
  },
  {
    icon: SparklesOff,
    title: "Your data is never used to train AI",
    body: "AI processes your files only to assist you, never to train general models.",
  },
];

/* Security & Privacy (#security) · security-spec v2. Copy first in the DOM; desktop places the art right via grid areas.
   v18: below 1280 the copy wrapper dissolves (display:contents) so the order is head → art → promises → banner.
   The only control is the Privacy Policy pill. */
export function SecurityPrivacy() {
  return (
    <section id="security" className="security" aria-labelledby="security-title">
      <div className="security__inner">
        <div className="security__copy">
          <div className="security__head">
          <p className="security__eyebrow" data-reveal="" style={revealIndex(0)}>
            <Shield size={16} strokeWidth={1.75} aria-hidden="true" />
            Security &amp; Privacy
          </p>
          <h2
            className="security__title"
            id="security-title"
            data-reveal=""
            style={revealIndex(1)}
          >
            <span className="security__line">
              Your family&apos;s data stays safe.
            </span>{" "}
            <span className="security__line">
              <span className="security__mark">And stays yours.</span>
            </span>
          </h2>
          </div>
          <ul className="security__list" data-reveal="group">
            {PROMISES.map(({ icon: Icon, title, body }, i) => (
              <li
                className="promise"
                key={title}
                data-reveal-item=""
                style={revealIndex(i)}
              >
                <span className="promise__ic">
                  <Icon size={22} strokeWidth={1.75} aria-hidden="true" />
                </span>
                <div className="promise__copy">
                  <h3 className="promise__title">{title}</h3>
                  <p className="promise__body">{body}</p>
                </div>
              </li>
            ))}
          </ul>
        </div>

        <figure className="security__art" data-reveal="art">
          <div className="security__panel">
            <Image
              src="/images/security-illustration.webp"
              width={864}
              height={1152}
              alt={ART_ALT}
              loading="lazy"
              decoding="async"
              sizes="(min-width:1280px) 520px, (min-width:768px) 760px, 100vw"
            />
          </div>
        </figure>

        <aside
          className="security__banner"
          aria-label="Privacy commitment"
          data-reveal=""
        >
          <span className="security__banner-ic" aria-hidden="true">
            <ShieldCheck size={28} strokeWidth={1.75} />
          </span>
          <span className="security__banner-rule" aria-hidden="true" />
          <div className="security__banner-copy">
            <p className="security__banner-title">
              Your privacy is our commitment
            </p>
            <p className="security__banner-text">
              FamilyKit is built to keep your family&apos;s information safe and
              private.
            </p>
          </div>
          {/* /privacy-policy does not exist yet in this build (placeholder link until the policy page is written). */}
          <a className="security__banner-btn" href="/privacy-policy">
            Read Our Privacy Policy
            <ChevronRight size={16} strokeWidth={2} aria-hidden="true" />
          </a>
        </aside>
      </div>
    </section>
  );
}
