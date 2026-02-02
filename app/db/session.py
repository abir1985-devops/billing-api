import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is not set")

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def get_db():
    """
    FastAPI dependency that yields a DB session per request.
    Ensures the session is closed after the request finishes.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def db_ping() -> bool:
    """
    Simple connectivity check: runs 'SELECT 1'.
    Useful for verifying DB connection works.
    """
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
    return True
