# ConvertX — Smart Unit Converter

ConvertX is a production-style **unit conversion web application** built with **FastAPI, Jinja2, HTMX, SQLAlchemy, and SQLite**.  
It is designed as a **Python-first server-rendered application** that provides fast, accurate unit conversions across multiple categories, while also supporting **conversion history, favorites, settings, reusable conversion logic, and dynamic partial updates**.

This project demonstrates how to build a clean, modular backend-driven web app with **FastAPI + Jinja2** instead of relying on a heavy frontend framework.

---

## Screenshots

### Dashboard
![ConvertX Dashboard](app/docs/screenshots/dashboard.png)

### Converter Workspace
![ConvertX Converter Workspace](app/docs/screenshots/converter-workspace.png)

### Conversion Unit
![Conversion Unit](app/docs/screenshots/conversion-unit.png)

### History Tracking
![ConvertX History Page](app/docs/screenshots/history.png)

### Favorites
![ConvertX Favorites Page](app/docs/screenshots/favorites.png)

### Settings
![ConvertX Settings Page](app/docs/screenshots/settings.png)

---

## Features

- **15 conversion categories**:
  - Length
  - Weight / Mass
  - Temperature
  - Area
  - Volume
  - Time
  - Speed
  - Data Storage
  - Pressure
  - Energy
  - Power
  - Angle
  - Frequency
  - Fuel Economy
  - Digital Transfer Rate

- **Interactive converter workspace**
  - category selection
  - value input
  - from-unit and to-unit selection
  - precision control
  - swap support
  - result rendering with partial updates

- **HTMX-powered dynamic UI**
  - updates result cards without full page reload
  - refreshes unit selectors dynamically based on category

- **Persistent history**
  - stores successful conversions in SQLite
  - enables recent conversion tracking

- **Favorites system**
  - save frequently used unit pairs
  - quickly access commonly repeated conversions

- **Settings support**
  - configurable app behavior such as precision and history preferences

- **Modular conversion engine**
  - dedicated converter modules for each category
  - clean registry-based converter resolution
  - easy to extend with new categories and units

- **Server-rendered architecture**
  - FastAPI for routing and application logic
  - Jinja2 templates for pages and partials
  - SQLAlchemy ORM for persistence

- **Testing support**
  - Pytest-based testing for conversion logic and routes

---

# Tech Stack

## Backend
- **Python 3.12+** (pinned to **3.14** via `.python-version`, matching local development)
- **FastAPI**
- **Pydantic v2**
- **SQLAlchemy 2.x**
- **SQLite**

## Frontend / Templating
- **Jinja2**
- **HTMX**
- **Tailwind CSS**

## Testing
- **Pytest**

---

# Project Architecture

ConvertX follows a **layered backend architecture** to keep the codebase modular, maintainable, and easy to extend.

## Main layers

### 1) Routers
FastAPI routers handle HTTP endpoints and request/response flow.

Examples:
- page routes
- converter routes
- favorites routes
- history routes
- settings routes

### 2) Services
The service layer contains business logic such as:
- performing conversions
- recording history
- checking / toggling favorites
- reading and updating settings

### 3) Converters
Each conversion category is implemented in its own converter module.  
This keeps the conversion logic isolated and reusable.

### 4) Repositories / Database layer
Database operations are handled through SQLAlchemy-backed models and persistence logic.

### 5) Templates and partials
Jinja2 templates render:
- full pages
- reusable HTML partials
- HTMX responses for dynamic UI updates

---

# Supported Categories

| Category | Description |
|---|---|
| Length | Distance and size conversions |
| Weight / Mass | Metric and imperial mass conversions |
| Temperature | Celsius, Fahrenheit, Kelvin conversions |
| Area | Surface measurement conversions |
| Volume | Liquid and space volume conversions |
| Time | Time unit conversions |
| Speed | Velocity conversions |
| Data Storage | Bytes, KB, MB, GB, TB, etc. |
| Pressure | Pressure measurement conversions |
| Energy | Joules, calories, kWh, etc. |
| Power | Watts, kilowatts, horsepower, etc. |
| Angle | Degree and radian conversions |
| Frequency | Hz, kHz, MHz, GHz conversions |
| Fuel Economy | Mileage and fuel consumption conversions |
| Digital Transfer Rate | bps, Kbps, Mbps, Gbps, etc. |

---

# Project Structure

```text
ConvertX/
│
├── app/
│   ├── main.py
│   ├── config.py
│   ├── dependencies.py
│   │
│   ├── core/
│   │   ├── constants.py
│   │   ├── enums.py
│   │   ├── exceptions.py
│   │   └── utils.py
│   │
│   ├── converters/
│   │   ├── base.py
│   │   ├── registry.py
│   │   ├── length.py
│   │   ├── weight.py
│   │   ├── temperature.py
│   │   └── ...
│   │
│   ├── db/
│   │   ├── base.py
│   │   ├── session.py
│   │   └── models/
│   │
│   ├── repositories/
│   ├── schemas/
│   ├── services/
│   │
│   ├── routers/
│   │   ├── _templating.py
│   │   ├── converter.py
│   │   ├── favorites.py
│   │   ├── history.py
│   │   ├── pages.py
│   │   └── settings.py
│   │
│   ├── templates/
│   │   ├── base.html
│   │   ├── pages/
│   │   └── partials/
│   │
│   ├── static/
│   │   ├── css/app.css
│   │   ├── js/app.js
│   │   └── icons/favicon.svg
│   │
│   ├── docs/screenshots/
│   │
│   └── tests/
│       ├── conftest.py
│       ├── test_conversion_service.py
│       ├── test_deployment_config.py
│       ├── test_fuel_economy.py
│       ├── test_history_and_settings.py
│       ├── test_routes.py
│       └── test_temperature_converter.py
│
├── requirements.txt
├── pytest.ini
├── .python-version
├── README.md
└── .gitignore
```

---

# How It Works

## Conversion flow

1. The user enters a value, category, and unit pair in the converter form.
2. The request is sent to a FastAPI route.
3. The route validates the input and identifies the selected conversion category.
4. The `ConversionService` calls the correct converter via the converter registry.
5. The conversion result is generated.
6. If history is enabled, the conversion is stored in the database.
7. Favorite status is checked for the selected unit pair.
8. A Jinja2 partial (such as a result card) is rendered and returned.
9. HTMX updates only the relevant part of the page without a full reload.

---

# Why This Project Matters

ConvertX is more than a basic calculator project. It demonstrates practical backend engineering skills and clean software design, including:

- building APIs and web routes with FastAPI
- structuring a Python project with routers, services, repositories, and domain modules
- implementing reusable business logic for multiple conversion domains
- rendering server-side templates with Jinja2
- using HTMX for interactive partial page updates
- persisting application data with SQLAlchemy and SQLite
- managing settings, history, and favorites in a maintainable way
- designing a project that can later scale to PostgreSQL or deployment environments

---

# Installation

## 1) Clone the repository
```bash
git clone https://github.com/<your-username>/convertx-smart-unit-converter.git
cd convertx-smart-unit-converter
```

## 2) Create a virtual environment

### Windows PowerShell
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### Windows CMD
```cmd
python -m venv .venv
.venv\Scripts\activate.bat
```

### macOS / Linux
```bash
python -m venv .venv
source .venv/bin/activate
```

## 3) Install dependencies
```bash
pip install -r requirements.txt
```

## 4) Run the FastAPI application
```bash
uvicorn app.main:app --reload
```

## 5) Open in browser
```text
http://127.0.0.1:8000
```

---

# Running Tests

Run the test suite with:

```bash
pytest -q
```

For verbose output:

```bash
pytest -v
```

---

# Database

By default, ConvertX uses **SQLite** for local development.

By default the database file is written to `convertx.db` in the repository root.
If that directory is not writable — which is the case on read-only serverless
filesystems such as Vercel Functions — `app/config.py` automatically falls back
to a SQLite file inside the system temp directory so the app can still start.

The project is structured so it can be migrated to **PostgreSQL** later with minimal architectural changes if the database URL and driver are updated appropriately.

Example PostgreSQL connection string:

```env
CONVERTX_DATABASE_URL=postgresql+psycopg://user:password@localhost/convertx
```

Install PostgreSQL driver if needed:

```bash
pip install "psycopg[binary]"
```

> **Read this before deploying:** SQLite is fine for local development, but it is
> **not durable persistent storage on Vercel**. See
> [Deployment — Vercel](#deployment--vercel) below.

---

# Deployment — Vercel

ConvertX is a plain **FastAPI** application that exports an `app` instance from
`app/main.py`. Vercel supports FastAPI with **zero configuration**, so there is
no `vercel.json`, no `/api` directory, and no rewrite rules to add.

Vercel detects this project automatically because:

- `requirements.txt` declares `fastapi`, which triggers the Python framework preset
- the ASGI entrypoint `app/main.py` exports a variable named `app`
- the Python version is pinned in `.python-version`

## Steps

1. **Push the repository to GitHub.**

   ```bash
   git add -A
   git commit -m "Prepare ConvertX for first Vercel deployment"
   git push origin main
   ```

2. **Import the repository into Vercel.**
   Go to [vercel.com/new](https://vercel.com/new) and choose **Add New… → Project**
   → import the GitHub repository.

3. **Select the repository root as the project root.**
   Leave the root directory as `/` (the folder containing `requirements.txt` and
   `app/`). Do **not** set an output directory or build command.

4. **Allow Vercel to detect the FastAPI application.**
   The **Framework Preset** should show *FastAPI* and the entrypoint should
   resolve to `app/main.py`. If Vercel ever fails to detect it, set the
   entrypoint explicitly in `pyproject.toml`:

   ```toml
   [tool.vercel]
   entrypoint = "app.main:app"
   ```

   You should not need this — it is only a fallback.

5. **Configure environment variables.**
   ConvertX has **no required environment variables** and ships with working
   defaults. Add `CONVERTX_DATABASE_URL` only if you want to point at a
   different database. See [Environment Variables](#environment-variables).

6. **Deploy.**
   Click **Deploy**. Vercel installs `requirements.txt`, detects the FastAPI
   framework, and builds a single Vercel Function from `app/main.py`.

7. **Open the generated deployment URL** (for example
   `https://convertx-xxxx.vercel.app`).

8. **Test the major routes:**

   | Route | What to check |
   |---|---|
   | `/` | Dashboard renders, category cards load |
   | `/converter` | Pick a category, submit the form, result appears **without a full page reload** (HTMX) |
   | `/supported-units` | All 15 categories and their units are listed |
   | `/history` | The conversion you just ran is listed |
   | `/favorites` | Star a result, then confirm it appears here |
   | `/settings` | Change precision/theme, reload and confirm it persisted |
   | `/about` | Renders |

   Also confirm the browser console is free of `404`s for `/static/css/app.css`,
   `/static/js/app.js` and `/static/icons/favicon.svg`.

## Static files on Vercel

`app/main.py` mounts `app/static/` at `/static` with Starlette's `StaticFiles`.
Vercel detects `StaticFiles` mounts at build time, copies the directory to its
CDN output, and serves those assets from the edge. No `public/` directory and no
extra configuration is required.

## Environment Variables

All settings are read from the environment with the `CONVERTX_` prefix. **None
are required** — ConvertX boots with built-in defaults.

| Variable | Default | Purpose |
|---|---|---|
| `CONVERTX_DATABASE_URL` | local `convertx.db` (temp dir fallback) | SQLAlchemy database URL |
| `CONVERTX_APP_NAME` | `ConvertX` | Application name shown in templates |
| `CONVERTX_TAGLINE` | *(see `app/config.py`)* | Tagline shown on the dashboard and About page |
| `CONVERTX_MAX_HISTORY_ITEMS` | `200` | Maximum retained history rows |
| `CONVERTX_DEFAULT_PRECISION` | `4` | Fallback precision setting |

Do not set `CONVERTX_TEMPLATES_DIR` or `CONVERTX_STATIC_DIR` on Vercel: the
defaults are absolute paths inside the deployed bundle, and overriding them
breaks template rendering and static-file serving.

## SQLite persistence on Vercel — important limitation

**SQLite is suitable for local development, but it must not be treated as
durable persistent storage for a production Vercel deployment.**

Vercel Functions run on an ephemeral filesystem. If the project directory is
read-only, ConvertX falls back to writing SQLite into the system temp
directory. What that means in practice:

- **History, favorites and settings will not survive.** Any redeploy, or simply
  waiting for an idle instance to be recycled and replaced, discards them and
  starts from a fresh, empty database.
- **Data is not shared between instances.** If several instances serve requests
  at once, each has its own database file, so one visitor cannot see another
  visitor's history, and updates may appear to be lost.
- **Data is not shared between deployments.** A new preview or production
  deployment starts empty.
- This is acceptable for a demo or first deployment, where conversions work
  normally for the life of a warm instance. It is not acceptable for real user
  data.

To get durable storage, introduce **PostgreSQL** (or another external, managed
datastore such as Neon or Supabase) in a later phase and point
`CONVERTX_DATABASE_URL` at it. Nothing in the schema, repositories or services
needs to change — see [Future Improvements](#future-improvements).

## Deploying from the Vercel CLI instead

```bash
npm i -g vercel
vercel            # preview deployment
vercel --prod     # production deployment
```

Use `vercel dev` to run the app locally against Vercel's build configuration
(requires CLI 48.1.8 or newer).

---

# Example Capabilities

ConvertX can be used for:

- metric ↔ imperial conversions
- engineering and scientific unit conversions
- data storage and transfer-rate calculations
- fuel economy comparison
- everyday measurement conversion workflows
- learning and experimenting with structured conversion logic

---

# Future Improvements

Possible future enhancements include:

- user authentication and account-based preferences
- exportable conversion history
- REST API endpoints for external programmatic usage
- Dockerized deployment setup
- **PostgreSQL production configuration** (required for durable history,
  favorites and settings on Vercel — see
  [Deployment — Vercel](#deployment--vercel))
- search and fuzzy matching for units
- usage analytics dashboard
- advanced presets and saved conversion profiles
- internationalization / multi-language support

---

# Local Development Notes

This repository is a **Python-first FastAPI application**.

The main local development command is:

```bash
uvicorn app.main:app --reload
```

To exercise a production-like configuration locally:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

This project is **not intended to be run as a standalone Vite/TanStack frontend app**.  
If older experimental frontend files exist from a previous setup, they are not part of the final ConvertX architecture and should not be treated as the main runtime for this project.

---

# Resume / Portfolio Summary

**ConvertX — Smart Unit Converter**  
Built a production-style unit conversion web application using **FastAPI, Jinja2, HTMX, SQLAlchemy, and SQLite**. Implemented a modular conversion engine supporting **15 unit categories**, dynamic partial rendering, persistent history and favorites, configurable settings, and a layered backend architecture with routers, services, repositories, and reusable converter modules.

---

# License

This project is licensed under the **MIT License**.

