(() => {
  const nav = document.getElementById('nav');
  const menu = document.getElementById('mobile-menu');
  const openBtn = nav.querySelector('.nav__menu-btn');
  const closeBtn = menu.querySelector('.mmenu__close');

  // Scrolled state: shorter bar, white translucent background, hairline + soft shadow
  const onScroll = () => { nav.dataset.scrolled = String(window.scrollY > 8); };
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  // Mobile menu: open/close, Esc, focus trap, scroll lock
  let lastFocus = null;
  const focusables = () => [...menu.querySelectorAll('a[href],button:not([disabled])')];
  function openMenu(){
    lastFocus = document.activeElement;
    menu.hidden = false; menu.classList.add('is-open');
    openBtn.setAttribute('aria-expanded','true');
    document.body.classList.add('is-locked');
    closeBtn.focus({ preventScroll: true });
  }
  function closeMenu(restore = true){
    menu.hidden = true; menu.classList.remove('is-open');
    openBtn.setAttribute('aria-expanded','false');
    document.body.classList.remove('is-locked');
    if (restore && lastFocus) lastFocus.focus({ preventScroll: true });
  }
  openBtn.addEventListener('click', openMenu);
  menu.querySelectorAll('[data-close]').forEach(el => el.addEventListener('click', () => closeMenu(el.tagName === 'BUTTON')));
  document.addEventListener('keydown', e => {
    if (menu.hidden) return;
    if (e.key === 'Escape') closeMenu();
    if (e.key === 'Tab') {
      const f = focusables(), first = f[0], last = f[f.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    }
  });
  window.matchMedia('(min-width:1024px)').addEventListener('change', e => { if (e.matches && !menu.hidden) closeMenu(false); });

  // Highlight the section in view
  const links = [...document.querySelectorAll('.nav__links a')];
  const io = new IntersectionObserver(entries => {
    entries.forEach(en => {
      if (!en.isIntersecting) return;
      links.forEach(a => a.getAttribute('href') === '#' + en.target.id ? a.setAttribute('aria-current','true') : a.removeAttribute('aria-current'));
    });
  }, { rootMargin: '-45% 0px -50% 0px' });
  links.forEach(a => { const s = document.querySelector(a.getAttribute('href')); if (s) io.observe(s); });
})();
