from fastapi import FastAPI
from app.db.session import db_ping
from app.api.routes.subscriptions import router as subscriptions_router
from app.api.routes.invoices import router as invoices_router
from prometheus_fastapi_instrumentator import Instrumentator
app = FastAPI(title="Billing API", version="0.1.0")
Instrumentator().instrument(app).expose(app)

@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/health/db")
def health_db():
    db_ping()
    return {"database": "ok"}

app.include_router(subscriptions_router)
app.include_router(invoices_router)
