from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    id: int
    first_name: str
    last_name: str
    age: int
    weight: float | None = None

user_list = [User(id=1, first_name="David", last_name="Campos", age=26, weight=1.75),
            User(id=2, first_name="Jose", last_name="Campos", age=24, weight=1.79),
            User(id=3, first_name="Enny", last_name="Galanton", age=27, weight=1.70)]

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

# Create
@app.post("/user/")
async def user(user: User):
    if type(search_user(user.id)) == User:
        return {"error": "El usuario ya existe"}
    user_list.append(user)
    return user


# Update
@app.put("/user/")
async def user(user: User):

    found = False

    for index, saved_user in enumerate(user_list):
        if saved_user.id == user.id:
            user_list[index] = user
            found = True
    
    if not found:
        return {"error": "No se ha encontrado el usuario"}

    return user

# Delete
@app.delete("/user/{id}")
async def user(id: int):
    found = False

    for index, saved_user in enumerate(user_list):
        if saved_user.id == id:
            del user_list[index]
            found = True
    
    if not found:
        return {"error": "No se ha eliminado el usuario"}
    
    return {"200": "Se ha eliminado el usuario"}


# Funcion para buscar id
def search_user(id: int):
    users = filter(lambda user: user.id == id, user_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el id solicitado"}

