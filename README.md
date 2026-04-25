# BMW Data API (WIP)

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

## Project Goals

This project focuses on:

* Data structure design
* Backend architecture (layer separation)
* Query parsing logic (basic NLP approach)
* Iterative development and refactoring

---

## Status

Early stage — actively developed and improved step by step.

---

Self-taught backend learning project.
