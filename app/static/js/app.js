// Minimal vanilla JS: theme toggle, swap units, copy result.
(function () {
  const root = document.documentElement;

  function applyTheme(theme) {
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    const dark = theme === 'dark' || (theme === 'system' && prefersDark);
    root.classList.toggle('dark', dark);
  }

  const stored = localStorage.getItem('convertx-theme') || 'system';
  applyTheme(stored);

  const toggle = document.getElementById('theme-toggle');
  if (toggle) {
    toggle.addEventListener('click', function () {
      const current = localStorage.getItem('convertx-theme') || 'system';
      const next = current === 'dark' ? 'light' : 'dark';
      localStorage.setItem('convertx-theme', next);
      applyTheme(next);
    });
  }

  const themeSelect = document.getElementById('theme-select');
  if (themeSelect) {
    themeSelect.addEventListener('change', function (e) {
      localStorage.setItem('convertx-theme', e.target.value);
      applyTheme(e.target.value);
    });
  }
})();

function swapUnits() {
  const form = document.getElementById('convert-form');
  if (!form) return;
  const from = form.querySelector('select[name=from_unit]');
  const to = form.querySelector('select[name=to_unit]');
  if (!from || !to) return;
  const tmp = from.value;
  from.value = to.value;
  to.value = tmp;
  if (window.htmx) htmx.trigger(form, 'submit');
}

function clearValue() {
  const form = document.getElementById('convert-form');
  if (!form) return;
  const input = form.querySelector('input[name=value]');
  if (input) { input.value = ''; input.focus(); }
}

function copyResult() {
  const el = document.getElementById('result-value');
  if (!el) return;
  const text = el.textContent.trim();
  if (navigator.clipboard) {
    navigator.clipboard.writeText(text);
  }
}
