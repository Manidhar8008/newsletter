(() => {
  const root = document.documentElement;
  const themeButton = document.querySelector('[data-theme-toggle]');
  const themeIcon = document.querySelector('.theme-icon');
  const menuButton = document.querySelector('[data-menu-toggle]');
  const mobileNav = document.querySelector('[data-mobile-nav]');
  const themeMeta = document.querySelector('#theme-color');

  const applyTheme = (theme) => {
    const light = theme !== 'dark';
    root.classList.toggle('dark', !light);
    if (themeIcon) themeIcon.textContent = light ? '☾' : '☼';
    if (themeButton) {
      themeButton.setAttribute('aria-label', light ? 'Switch to dark mode' : 'Switch to light mode');
      themeButton.setAttribute('title', light ? 'Switch to dark mode' : 'Switch to light mode');
    }
    if (themeMeta) themeMeta.setAttribute('content', light ? '#ffffff' : '#101010');
  };

  const savedTheme = localStorage.getItem('dispatch-theme-v2');
  applyTheme(savedTheme === 'dark' ? 'dark' : 'light');

  themeButton?.addEventListener('click', () => {
    const next = root.classList.contains('dark') ? 'light' : 'dark';
    localStorage.setItem('dispatch-theme-v2', next);
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

  document.querySelectorAll('[data-copy-link]').forEach((button) => {
    button.addEventListener('click', async () => {
      try {
        await navigator.clipboard.writeText(window.location.href);
        const old = button.textContent;
        button.textContent = 'Copied';
        setTimeout(() => { button.textContent = old; }, 1400);
      } catch {
        button.textContent = 'Copy failed';
        setTimeout(() => { button.textContent = 'Copy link'; }, 1400);
      }
    });
  });

  const searchInput = document.querySelector('[data-search-input]');
  const searchResults = document.querySelector('[data-search-results]');
  if (searchInput && searchResults) {
    let index = [];
    const render = (items) => {
      searchResults.innerHTML = items.length
        ? items.map((item) => `
          <article class="search-result">
            <p class="section-label">${item.section || 'DISPATCH'} · ${item.date || ''}</p>
            <h3><a href="${item.url}">${item.title}</a></h3>
            <p>${item.description || ''}</p>
          </article>`).join('')
        : '<p class="search-empty">Nothing found. Try a project, concept, or phrase.</p>';
    };
    fetch(`${document.querySelector('base')?.href || ''}${window.location.pathname.includes('/newsletter/') ? '/newsletter/search.json' : '/search.json'}`)
      .then((r) => r.ok ? r.json() : [])
      .then((data) => {
        index = Array.isArray(data) ? data : [];
        const initial = new URLSearchParams(window.location.search).get('q') || '';
        if (initial) searchInput.value = initial;
        const run = () => {
          const q = searchInput.value.trim().toLowerCase();
          const terms = q.split(/\s+/).filter(Boolean);
          const results = terms.length ? index.filter((item) => {
            const hay = [item.title, item.description, item.section, ...(item.tags || [])].join(' ').toLowerCase();
            return terms.every((term) => hay.includes(term));
          }) : index.slice(0, 20);
          render(results.slice(0, 50));
        };
        searchInput.addEventListener('input', run);
        document.querySelector('[data-search-form]')?.addEventListener('submit', (event) => { event.preventDefault(); run(); });
        run();
      })
      .catch(() => render([]));
  }
})();
