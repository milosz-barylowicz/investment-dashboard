# ADR-002: Historical Data Storage Format and Strategy

**Status:** Accepted
**Date:** 2026-11-09

## Context

The application needs to store historical stock price data to avoid fetching the entire dataset from the external data provider every time the application is launched.

Initially, we expect to support a relatively small number of companies and local users. Therefore, a simple and lightweight storage solution should be sufficient for the MVP.

## Options Under Consideration

- A single **JSON** file containing data for all companies.
- A separate **JSON** file for each company.
- An **SQLite** database.
- A relational database, such as **PostgreSQL**.

## Decision

We will use a separate **JSON** file for each company. Each file will contain company metadata and an array of daily stock price observations.

## Example Structure

```json
{
    "schema_version": 1,
    "ticker": "CDR",
    "name": "CD Projekt S.A.",
    "currency": "PLN",
    "source": "yfinance",
    "last_updated": "2026-11-09T20:30:00Z",
    "history": [
        {
            "date": "2026-11-09",
            "open": 132.0,
            "high": 134.5,
            "low": 130.2,
            "close": 131.0,
            "volume": 125000
        }
    ]
}
```

## Consequences

- Simple implementation and easy integration with Python.
- Human-readable data format, making debugging and manual inspection easier.
- Each company's data can be managed independently.
- No need to configure or maintain a database server.
- Limited querying and filtering capabilities compared to relational databases.
- Potential performance limitations as the amount of historical data grows.
- Migration to SQLite or another database may be necessary as the application evolves.
