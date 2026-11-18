# Noor Foods API

An API for Noor Foods products, orders and stock, built with FastAPI and
SQLModel on the Noor Foods Postgres database.

## Requirements

- [uv](https://docs.astral.sh/uv/) and Python 3.14
- The `noor-foods-db` database running in Docker on port 5433:

  ```
  cd ~/projects/noor-foods-db
  docker compose up -d --wait
  ```

## Settings

Settings come from environment variables or a `.env` file
(`src/noor_foods_api/config.py`).

| Variable       | Default                                                            |
| -------------- | ------------------------------------------------------------------ |
| `DATABASE_URL` | `postgresql+psycopg://postgres:postgres@localhost:5433/noor_foods` |

## Run

```
uv run fastapi dev
```

Open http://127.0.0.1:8000 (returns `{"app": "Noor Foods API", "docs": "/docs"}`)
and http://127.0.0.1:8000/docs.

## Check the database connection

```
uv run python
>>> from sqlalchemy import text
>>> from noor_foods_api.database import get_engine
>>> with get_engine().connect() as conn:
...     conn.execute(text("SELECT count(*) FROM orders")).scalar()
...
200000
```

## Project layout

- `src/noor_foods_api/config.py`: settings, read once and cached
- `src/noor_foods_api/database.py`: the cached engine and a session per request
- `src/noor_foods_api/main.py`: the FastAPI app and `GET /`
