# Cars Data API

## Overview

Cars Data API is a backend oriented CLI project for querying BMW models, generations, engines, transmissions and performance data.

The project focuses on building a clean data structure and query engine and simulating how backend systems evolve from simple scripts into scalable applications.

Development approach
MVP -> Structured Logic -> API Layer -> Database -> Deployment

## Current Features

- Structured BMW dataset stored in JSON format
- Multi generation support from E21 to G20
- CLI query system
- Regex based input parsing
- Filtering by model generation such as E90 F30
- Filtering by fuel type petrol diesel hybrid
- Intent detection best engine or full dataset

## Example Usage

Ask e90
returns full dataset for BMW E90

Ask f30 petrol
returns petrol engines only

Ask g20 best diesel
returns best diesel engine recommendation

Ask bmw e46 engines
returns available engines for E46

## Project Structure

cars.py        JSON data loader BMW dataset
carparser.py   regex based query parsing
service.py     business logic layer
app.py         CLI interface and output formatting
datacars.json  structured dataset

## Tech Stack

Python
JSON data storage
Regex query parsing
CLI interface

## Current Improvements

Refactored data model from strings to structured JSON objects
Introduced reasoning field for best engine recommendations
Improved separation of concerns between parser service data and UI
Implemented structured CLI output formatting
Improved fallback and error handling in service layer

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

## Known Issues

Parser is not fully robust for noisy natural language input
Some queries return broader results than expected
CLI output formatting is minimal

## Project Goals

Learn backend architecture fundamentals
Build structured data querying system
Practice parsing logic and lightweight NLP approach
Simulate real backend development workflow
Prepare for FastAPI and database integration

## Status

Early stage backend project evolving from CLI prototype toward API ready architecture