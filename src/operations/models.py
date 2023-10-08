from sqlalchemy import String, Column, TIMESTAMP
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped


class Base(DeclarativeBase):
    pass


class Operation(Base):
    __tablename__ = 'operation'

    id: Mapped[int] = mapped_column(primary_key=True)
    quantity: Mapped[str] = mapped_column(String)
    figi: Mapped[str] = mapped_column(String)
    instrument_type: Mapped[str] = mapped_column(String, nullable=False)
    date = Column(TIMESTAMP)
    type: Mapped[str] = mapped_column(String)