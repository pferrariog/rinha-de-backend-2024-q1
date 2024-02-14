# from contextlib import AbstractContextManager
from db.engine import get_db_connection
from fastapi import Depends
from models.entities.customer_entity import Customer
from sqlalchemy import select
from sqlalchemy.orm import Session


class CustomerRepository:
    """Customer default operations"""

    def __init__(self, session: Session = Depends(get_db_connection)) -> None:
        """Initialize class variables"""
        self.session = session

    def get(self, id: int) -> ...:
        """Get customer by id"""
        try:
            return self.session.scalar(select(Customer).where(Customer.id == id))
        except Exception:
            raise
