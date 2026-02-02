from fastapi import FastAPI
from app.db.session import db_ping

app = FastAPI(title="Billing API", version="0.1.0")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/health/db")
def health_db():
    db_ping()
    return {"database": "ok"}

