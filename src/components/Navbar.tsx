"use client";

import {
  useCallback,
  useEffect,
  useId,
  useRef,
  useState,
} from "react";
import Image from "next/image";
import { ChevronRight, Menu, X } from "lucide-react";

const NAV_LINKS = [
  { href: "#why", label: "Why FamilyKit" },
  { href: "#how-it-works", label: "How it works" },
  { href: "#uses", label: "Uses" },
  { href: "#security", label: "Security" },
] as const;

/* "#top" (the Hero) is observed too: while it holds the middle of the viewport, no link is active. */
const SECTION_IDS = [
  "#top",
  ...NAV_LINKS.map((link) => link.href),
  "#early-access",
];

function Logo({ className }: { className?: string }) {
  return (
    <Image
      className={className}
      src="/images/familykit-logo.png"
      alt="FamilyKit"
      width={960}
      height={318}
      priority
    />
  );
}

export function Navbar() {
  const [scrolled, setScrolled] = useState(false);
  const [open, setOpen] = useState(false);
  const [active, setActive] = useState<string | null>(null);
  const menuId = useId();
  const menuBtnRef = useRef<HTMLButtonElement>(null);
  const menuRef = useRef<HTMLDivElement>(null);
  const lastFocusRef = useRef<HTMLElement | null>(null);

  useEffect(() => {
    const onScroll = () => {
      setScrolled(window.scrollY > 8);
      if (window.scrollY <= 8) setActive(null);
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  useEffect(() => {
    const observer = new IntersectionObserver(
      (entries) => {
        const visible = entries
          .filter((entry) => entry.isIntersecting)
          .sort((a, b) => b.intersectionRatio - a.intersectionRatio)[0];
        if (visible) {
          const id = "#" + visible.target.id;
          setActive(id === "#top" ? null : id);
        }
      },
      { rootMargin: "-45% 0px -50% 0px" },
    );

    for (const href of SECTION_IDS) {
      const section = document.querySelector(href);
      if (section) observer.observe(section);
    }

    return () => observer.disconnect();
  }, []);

  const [closing, setClosing] = useState(false);
  const closeTimerRef = useRef<number | null>(null);

  /* Close with a short exit animation (180ms); instant under prefers-reduced-motion. */
  const closeMenu = useCallback((restore = true) => {
    document.body.classList.remove("is-locked");
    if (restore && lastFocusRef.current) {
      lastFocusRef.current.focus({ preventScroll: true });
    }
    if (closeTimerRef.current) window.clearTimeout(closeTimerRef.current);
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
      setClosing(false);
      setOpen(false);
      return;
    }
    setClosing(true);
    closeTimerRef.current = window.setTimeout(() => {
      closeTimerRef.current = null;
      setClosing(false);
      setOpen(false);
    }, 180);
  }, []);

  const toggleMenu = useCallback(() => {
    if (open && closing) {
      if (closeTimerRef.current) window.clearTimeout(closeTimerRef.current);
      closeTimerRef.current = null;
      setClosing(false);
      document.body.classList.add("is-locked");
      return;
    }
    if (open) {
      closeMenu(false);
      return;
    }
    lastFocusRef.current = document.activeElement as HTMLElement | null;
    document.body.classList.add("is-locked");
    setOpen(true);
  }, [open, closing, closeMenu]);

  useEffect(() => {
    if (open) {
      menuBtnRef.current?.focus({ preventScroll: true });
    }
  }, [open]);

  useEffect(() => {
    if (!open) return;

    const focusables = () => {
      const items: HTMLElement[] = [];
      if (menuBtnRef.current) items.push(menuBtnRef.current);
      const menu = menuRef.current;
      if (menu) {
        items.push(
          ...menu.querySelectorAll<HTMLElement>("a[href],button:not([disabled])"),
        );
      }
      return items;
    };

    const onKey = (event: KeyboardEvent) => {
      if (event.key === "Escape") {
        event.preventDefault();
        closeMenu();
        return;
      }
      if (event.key !== "Tab") return;
      const items = focusables();
      const first = items[0];
      const last = items[items.length - 1];
      if (event.shiftKey && document.activeElement === first) {
        event.preventDefault();
        last?.focus();
      } else if (!event.shiftKey && document.activeElement === last) {
        event.preventDefault();
        first?.focus();
      }
    };

    document.addEventListener("keydown", onKey);
    const media = window.matchMedia("(min-width: 1024px)");
    const onMedia = (event: MediaQueryListEvent) => {
      if (event.matches) closeMenu(false);
    };
    media.addEventListener("change", onMedia);

    return () => {
      document.removeEventListener("keydown", onKey);
      media.removeEventListener("change", onMedia);
    };
  }, [open, closeMenu]);

  useEffect(() => {
    return () => {
      document.body.classList.remove("is-locked");
      if (closeTimerRef.current) window.clearTimeout(closeTimerRef.current);
    };
  }, []);

  return (
    <>
      <div
        className={
          "mmenu__scrim" + (open ? " is-open" : "") + (closing ? " is-closing" : "")
        }
        hidden={!open}
        onClick={() => closeMenu(true)}
      />
      <header
        className="nav"
        id="nav"
        data-scrolled={scrolled ? "true" : "false"}
        data-open={open ? "true" : "false"}
      >
        <div className="nav__inner">
          <a className="nav__logo" href="#top" aria-label="FamilyKit home">
            <Logo />
          </a>

          <nav className="nav__links" aria-label="Main">
            {NAV_LINKS.map((link) => (
              <a
                key={link.href}
                href={link.href}
                aria-current={active === link.href ? "true" : undefined}
              >
                {link.label}
              </a>
            ))}
          </nav>

          <div className="nav__actions">
            <a className="btn btn--primary nav__cta" href="#early-access">
              Get Early Access
            </a>
            <button
              ref={menuBtnRef}
              className="nav__menu-btn"
              type="button"
              aria-label={open ? "Close menu" : "Open menu"}
              aria-expanded={open}
              aria-controls={menuId}
              onClick={toggleMenu}
            >
              {open ? (
                <X size={24} strokeWidth={2} aria-hidden="true" />
              ) : (
                <Menu size={24} strokeWidth={2} aria-hidden="true" />
              )}
            </button>
          </div>
        </div>

        <div
          ref={menuRef}
          className={"mmenu" + (open ? " is-open" : "") + (closing ? " is-closing" : "")}
          id={menuId}
          role="dialog"
          aria-modal="true"
          aria-label="Menu"
          hidden={!open}
        >
          <nav className="mmenu__links" aria-label="Main">
            {NAV_LINKS.map((link) => (
              <a
                key={link.href}
                href={link.href}
                aria-current={active === link.href ? "true" : undefined}
                onClick={() => closeMenu(false)}
              >
                <span>{link.label}</span>
                <ChevronRight size={20} strokeWidth={2} aria-hidden="true" />
              </a>
            ))}
          </nav>
          <div className="mmenu__bottom">
            <a
              className="btn btn--primary btn--block"
              href="#early-access"
              onClick={() => closeMenu(false)}
            >
              Get Early Access
            </a>
          </div>
        </div>
      </header>
    </>
  );
}
