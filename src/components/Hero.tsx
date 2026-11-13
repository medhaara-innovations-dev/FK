import Image from "next/image";
import {
  ArrowDown,
  ArrowRight,
  Bell,
  Cake,
  Car,
  Check,
  ChevronRight,
  CircleAlert,
  House,
  LayoutGrid,
  Plus,
  ShieldCheck,
  Sparkles,
  UserCheck,
  Users,
  Wallet,
  Wifi,
} from "lucide-react";
import { ASK_AI_ALT, PhoneAskAI } from "@/components/PhoneAskAI";

/* Ask AI is not confirmed by the founder yet. Set to false to remove it from the phone (and from the alt text). */
const SHOW_ASK_AI = true;

const VISUAL_ALT =
  "The FamilyKit app on a phone. Needs attention: motor insurance renews tomorrow, with the insurance advisor Rajesh Kumar one tap away and buttons to mark it as done or view the policy. Upcoming: Arjun's birthday on 24 October, in 5 days.";

/* Mockup's exact phone glyph (lucide-react 1.x draws "phone" differently; the founder wants this card pixel-exact). */
function PhoneIcon() {
  return (
    <svg
      viewBox="0 0 24 24"
      width="14"
      height="14"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z" />
    </svg>
  );
}

/* Hero (#top) · hero-spec v3. Phone contents are sample illustration data only. */
export function Hero({ showAskAI = SHOW_ASK_AI }: { showAskAI?: boolean }) {
  return (
    <section id="top" className="hero" aria-labelledby="hero-title">
      <div className="hero__inner">
        <div className="hero__copy">
          <p className="hero__eyebrow">
            <Users size={16} strokeWidth={2} aria-hidden="true" />
            For the whole family
          </p>
          <h1 className="hero__title" id="hero-title">
            Everything important,{" "}
            <span className="hero__accent">in one place.</span>
          </h1>
          <p className="hero__lede">
            You don&apos;t have to remember where everything is. FamilyKit
            remembers for you.
          </p>
          <div className="hero__actions">
            <a
              className="btn btn--primary btn--lg hero__cta"
              href="#early-access"
            >
              Get Early Access
              <ArrowRight size={20} strokeWidth={2} aria-hidden="true" />
            </a>
            <a className="btn btn--secondary btn--lg hero__secondary" href="#how-it-works">
              See how it works
              <ArrowDown size={18} strokeWidth={2} aria-hidden="true" />
            </a>
          </div>
          <ul className="hero__points" aria-label="Why families trust FamilyKit">
            <li>
              <span className="hero__point-ic" aria-hidden="true">
                <ShieldCheck size={20} strokeWidth={2} />
              </span>
              <span>Secure &amp; Private</span>
            </li>
            <li>
              <span className="hero__point-ic" aria-hidden="true">
                <UserCheck size={20} strokeWidth={2} />
              </span>
              <span>You&apos;re in control</span>
            </li>
            <li>
              <span className="hero__point-ic" aria-hidden="true">
                <Sparkles size={20} strokeWidth={2} />
              </span>
              <span>AI-Powered</span>
            </li>
          </ul>
        </div>

        <div
          className="hero__visual"
          role="img"
          aria-label={VISUAL_ALT + (showAskAI ? ASK_AI_ALT : "")}
        >
          <div className="hero__glow" aria-hidden="true" />
          <div className="hero__ring" aria-hidden="true">
            {/* Decorative orbit (v16): only drawn when motion is allowed (motion.css). */}
            <span className="hero__orbit" />
          </div>
          <div className="phone" aria-hidden="true">
            <i className="phone__btn phone__btn--a" />
            <i className="phone__btn phone__btn--b" />
            <i className="phone__btn phone__btn--c" />
            <div className="phone__screen">
              <div className="app__status">
                <span className="app__time">9:41</span>
                <span className="app__island" />
                <span className="app__status-icons">
                  <span className="app__bars">
                    <i />
                    <i />
                    <i />
                    <i />
                  </span>
                  <Wifi size={15} strokeWidth={2.5} />
                  <span className="app__batt">
                    <i />
                  </span>
                </span>
              </div>
              <div className="app__head">
                <Image
                  src="/images/familykit-mark-96.png"
                  width={34}
                  height={35}
                  alt=""
                  priority
                />
                <div>
                  <p className="app__hi">Good morning,</p>
                  <p className="app__name">Sharma family</p>
                </div>
                <span className="app__bell">
                  <Bell size={18} strokeWidth={2} />
                </span>
              </div>

              <div className="app__body">
                <p className="app__h app__h--urgent">
                  <CircleAlert size={16} strokeWidth={2} />
                  Needs attention
                </p>
                <div className="acard acard--attn">
                  <div className="attn__top">
                    <span className="app__ic">
                      <Car size={20} strokeWidth={2} />
                    </span>
                    <div className="attn__txt">
                      <div className="attn__meta">
                        <span className="attn__kicker">Insurance</span>
                        <em className="app__chip app__chip--urgent">
                          Renews tomorrow
                        </em>
                      </div>
                      <b className="attn__title">Motor Insurance</b>
                    </div>
                  </div>
                  <div className="attn__adv">
                    <span className="attn__avatar">RK</span>
                    <div>
                      <small>Insurance advisor</small>
                      <b>Rajesh Kumar</b>
                    </div>
                    <span className="attn__call">
                      <PhoneIcon />
                      Call
                    </span>
                  </div>
                  <div className="attn__btns">
                    <span className="abtn">
                      <Check size={15} strokeWidth={2.5} />
                      Mark as done
                    </span>
                    <span className="abtn abtn--primary">View policy</span>
                  </div>
                </div>

                <p className="app__h">Upcoming</p>
                <div className="acard acard--row">
                  <span className="app__ic">
                    <Cake size={20} strokeWidth={2} />
                  </span>
                  <div>
                    <b>Arjun&apos;s Birthday</b>
                    <small>24 Oct · In 5 days</small>
                  </div>
                  <ChevronRight
                    className="acard__chev"
                    size={18}
                    strokeWidth={2}
                  />
                </div>

                {showAskAI && <PhoneAskAI />}
              </div>

              <nav className="app__tabbar">
                <span className="is-on">
                  <House size={22} strokeWidth={2} />
                  Home
                </span>
                <span>
                  <Users size={22} strokeWidth={2} />
                  Family
                </span>
                <span className="app__plus">
                  <b>
                    <Plus size={24} strokeWidth={2.25} />
                  </b>
                </span>
                <span>
                  <LayoutGrid size={22} strokeWidth={2} />
                  Categories
                </span>
                <span>
                  <Wallet size={22} strokeWidth={2} />
                  Pay &amp; Renew
                </span>
              </nav>
              <span className="app__home-ind" />
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
