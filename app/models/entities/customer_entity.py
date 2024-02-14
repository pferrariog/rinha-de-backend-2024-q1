from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    """SQLAlchemy base model"""

    pass


class Customer(Base):
    """Customer table fields"""

    __tablename__ = "customer"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    limit: Mapped[int]
    balance: Mapped[int]
