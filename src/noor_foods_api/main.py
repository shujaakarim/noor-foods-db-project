from fastapi import FastAPI

app = FastAPI(
    title="Noor Foods API",
    description="Products, orders and stock for Noor Foods.",
)


@app.get("/")
def root() -> dict[str, str]:
    return {"app": "Noor Foods API", "docs": "/docs"}
