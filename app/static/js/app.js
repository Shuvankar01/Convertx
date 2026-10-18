// ConvertX Pro — theme, swap/unwrap helpers, searchable units, copy toast.
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

// ---------------------------------------------------------------------------
// Toast notifications
// ---------------------------------------------------------------------------
function showToast(message, tone) {
  const host = document.getElementById('toast-host');
  if (!host) return;
  const toast = document.createElement('div');
  toast.className =
    'toast pointer-events-auto flex items-center gap-2 rounded-xl border px-4 py-2.5 text-sm font-medium shadow-lg ' +
    (tone === 'error'
      ? 'border-rose-500/40 bg-rose-600 text-white'
      : 'border-slate-700 bg-slate-900 text-white');
  toast.setAttribute('role', 'status');

  const check = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
  check.setAttribute('width', '16');
  check.setAttribute('height', '16');
  check.setAttribute('viewBox', '0 0 24 24');
  check.setAttribute('fill', 'none');
  check.setAttribute('stroke', 'currentColor');
  check.setAttribute('stroke-width', '2.4');
  check.setAttribute('stroke-linecap', 'round');
  check.setAttribute('stroke-linejoin', 'round');
  const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
  path.setAttribute('d', 'M20 6 9 17l-5-5');
  check.appendChild(path);

  const label = document.createElement('span');
  label.textContent = message;

  toast.appendChild(check);
  toast.appendChild(label);
  host.appendChild(toast);

  requestAnimationFrame(function () {
    toast.classList.add('toast-in');
  });
  setTimeout(function () {
    toast.classList.remove('toast-in');
    setTimeout(function () {
      toast.remove();
    }, 300);
  }, 2200);
}

// ---------------------------------------------------------------------------
// Converter helpers
// ---------------------------------------------------------------------------
function swapUnits() {
  const form = document.getElementById('convert-form');
  if (!form) return;
  const from = form.querySelector('select[name=from_unit]');
  const to = form.querySelector('select[name=to_unit]');
  if (!from || !to) return;
  const tmp = from.value;
  from.value = to.value;
  to.value = tmp;

  const icon = document.getElementById('swap-icon');
  if (icon) icon.classList.toggle('rotate-180');

  if (window.htmx) htmx.trigger(form, 'submit');
}

function clearValue() {
  const form = document.getElementById('convert-form');
  if (!form) return;
  const input = form.querySelector('input[name=value]');
  if (input) {
    input.value = '';
    input.focus();
  }
}

function copyResult() {
  const el = document.getElementById('result-value');
  if (!el) return;
  const text = el.textContent.trim();

  function done() {
    showToast('Copied to clipboard!');
  }

  function fallback() {
    try {
      const ta = document.createElement('textarea');
      ta.value = text;
      ta.style.position = 'fixed';
      ta.style.opacity = '0';
      document.body.appendChild(ta);
      ta.select();
      document.execCommand('copy');
      ta.remove();
      done();
    } catch (err) {
      showToast('Copy failed', 'error');
    }
  }

  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(text).then(done, fallback);
  } else {
    fallback();
  }
}

// ---------------------------------------------------------------------------
// Searchable unit selectors (progressive enhancement over native <select>)
// ---------------------------------------------------------------------------
function initUnitSearch(scope) {
  const rootEl = scope && scope.querySelectorAll ? scope : document;
  const fields = [];
  if (rootEl.matches && rootEl.matches('[data-unit-field]')) fields.push(rootEl);
  rootEl.querySelectorAll('[data-unit-field]').forEach(function (f) {
    fields.push(f);
  });

  fields.forEach(function (field) {
    if (field.dataset.unitSearchReady) return;
    const select = field.querySelector('select');
    const input = field.querySelector('[data-unit-search]');
    if (!select || !input) return;
    field.dataset.unitSearchReady = '1';

    const all = Array.prototype.map.call(select.options, function (o) {
      return { value: o.value, text: (o.textContent || '').trim() };
    });

    function render(query) {
      const q = query.trim().toLowerCase();
      const current = select.value;
      while (select.firstChild) select.removeChild(select.firstChild);

      let matches = all.filter(function (o) {
        return (
          !q ||
          o.text.toLowerCase().indexOf(q) !== -1 ||
          o.value.toLowerCase().indexOf(q) !== -1
        );
      });
      if (!matches.length) matches = all.slice();

      matches.forEach(function (o) {
        const opt = document.createElement('option');
        opt.value = o.value;
        opt.textContent = o.text;
        if (o.value === current) opt.selected = true;
        select.appendChild(opt);
      });
      if (!select.value && select.options.length) select.selectedIndex = 0;
      return current;
    }

    input.addEventListener('input', function () {
      const before = select.value;
      render(input.value);
      if (select.value !== before) {
        select.dispatchEvent(new Event('change', { bubbles: true }));
      }
    });

    input.addEventListener('keydown', function (e) {
      if (e.key === 'Enter') {
        e.preventDefault();
        render(input.value);
        input.blur();
        select.dispatchEvent(new Event('change', { bubbles: true }));
      }
    });
  });
}

// ---------------------------------------------------------------------------
// Boot + re-init after HTMX swaps
// ---------------------------------------------------------------------------
document.addEventListener('DOMContentLoaded', function () {
  initUnitSearch(document);
});

if (window.htmx && typeof window.htmx.onLoad === 'function') {
  window.htmx.onLoad(function (elt) {
    initUnitSearch(elt);
  });
}
