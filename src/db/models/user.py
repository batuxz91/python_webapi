from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    surname: str
    email: str
    doc: str
    typeDoc: int


class UserDto(BaseModel):
    name: str
    surname: str
    email: str
    doc: str
    typeDoc: int
