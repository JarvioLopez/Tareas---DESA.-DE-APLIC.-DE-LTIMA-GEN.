from pydantic import BaseModel, ConfigDict


class PersonOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    BusinessEntityID: int
    FirstName: str
    LastName: str
