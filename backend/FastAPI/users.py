from fastapi import FastAPI
from pydantic import BaseModel

class Users(BaseModel):
    id: int
    first_name: str
    last_name: str
    age: int
    weight: float | None = None

user_list = [Users(id=1, first_name="David", last_name="Campos", age=26, weight=1.75),
            Users(id=2, first_name="Jose", last_name="Campos", age=24, weight=1.79),
            Users(id=3, first_name="Enny", last_name="Galanton", age=27, weight=1.70)]

app = FastAPI()

@app.get("/users")
async def create_user():
    return user_list

@app.get("/usersjson")
async def create_user_json():
    return [{"first_name": "David", "last_name": "Campos", "age": 26, "weight": 1.75},
            {"first_name": "Jose", "last_name": "Campos", "age": 24, "weight": 1.79},
            {"first_name": "Enny", "last_name": "Galanton", "age": 27, "weight": 1.70}]

@app.get("/user/{id}")
async def user(id: int):
    return search_user(id)

@app.get("/user/")
async def user(id: int):
    return search_user(id)

def search_user(id: int):
    users = filter(lambda user: user.id == id, user_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el id solicitado"}
