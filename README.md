# Cars Data API

## Overview

Cars Data API is a backend-oriented CLI project for querying BMW models, generations, engines, transmissions and performance data.

The project simulates how backend systems evolve from simple scripts into structured applications with data layers, query parsing and database storage.

Development approach
MVP → Structured Logic → JSON Dataset → SQLite Database → Service Layer → API (planned)

---

## Current Features

- Structured BMW dataset stored in JSON format (used as source of truth)
- SQLite database for runtime querying
- Multi-generation support from E21 to G20
- CLI-based query system
- Regex-based input parsing system
- Model detection (E21, E30, E46, E90, F30, G20 etc.)
- Fuel filtering (petrol, diesel, hybrid)
- Intent detection (best engine vs full dataset)
- Structured response formatting in CLI

---

## Example Usage

Ask: e90  
Returns full dataset for BMW E90

Ask: f30 petrol  
Returns petrol engines only

Ask: g20 best diesel  
Returns best diesel engine recommendation

Ask: bmw e46 engines  
Returns available engines for E46

---

## Project Structure

app.py        CLI interface and pretty output formatting  
service.py    business logic layer (query processing)  
carparser.py  regex-based query parsing (model, fuel, intent detection)  
cars.py       SQLite database connection layer  
datacars.json source dataset used for database seeding  
cars.db       SQLite database file  

---

## Tech Stack

Python  
SQLite  
JSON data source  
Regex-based parsing system  
CLI interface  

---

## Architecture Overview

The system follows a layered backend design:

- Data Layer → JSON source + SQLite storage
- Parser Layer → extracts intent, model, fuel from user input
- Service Layer → applies business logic and query rules
- Presentation Layer → CLI output formatting

---

## Data Pipeline

The project includes a simple ETL-like process:

1. Extract → JSON dataset
2. Transform → structured engine objects
3. Load → SQLite database

Database is rebuilt using a seed script with idempotent inserts and reset logic.

---

## Current Improvements

- Refactored from monolithic script to layered architecture
- Migrated from pure JSON logic to SQLite-backed storage
- Improved query parsing using regex patterns
- Added structured “best engine” reasoning field
- Implemented safe database seeding (INSERT OR IGNORE + reset)
- Improved CLI output formatting

---

## Development Approach

Step 1 Monolithic script
Single file with hardcoded string based data and no separation of logic

Step 2 Architecture separation
Split into app service parser and data layer

Step 3 Regex parsing system
Implemented detection for BMW models fuel types and query intent

Step 4 Data restructuring
Converted engine data from strings to structured objects including model engine power and reasoning

Step 5 Service refactor
Improved response structure fallback handling and output consistency

Step 6 — Database migration  
Introduced SQLite storage with reproducible seeding pipeline and query-ready structure

---

## Known Issues

## Known Issues

- Query parsing is still regex-based and does not handle complex natural language inputs
- Input is not fully normalized (spacing, typos, mixed formatting can break detection)
- No validation layer for user input before processing in service layer
- SQLite schema is not fully normalized (some redundancy in engine storage)
- CLI output formatting is basic and not structured for API responses yet
- No error handling layer separation (service returns mixed success/error dicts)
- No logging system for debugging queries and database operations

---

## Project Goals

- Learn backend architecture fundamentals
- Build structured query system over real dataset
- Practice parsing logic (light NLP approach)
- Simulate real-world backend evolution (script → database → API)
- Prepare foundation for FastAPI REST layer

---

## Status

Early-stage backend project evolving from CLI prototype into API-ready architecture.