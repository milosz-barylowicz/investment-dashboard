# ADR-003: Historical Data Update Strategy

**Status:** Accepted
**Date:** 2026-11-09

## Context

Downloading the entire historical dataset every time the application is launched would result in unnecessary data transfers and increased loading times.

At the same time, we need to account for the possibility of historical data corrections made by the data provider.

## Options Under Consideration

- Downloading the full historical dataset on every application launch.
- Downloading only new stock price observations.
- A hybrid strategy combining incremental updates with periodic full-history synchronization.

## Decision

We will use a hybrid update strategy.

1. If no historical data is available, we will download the full 12-month historical dataset.
2. During standard updates, we will download data starting from the last stored trading date, including a small overlapping time window.
3. Periodically, we will re-fetch the full historical dataset to account for potential corrections made by the data provider.
4. We will merge the downloaded data based on trading dates, updating existing records instead of creating duplicates.
5. In case of a download error, we will retain the previously stored data.

## Consequences

- Reduced data transfer during standard updates.
- Shorter application loading and update times.
- Ability to incorporate historical data corrections.
- Greater synchronization complexity compared to simply downloading the entire dataset.
- The need to handle duplicate records, missing trading sessions, and file-writing errors.

The frequency of full-history synchronization will be configurable and determined during implementation.
