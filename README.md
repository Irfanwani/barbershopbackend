# Archived

This repository is **archived and no longer maintained.** The code still works
as a Django project, but nothing has been changed here since April 2023.

## Where it went

Everything now lives in one repository:

**https://github.com/Irfanwani/barbershop**

| This repository | Now |
| --- | --- |
| `accounts/`, `haircut/` | `services/api/accounts/`, `services/api/providers/` |
| `barbershop/` | `services/api/bookings/`, `services/api/payments/` |
| `manage.py` | `services/api/manage.py` |

The git history of this repository was preserved when the backend moved, so
`git log` on `services/api` still reaches back to the first commit.

## Why it was replaced

The old schema and the two apps that used it had problems that could not be
fixed in place:

- A "user" existed in two places. The customer app and the provider app each
  had their own idea of who someone was, and a booking only worked if you got
  lucky.
- Prices were stored after a 10% commission had already been added, and a
  further 10% was applied when they were read. The number in the database was
  neither the shelf price nor the charged price.
- Appointments had no lifecycle. `paid` was a boolean, cancelling deleted the
  row, so there was no record that a cancellation had ever happened.
- Booking a slot compared a rounded-tripped timestamp string against a head
  count inside a bare `except`, which meant any error in the comparison meant
  "always allow" — double-booking by default.

## What changed

- One API under `/api/v1/`, one app.
- Prices are the provider's own, and the platform fee is applied once, at the
  edge.
- Bookings have an explicit lifecycle with a terminal state.
- Exact shop coordinates are never returned to another user.

See the [architecture notes](https://github.com/Irfanwani/barbershop/blob/main/docs/ARCHITECTURE.md)
and [the migration guide](https://github.com/Irfanwani/barbershop/blob/main/docs/MIGRATION.md),
which covers moving production data across.

## Licensing

This repository keeps whatever licence it had. If there was not one, that is a
gap worth closing before anything from here is reused.
