# ConvertX — Smart Unit Converter

ConvertX is a production-style **unit conversion web application** built with **FastAPI, Jinja2, HTMX, SQLAlchemy, and SQLite**.  
It is designed as a **Python-first server-rendered application** that provides fast, accurate unit conversions across multiple categories, while also supporting **conversion history, favorites, settings, reusable conversion logic, and dynamic partial updates**.

This project demonstrates how to build a clean, modular backend-driven web app with **FastAPI + Jinja2** instead of relying on a heavy frontend framework.

---

## Screenshots

### Dashboard
![ConvertX Dashboard](docs/screenshots/dashboard.png)

### Converter Workspace
![ConvertX Converter Workspace](docs/screenshots/converter-workspace.png)

### Conversion Unit
![Conversion Unit](docs/screenshots/conversion-unit.png)

### History Tracking
![ConvertX History Page](docs/screenshots/history.png)

### Favorites
![ConvertX Favorites Page](docs/screenshots/favorites.png)

### Settings
![ConvertX Settings Page](docs/screenshots/settings.png)

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
- **Python 3.12+**
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
│   │   ├── session.py
│   │   └── models/
│   │
│   ├── repositories/
│   ├── schemas/
│   ├── services/
│   │
│   ├── routers/
│   │   ├── converter.py
│   │   ├── favorites.py
│   │   ├── history.py
│   │   ├── pages.py
│   │   └── settings.py
│   │
│   ├── templates/
│   │   ├── base templates
│   │   ├── pages
│   │   └── partials
│   │
│   └── static/
│
├── tests/
├── requirements.txt
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

The project is structured so it can be migrated to **PostgreSQL** later with minimal architectural changes if the database URL and driver are updated appropriately.

Example PostgreSQL connection string:

```env
CONVERTX_DATABASE_URL=postgresql+psycopg://user:password@localhost/convertx
```

Install PostgreSQL driver if needed:

```bash
pip install "psycopg[binary]"
```

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
- PostgreSQL production configuration
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

This project is **not intended to be run as a standalone Vite/TanStack frontend app**.  
If older experimental frontend files exist from a previous setup, they are not part of the final ConvertX architecture and should not be treated as the main runtime for this project.

---

# Resume / Portfolio Summary

**ConvertX — Smart Unit Converter**  
Built a production-style unit conversion web application using **FastAPI, Jinja2, HTMX, SQLAlchemy, and SQLite**. Implemented a modular conversion engine supporting **15 unit categories**, dynamic partial rendering, persistent history and favorites, configurable settings, and a layered backend architecture with routers, services, repositories, and reusable converter modules.

---

# License

This project is licensed under the **MIT License**.

