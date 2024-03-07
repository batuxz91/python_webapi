from fastapi import APIRouter
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    surname: str
    email: str
    doc: str
    typeDoc: int


router = APIRouter(tags=["users"], prefix="/user",
                   responses={404: {"message": "No encontrado"}})

users_list = [User(id=1, name="Cesar", surname="Maydana", email="maydanacesar@gmail.com", doc="32091981", typeDoc="1"),
              User(id=2, name="Leonardo", surname="Maydana", email="maydanaleo@gmail.com", doc="32091980", typeDoc="1")]


@router.get("/{id}")
async def user(id: int):
    return search_user(id)


@router.post("/")
async def user(user: User):
    if type(search_user(user.id)) == User:
        return {"error": "El usuario ya existe"}
    else:
        users_list.append(user)
        return user


@router.put("/")
async def user(user: User):

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True

    if not found:
        return {"error": "No se encontro el usuario"}
    else:
        return search_user(user.id)


def search_user(id: int):
    user = filter(lambda user: user.id == id, users_list)
    try:
        return list(user)[0]
    except:
        return {"error": "No se encontro el usuario"}
