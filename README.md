# Cars Data API (WIP)

## Overview

Simple backend-oriented project for querying BMW models, generations, engines and transmissions.

The goal of this project is to build a structured data system and gradually evolve it into a full backend application.

Development approach:
**MVP → API → Database → Deployment**

---

## Current Features

* Structured data stored in Python (dictionary-based)
* Currently supports: **BMW 3 Series**
* Data hierarchy:

  * Brand → Series → Generation → Engines / Transmission → Best Engine
* Query system via CLI (command line)
* Basic parsing of user input:

  * generation detection (e.g. "E90", "F30")
  * fuel type detection (petrol / diesel)
  * "best" engine detection

---

## Example Usage

```bash
python app.py
```

```
Ask: e90
→ returns engines for BMW E90

Ask: e90 petrol
→ returns petrol engines only

Ask: f30 best
→ returns best engine + transmission

Ask: bmw
→ returns available generations (planned improvement)
```

---

## Project Structure

```
cars.py      # data layer (BMW data)
parser.py    # user input parsing (model, fuel, intent)
service.py   # business logic (what to return)
app.py       # CLI interface (user interaction)
```

---

## Tech Stack

* Python
* (planned) FastAPI
* (planned) SQLite / PostgreSQL
* (planned) Docker

---

## In Progress

* Improving query understanding (parser logic)
* Better output formatting (more readable results)
* Smarter filtering (return only relevant data)

---

## Planned Features

* REST API using FastAPI
* Database integration (SQLite → PostgreSQL)
* Data ingestion (external APIs or scraping)
* Dockerization
* Possible frontend (future)

---

## ## Development Progress (Iterative & non-linear)

This project was developed in a non-linear way, with multiple refactors across layers, evolved iteratively as understanding of backend architecture improved over time.

### Step 1 — Monolithic script
- Initial version was a single Python file
- Data stored as simple strings
- No separation of logic


### Step 2 — Architecture separation
- Introduced separation of concerns:
  - app.py (user interface layer)
  - service.py (business logic layer)
  - parser.py (input interpretation layer)
  - cars.py (data layer)
  

### Step 3 — Input parsing system
- Added model detection (E21, E90, F30, etc.)
- Added fuel detection (petrol / diesel)
- Added intent detection ("best engine" queries)


### Step 4 — Data restructuring
- Converted engine data from strings → structured dictionaries
- Introduced hierarchical model (series → generation → engines)


### Step 5 — Ongoing improvements
- Improving parser accuracy (handling natural language inputs)
- Handling fallback cases (partial queries like "BMW 3 series")
- Improving output formatting and structure

---

## Project Goals

This project focuses on:

* Data structure design
* Backend architecture (layer separation)
* Query parsing logic (basic NLP approach)
* Iterative development and refactoring

---

## Known Issues

- Parser does not yet handle complex natural language queries
- Some queries return too broad results (needs better filtering)
- Output formatting is still CLI-based (not API yet)

---

## Status

Early stage — actively developed and improved step by step.

---

Self-taught backend learning project.
