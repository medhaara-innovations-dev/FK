import Image from "next/image";
import { Calendar, ShieldCheck, Sparkles } from "lucide-react";
import { EarlyAccessForm } from "@/components/EarlyAccessForm";
import { revealIndex } from "@/lib/motion";

const PHOTO_ALT =
  "An Indian family — a mother in a cream saree, a father in a purple shirt, a teenage daughter in a lilac top and a young son in a mint tee — smiling together as they look at a smartphone.";

/* Final CTA (#early-access) · cta-footer-spec v3 (approved). Copy + form first in the DOM, photo second.
   Stacked below 1280; 1280+ copy left / photo right. The photo fades to pure alpha at the bottom. */
export function EarlyAccess() {
  return (
    <section id="early-access" className="cta" aria-labelledby="cta-title">
      <div className="cta__inner">
        <div className="cta__copy">
          <p className="cta__eyebrow" data-reveal="" style={revealIndex(0)}>
            <Sparkles size={16} strokeWidth={1.75} aria-hidden="true" />
            Early Access
          </p>
          <h2
            className="cta__title"
            id="cta-title"
            data-reveal=""
            style={revealIndex(1)}
          >
            <span className="cta__line">Ready to put</span>{" "}
            <span className="cta__line">
              <span className="cta__mark">everything in place?</span>
            </span>
          </h2>
          <p className="cta__lede" data-reveal="" style={revealIndex(2)}>
            Join Indian families organizing documents, dates, and
            responsibilities in one calm, private space.
          </p>
          <EarlyAccessForm />
        </div>

        <figure className="cta__visual" data-reveal="art">
          <div className="cta__photo">
            <Image
              src="/images/cta-family.webp"
              width={1152}
              height={864}
              alt={PHOTO_ALT}
              loading="lazy"
              decoding="async"
              sizes="(min-width:1280px) 560px, (min-width:1024px) 760px, (min-width:768px) 688px, 100vw"
            />
            <span className="cta__badge cta__badge--shield" aria-hidden="true">
              <ShieldCheck size={20} strokeWidth={1.75} />
            </span>
            <span className="cta__badge cta__badge--cal" aria-hidden="true">
              <Calendar size={20} strokeWidth={1.75} />
            </span>
          </div>
        </figure>
      </div>
    </section>
  );
}
