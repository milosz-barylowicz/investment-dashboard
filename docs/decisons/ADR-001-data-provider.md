# ADR-001: Stock Market Data Provider Selection

**Status:** Accepted
**Date:** 2026-11-09

## Context

The application requires access to historical stock market data for companies listed on the Warsaw Stock Exchange (GPW). We need a data provider that allows us to build and test the MVP quickly, without spending too much time on integration and API configuration.

## Options Under Consideration

- Yahoo Finance using the `yfinance` Python library
- Other stock market data providers, such as the XTB API
- Direct data sources provided by the Warsaw Stock Exchange (GPW)

## Decision

For the MVP, we will use **Yahoo Finance through the `yfinance` library**.

## Consequences

- Faster initial development and integration.
- No need to manage API keys or a dedicated API subscription for basic access.
- Dependency on an unofficial interface to Yahoo Finance.
- Potential limitations in data availability, reliability, and API compatibility.
- We may need to switch to another data provider as the application evolves.
