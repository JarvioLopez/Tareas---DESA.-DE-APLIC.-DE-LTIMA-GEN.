from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Person(Base):
    __tablename__ = "Person"
    __table_args__ = {"schema": "Person"}

    BusinessEntityID: Mapped[int] = mapped_column(
        Integer, primary_key=True
    )
    FirstName: Mapped[str] = mapped_column(String(50))
    LastName: Mapped[str] = mapped_column(String(50))
