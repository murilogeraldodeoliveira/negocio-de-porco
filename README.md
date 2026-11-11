# Negócio de Porco — Business Marketplace API

## Project Overview

Negócio de Porco is an independently developed marketplace backend designed to connect businesses across different cities, regions, and states in Brazil.

The project is being developed in Python using FastAPI, SQLAlchemy, and SQLite.

Its long-term goal is to provide a platform where businesses can advertise products and services and connect with potential customers.

## Technology Stack

- Python 3
- FastAPI — REST API development
- SQLAlchemy — Database ORM
- SQLite — Local database
- Pydantic — Data validation
- Uvicorn — ASGI server
- Swagger UI — Interactive API documentation

## Current Features

The API currently provides endpoints for:

- Registering businesses
- Listing registered businesses
- Retrieving businesses by ID
- Updating business information
- Deleting business records
- Checking for duplicate CNPJ registrations

Business records include contact details and geographic information such as state, region, and city.

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | API health message |
| GET | /empresas | List businesses |
| POST | /empresas | Register a business |
| GET | /empresas/{empresa_id} | Retrieve a business |
| PUT | /empresas/{empresa_id} | Update a business |
| DELETE | /empresas/{empresa_id} | Delete a business |

## Running Locally

Install the required dependencies:

```bash
pip install fastapi uvicorn sqlalchemy pydantic
```

Start the development server from the project root:

```bash
python -m uvicorn app.main:app --reload
```

Open the interactive API documentation:

http://127.0.0.1:8000/docs

## Project Status

This project is under active development.

The current version focuses on backend architecture and business registration management.

## Planned Improvements

- Product and service listings
- Geographic search and filtering
- User authentication
- Improved data validation
- Automated API testing
- Database migrations
- Frontend integration

## Development Approach

The project is being developed incrementally, focusing on maintainable code, practical functionality, and continuous improvement.

AI-assisted coding tools may be used to support implementation, debugging, testing, and code review.

## Ownership

This is an independently developed software project.