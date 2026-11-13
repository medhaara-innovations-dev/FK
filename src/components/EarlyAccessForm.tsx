"use client";

import { useRef, useState, type FormEvent } from "react";
import { ArrowRight, ShieldCheck } from "lucide-react";
import { revealIndex } from "@/lib/motion";

/* Early access form (cta-footer-spec v3 §5, mirrors site/js/cta.js). Front-end only:
   validates Email + Indian WhatsApp number and shows the confirmation. No request is sent;
   the live build will hook this to the real waitlist. */
const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

function indianMobile(value: string): string | null {
  let digits = value.replace(/\D/g, "");
  if (digits.startsWith("91") && digits.length === 12) digits = digits.slice(2);
  if (digits.startsWith("0") && digits.length === 11) digits = digits.slice(1);
  return /^[6-9]\d{9}$/.test(digits) ? digits : null;
}

type Field = "email" | "whatsapp";

export function EarlyAccessForm() {
  const emailRef = useRef<HTMLInputElement>(null);
  const waRef = useRef<HTMLInputElement>(null);
  const confirmRef = useRef<HTMLParagraphElement>(null);
  const [error, setError] = useState<{ field: Field; message: string } | null>(
    null,
  );
  const [done, setDone] = useState(false);

  const fail = (field: Field, message: string) => {
    setError({ field, message });
    (field === "email" ? emailRef : waRef).current?.focus();
  };

  const onSubmit = (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    setError(null);
    const email = emailRef.current;
    const emailVal = (email?.value || "").trim();
    const waVal = (waRef.current?.value || "").trim();

    if (!emailVal) return fail("email", "Please enter your email address.");
    if (!EMAIL_RE.test(emailVal) || (email && !email.checkValidity()))
      return fail("email", "Please enter a valid email address.");
    if (!waVal) return fail("whatsapp", "Please enter your WhatsApp number.");
    if (!indianMobile(waVal))
      return fail("whatsapp", "Please enter a 10-digit Indian WhatsApp number.");

    setDone(true);
    requestAnimationFrame(() => confirmRef.current?.focus());
  };

  const clear = () => {
    if (error) setError(null);
  };

  return (
    <form
      className="cta__form"
      action="#early-access"
      method="post"
      noValidate
      onSubmit={onSubmit}
      data-state={done ? "success" : error ? "error" : undefined}
      data-reveal=""
      style={revealIndex(3)}
    >
      <div className="cta__fields">
        <div className="cta__field">
          <label className="sr-only" htmlFor="cta-email">
            Email address
          </label>
          <input
            ref={emailRef}
            className="cta__input"
            id="cta-email"
            type="email"
            name="email"
            autoComplete="email"
            inputMode="email"
            spellCheck={false}
            required
            placeholder="Email address"
            aria-describedby="cta-form-status"
            aria-invalid={error?.field === "email" ? "true" : "false"}
            disabled={done}
            onInput={clear}
          />
        </div>
        <div className="cta__field cta__field--whatsapp">
          <label className="sr-only" htmlFor="cta-whatsapp">
            WhatsApp number
          </label>
          <div className="cta__input-wrap">
            <span className="cta__prefix" aria-hidden="true">
              +91
            </span>
            <input
              ref={waRef}
              className="cta__input"
              id="cta-whatsapp"
              type="tel"
              name="whatsapp"
              autoComplete="tel"
              inputMode="tel"
              spellCheck={false}
              required
              placeholder="98765 43210"
              aria-describedby="cta-form-status"
              aria-invalid={error?.field === "whatsapp" ? "true" : "false"}
              disabled={done}
              onInput={clear}
            />
          </div>
        </div>
        <button className="cta__submit" type="submit" disabled={done}>
          Get Early Access
          <ArrowRight size={20} strokeWidth={2} aria-hidden="true" />
        </button>
      </div>
      <p
        className="cta__error"
        id="cta-form-status"
        hidden={!error}
        role="alert"
      >
        {error?.message ?? ""}
      </p>
      <p className="cta__note">
        Free during early access · No&nbsp;spam · Indian&nbsp;servers only
      </p>
      <p
        ref={confirmRef}
        className="cta__confirm"
        hidden={!done}
        role="status"
        tabIndex={-1}
      >
        <ShieldCheck size={22} strokeWidth={1.75} aria-hidden="true" />
        You&apos;re on the early access list. We&apos;ll email or WhatsApp when
        your invite is ready.
      </p>
    </form>
  );
}
