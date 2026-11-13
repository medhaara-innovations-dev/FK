import { ArrowUp, ChevronRight, Sparkles } from "lucide-react";

/* Ask AI block inside the hero phone (hero-spec v3).
   NOT yet confirmed by the founder, so it is isolated here and switched by SHOW_ASK_AI in Hero.tsx.
   Sample illustration data only. The input pill is hidden below 768px (hero.css .ai__input). */
export const ASK_AI_ALT =
  " Ask AI: when does Papa's health policy renew? AI answers 15 January 2027.";

export function PhoneAskAI() {
  return (
    <>
      <p className="app__h app__h--ai">
        Ask AI
        <span className="ai__tag">AI</span>
      </p>
      <div className="acard acard--ai">
        <p className="ai__q">When does Papa&apos;s health policy renew?</p>
        <div className="ai__a">
          <span className="ai__spark">
            <Sparkles size={15} strokeWidth={2} />
          </span>
          <b>15 Jan 2027</b>
          <span className="ai__link">
            View policy
            <ChevronRight size={14} strokeWidth={2.25} />
          </span>
        </div>
        <div className="ai__input">
          <span>Ask about your family&apos;s documents…</span>
          <i>
            <ArrowUp size={14} strokeWidth={2.5} />
          </i>
        </div>
      </div>
    </>
  );
}
