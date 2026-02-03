from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field


class SubscriptionCreate(BaseModel):
    customer_id: UUID
    plan_id: UUID


class SubscriptionOut(BaseModel):
    id: UUID
    customer_id: UUID
    plan_id: UUID
    status: str
    cancel_at_period_end: bool
    current_period_start: datetime
    current_period_end: datetime

    class Config:
        from_attributes = True
