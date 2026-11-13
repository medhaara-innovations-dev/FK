import type { CSSProperties } from "react";

/* Stagger index for [data-reveal] / [data-reveal-item] elements (read by motion.css as var(--i)). */
export const revealIndex = (i: number) => ({ "--i": i }) as CSSProperties;

/* Boot script, inlined in <head> (layout.tsx). It only turns motion on when the browser can run it:
   IntersectionObserver present and no prefers-reduced-motion. If the observer below never mounts
   (JS error, slow hydration), motion is switched off again after 3s, so nothing stays hidden. */
export const MOTION_BOOT = `(function(){try{var d=document.documentElement;if(!("IntersectionObserver" in window)||window.matchMedia("(prefers-reduced-motion: reduce)").matches)return;d.setAttribute("data-motion","");setTimeout(function(){if(!d.hasAttribute("data-motion-ready"))d.removeAttribute("data-motion")},3000)}catch(e){}})();`;
