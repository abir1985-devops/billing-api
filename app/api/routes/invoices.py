from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.invoice import Invoice
from app.schemas.invoice import InvoiceOut

router = APIRouter(prefix="/invoices", tags=["invoices"])


@router.get("", response_model=list[InvoiceOut])
def list_invoices(customer_id: UUID | None = None, limit: int = 20, offset: int = 0, db: Session = Depends(get_db)):
    limit = min(limit, 100)
    q = db.query(Invoice).order_by(Invoice.created_at.desc())
    if customer_id:
        q = q.filter(Invoice.customer_id == customer_id)
    return q.offset(offset).limit(limit).all()
