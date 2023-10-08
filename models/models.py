from datetime import datetime
from typing import Optional

from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, JSON, Boolean
from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase


class Base(DeclarativeBase):
    pass


class Role(Base):
    __tablename__ = 'role'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    # permissions: Mapped[Optional[JSON]]

    # id = Column(Integer, primary_key=True)
    # name = Column(String, nullable=False)
    permissions = Column(JSON)


class User(Base):
    __tablename__ = 'user'

    # id: Mapped[int] = mapped_column(primary_key=True)
    # email: Mapped[str] = mapped_column(String(30), nullable=False)
    # username: Mapped[str] = mapped_column(String(30), nullable=False)
    # registered_at = Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, default=datetime.utcnow())
    #
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    username = Column(String, nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    role_id = Column(Integer, ForeignKey(Role.id))
    hashed_password: Mapped[str] = mapped_column(
        String(length=1024), nullable=False
    )
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )
    is_verified: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )
