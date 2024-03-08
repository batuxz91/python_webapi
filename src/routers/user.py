from fastapi import APIRouter
from db.models.user import User, UserDto
from db.client import connection
import json

router = APIRouter(tags=["users"], prefix="/user",
                   responses={404: {"message": "No encontrado"}})


@router.get("/all")
async def user():
    users_list = []

    query = 'select * from app_user'
    for row in connection.cursor().execute(query):
        users_list.append(User(
            id=row[0], name=row[1], surname=row[2], email=row[3], doc=row[4], typeDoc=row[5]))

    return users_list


@router.get("/{id}")
async def user(id: int):

    users_list = []
    found = False

    for row in connection.cursor().execute("select * from app_user where id=:id", id=id):
        users_list.append(User(
            id=row[0], name=row[1], surname=row[2], email=row[3], doc=row[4], typeDoc=row[5]))
        found = True

    if found:
        return users_list[0]
    else:
        return {"error": "usuario no encontrado"}


@router.post("/")
async def user(user: UserDto):
    for row in connection.cursor().execute("select app_user_seq.nextval from dual"):
        app_user_seq = row[0]

    app_user_new = [(1, int(app_user_seq)), (2, user.name), (3, user.surname),
                    (4, user.email), (5, user.doc), (6, int(user.typeDoc))]

    connection.cursor().executemany(
        "insert into app_user (id,name,surname,email,doc,doctype) values (:1,:2,:3,:4,:5,:6)", app_user_new)

    connection.commit()
    print(connection.cursor.rowcount, "Rows Inserted")

    # users_list = []
    # for row in connection.cursor().execute("select * from app_user where id=:id", id=app_user_seq):
    #     users_list.append(User(
    #         id=row[0], name=row[1], surname=row[2], email=row[3], doc=row[4], typeDoc=row[5]))

    return "OK"
