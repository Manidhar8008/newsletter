(() => {
  const root = document.documentElement;
  const themeButton = document.querySelector('[data-theme-toggle]');
  const themeIcon = document.querySelector('.theme-icon');
  const menuButton = document.querySelector('[data-menu-toggle]');
  const mobileNav = document.querySelector('[data-mobile-nav]');

  const applyTheme = (theme) => {
    const light = theme === 'light';
    root.classList.toggle('light', light);
    if (themeIcon) themeIcon.textContent = light ? '☾' : '☼';
    if (themeButton) {
      themeButton.setAttribute('aria-label', light ? 'Switch to dark mode' : 'Switch to light mode');
      themeButton.setAttribute('title', light ? 'Switch to dark mode' : 'Switch to light mode');
    }
  };

  const savedTheme = localStorage.getItem('dispatch-theme');
  applyTheme(savedTheme === 'light' ? 'light' : 'dark');

  themeButton?.addEventListener('click', () => {
    const next = root.classList.contains('light') ? 'dark' : 'light';
    localStorage.setItem('dispatch-theme', next);
    applyTheme(next);
  });

  menuButton?.addEventListener('click', () => {
    const isOpen = mobileNav?.classList.toggle('open') ?? false;
    menuButton.setAttribute('aria-expanded', String(isOpen));
    menuButton.setAttribute('aria-label', isOpen ? 'Close menu' : 'Open menu');
  });

  mobileNav?.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', () => {
      mobileNav.classList.remove('open');
      menuButton?.setAttribute('aria-expanded', 'false');
      menuButton?.setAttribute('aria-label', 'Open menu');
    });
  });
})();
