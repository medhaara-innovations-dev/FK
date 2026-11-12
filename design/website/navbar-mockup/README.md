# FamilyKit landing page v2 (static HTML/CSS), built section by section
Fresh build on the locked brand foundation. Separate from the older Next.js app in ../src (untouched).
- index.html: page shell. Navbar done; sections are empty anchors (#top hero, #why, #how, #security, #pricing, #early-access) to fill one at a time.
- css/fonts.css (self-hosted Poppins 500/600, Mulish 400/600 in fonts/), css/familykit-brand.css (copy of /workspace/fk-palette), css/base.css (layout vars, buttons, focus), css/navbar.css
- js/navbar.js: scrolled state (>8px), mobile menu (Esc, focus trap, scroll lock), current-section marker
- assets/familykit-logo.png: founder horizontal light logo, trimmed to its edges, 480px wide
- _capture/: capture.py (Playwright shots, DSF 2) + sheets.py/desktop.html/mobile.html -> ../review/
Preview: cd site && python3 -m http.server 18731
