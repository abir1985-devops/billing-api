from datetime import datetime, timedelta
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.customer import Customer
from app.models.plan import Plan
from app.models.subscription import Subscription
from app.models.invoice import Invoice
from app.schemas.subscription import SubscriptionCreate, SubscriptionOut

router = APIRouter(prefix="/subscriptions", tags=["subscriptions"])


def add_30_days(dt: datetime) -> datetime:
    # For v1 we use 30 days instead of real calendar months (simple + stable).
    return dt + timedelta(days=30)


@router.post("", response_model=SubscriptionOut, status_code=status.HTTP_201_CREATED)
def create_subscription(payload: SubscriptionCreate, db: Session = Depends(get_db)):
    customer = db.query(Customer).filter(Customer.id == payload.customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")

    plan = db.query(Plan).filter(Plan.id == payload.plan_id).first()
    if not plan:
        raise HTTPException(status_code=404, detail="Plan not found")
    if not plan.is_active:
        raise HTTPException(status_code=400, detail="Plan is not active")

    # Business rule: one active subscription per customer
    existing_active = (
        db.query(Subscription)
        .filter(Subscription.customer_id == payload.customer_id, Subscription.status == "active")
        .first()
    )
    if existing_active:
        raise HTTPException(status_code=409, detail="Customer already has an active subscription")

    now = datetime.utcnow()
    period_start = now
    period_end = add_30_days(now)

    sub = Subscription(
        customer_id=payload.customer_id,
        plan_id=payload.plan_id,
        status="active",
        cancel_at_period_end=False,
        current_period_start=period_start,
        current_period_end=period_end,
    )
    db.add(sub)
    db.flush()  # gets sub.id without committing yet

    invoice = Invoice(
        customer_id=payload.customer_id,
        subscription_id=sub.id,
        period_start=period_start,
        period_end=period_end,
        amount_cents=plan.amount_cents,
        currency=plan.currency,
        status="open",
    )
    db.add(invoice)

    # One transaction for both subscription + invoice
    db.commit()
    db.refresh(sub)
    return sub


@router.get("/{subscription_id}", response_model=SubscriptionOut)
def get_subscription(subscription_id: UUID, db: Session = Depends(get_db)):
    sub = db.query(Subscription).filter(Subscription.id == subscription_id).first()
    if not sub:
        raise HTTPException(status_code=404, detail="Subscription not found")
    return sub
