from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


# IMPORTANT:
# Import models here so Alembic can discover them
from app.models.customer import Customer  # noqa: E402,F401
from app.models.plan import Plan  # noqa: E402,F401
