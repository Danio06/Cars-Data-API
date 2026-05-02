# Cars Data API

## Overview

Cars Data API is a backend project for querying BMW specifications such as models, generations, engines, and transmissions.

The project focuses on learning backend fundamentals by evolving from a simple script into a structured application with a layered architecture, query parsing, a relational database, and a REST API.

Development path:  
MVP → Layered Architecture → JSON Dataset → ETL → SQLite → PostgreSQL → REST API → Cloud Deploy → Frontend → Unit Tests

---

## Current Features

- BMW dataset stored in JSON as source of truth (multiple series supported)
- PostgreSQL database used for runtime queries (hosted on Render)
- REST API (FastAPI) for programmatic access, deployed to Render
- Interactive frontend hosted on GitHub Pages
- Layered architecture: Parser/Service/Repository/API
- Smart scope detection: model(F30), series(3_series), family(X→X1-X7), intent(suv, coupe, sedan)
- Unit test suite (pytest) covering parser logic - 7/7 passing
- Rule-based parsing using ragex (model, fuel type, intent)
- Dynamic model and series detection based on database content
- Filtering by:
  - model generation (E90, F30, G20, etc.)
  - series (e.g. 3 Series, X5)
  - fuel type (petrol, diesel, hybrid)
- Support for multiple generations in a single query
- "Best engine" query support with reasoning
- Data seeding on API startup (JSON → PostgreSQL)

---

## Live Demo

**Frontend:** https://danio06.github.io/CarsFrontEnd/  
**API:** https://cars-data-api.onrender.com  
**Docs (Swagger):** https://cars-data-api.onrender.com/docs

> Note: API is hosted on Render free tier — first request may take ~30s (cold start).

---

## REST API (FastAPI)

- Interactive docs: `/docs` (Swagger UI)
- Endpoint: `GET /search?q={query}`

### Example Usage

Request:
```
GET https://cars-data-api.onrender.com/search?q=e90
```

Response: BMW E90 dataset including engines and transmission.

---

## How to Run Locally

1. Clone the repository:
```
git clone https://github.com/Danio06/Cars-Data-API.git
cd Cars-Data-API
```

2. Set environment variable:
```
DATABASE_URL=your_postgresql_connection_string
```

3. Install dependencies:
```
pip install -r requirements.txt
```

4. Run the API:
```
uvicorn api:app --reload
```

5. Visit:
```
http://127.0.0.1:8000/docs
```

6. (Optional) Run CLI version:
```
python app.py
```
7. Run unit tests:

```

python -m pytest test.py
```

---

## Example Usage

```
Ask: e90
Returns engines and transmissions for E90

Ask: f30 petrol
Returns petrol engines only

Ask: g20 best diesel
Returns best diesel engine recommendation

Ask: 3 series
Returns all available generations for BMW 3 Series

Ask: X
Returns entire X-family

```

---

## Project Structure

```
main.py         FastAPI entry point
api.py          FastAPI REST API layer
service.py      Business logic and orchestration
carparser.py    Smart query parser (scope, fuel, intent detection)
carsdatabase.py ETL script for loading JSON data into PostgreSQL
db.py           Database connection helper
datacars.json   Source dataset
app.py          CLI interface and output formatting
repository/
    cars_rep.py Repository layer — all SQL queries isolated here
test.py         Unit tests for parser logic (pytest, 7/7)
```

---

## Tech Stack

```
Python 3
FastAPI
PostgreSQL (psycopg2)
pytest
Uvicorn
Render (cloud deployment)
GitHub Pages (frontend hosting)
JSON
Regex (pattern-based parsing)
```

---

## Architecture Overview

The project follows a layered backend design:

- **Data Layer** — JSON dataset + PostgreSQL storage (Render)
- **Repository Layer** — All SQL queries isolated in one place, decoupled from business logic
- **Parser Layer** — Extracts model, fuel type, and intent from user input
- **Service Layer** — Handles SQL queries and response building
- **Presentation Layer**
  - CLI for local usage
  - FastAPI for REST API access
  - HTML/CSS/JS frontend on GitHub Pages

---

## Data Pipeline

Data is loaded automatically on API startup:

1. **Extract** — Read raw data from JSON
2. **Transform** — Normalize structure and handle missing values
3. **Load** — Insert into PostgreSQL tables:
   - engines
   - best_engines
   - transmissions

---

## Key Improvements

- Refactored from single-file script to layered architecture
- Migrated from in-memory JSON to SQLite, then to PostgreSQL
- Extracted Repository layer — SQL queries separated from business logic
- Refactored parser into smart scope detection (model / series / family)
- Added unit test suite (pytest, 7/7) running without database dependency
- Added REST API using FastAPI
- Added support for "best engine" logic with reasoning
- Migrated to cloud: API on Render, database on Render PostgreSQL
- Built frontend (HTML/CSS/JS) hosted on GitHub Pages
- Implemented idempotent database seeding on startup

---

## Known Issues

- Parsing is rule-based and does not handle complex natural language
- No fuzzy matching or typo handling
- No logging or error tracking system

---

## Project Goals

- Learn backend architecture and separation of concerns
- Build a structured query system over real data
- Practice data transformation (JSON → SQL)
- Build and expose a REST API using FastAPI
- Deploy a full working application to the cloud
- Write testable, maintainable code with unit test coverage

---

## Status

**Live** — API deployed on Render, frontend on GitHub Pages. Unit tested (pytest 7/7)  
Next steps:
- Integration tests hitting live API endpoints (pytest + requests)
- Error logging to rotating file (Python logging module)
- Error reporting — structured log file with timestamp, endpoint, query, error type
- Frontend E2E tests (Playwright)
- GitHub Actions CI — run unit tests on every push
