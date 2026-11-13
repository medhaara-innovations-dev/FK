import Image from "next/image";

const FOOTER_LINKS = [
  { href: "#why", label: "Why FamilyKit" },
  { href: "#how-it-works", label: "How it works" },
  { href: "#uses", label: "Uses" },
  { href: "#security", label: "Security" },
  /* Placeholder route until the privacy policy page is built (404s on the static preview). */
  { href: "/privacy-policy", label: "Privacy Policy" },
] as const;

/* Footer · cta-footer-spec v3. White, 1px #ECE8F5 divider, official full-colour logo (same file as the navbar). */
export function Footer() {
  return (
    <footer className="footer">
      <div className="footer__inner">
        <div className="footer__brand">
          <a className="footer__logo" href="#top" aria-label="FamilyKit home">
            <Image
              src="/images/familykit-logo.png"
              width={960}
              height={318}
              alt="FamilyKit"
              loading="lazy"
            />
          </a>
          <p className="footer__tagline">
            Everything important about your family, in one place.
          </p>
        </div>
        <nav className="footer__links" aria-label="Footer">
          {FOOTER_LINKS.map((link) => (
            <a key={link.href} href={link.href}>
              {link.label}
            </a>
          ))}
        </nav>
      </div>
      <div className="footer__bar">
        <p className="footer__copy">
          © 2026 Medhaara Innovations. Made in India.
        </p>
        <p className="footer__trust">AES-256 encrypted · Data stored in India</p>
      </div>
    </footer>
  );
}
