from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class InvoiceOut(BaseModel):
    id: UUID
    customer_id: UUID
    subscription_id: UUID
    period_start: datetime
    period_end: datetime
    amount_cents: int
    currency: str
    status: str

    class Config:
        from_attributes = True
