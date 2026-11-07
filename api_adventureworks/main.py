from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import get_db
from models import Person
from schemas import PersonOut

app = FastAPI(
    title="AdventureWorks API",
    version="1.0.0",
    description="API académica para consultar Person.Person",
)

DbSession = Annotated[Session, Depends(get_db)]


@app.get("/health")
def health():
    return {"status": "ok", "api": "AdventureWorks API activa"}


@app.get("/persons", response_model=list[PersonOut])
def read_persons(
    db: DbSession,
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=10, ge=1, le=50),
    last_name: str | None = Query(default=None),
):
    stmt = select(Person).order_by(Person.BusinessEntityID)
    if last_name:
        stmt = stmt.where(Person.LastName.ilike(f"%{last_name}%"))
    stmt = stmt.offset(skip).limit(limit)
    return db.scalars(stmt).all()


@app.get("/persons/{person_id}", response_model=PersonOut)
def read_person(person_id: int, db: DbSession):
    person = db.get(Person, person_id)
    if person is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Persona no encontrada",
        )
    return person
