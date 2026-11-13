"use client";

import { useEffect } from "react";

/* One observer for the whole page: adds .is-in to each [data-reveal] once it scrolls into view (once: true). */
export function RevealObserver() {
  useEffect(() => {
    const root = document.documentElement;
    const els = Array.from(document.querySelectorAll<HTMLElement>("[data-reveal]"));
    if (!root.hasAttribute("data-motion") || !("IntersectionObserver" in window)) {
      els.forEach((el) => el.classList.add("is-in"));
      return;
    }
    const io = new IntersectionObserver(
      (entries) => {
        for (const entry of entries) {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-in");
            io.unobserve(entry.target);
          }
        }
      },
      { rootMargin: "0px 0px -8% 0px", threshold: 0 },
    );
    els.forEach((el) => io.observe(el));
    root.setAttribute("data-motion-ready", "");
    return () => io.disconnect();
  }, []);
  return null;
}
