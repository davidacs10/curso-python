from fastapi import APIRouter, HTTPException
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

router = APIRouter(prefix="/users", 
                   tags= ["users"], 
                   responses= {404:{"message":"No encontrado"}})

@router.get("/")
async def create_user():
    return user_list

@router.get("/usersjson")
async def create_user_json():
    return [{"first_name": "David", "last_name": "Campos", "age": 26, "weight": 1.75},
            {"first_name": "Jose", "last_name": "Campos", "age": 24, "weight": 1.79},
            {"first_name": "Enny", "last_name": "Galanton", "age": 27, "weight": 1.70}]

@router.get("/user/{id}")
async def user(id: int):
        return search_user(id)

@router.get("/user/")
async def user(id: int):
    return search_user(id)

# Create
@router.post("/user/", status_code=201, response_model=User)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=409, detail="El usuario ya existe.")
    user_list.append(user)
    return user


# Update
@router.put("/user/")
async def user(user: User):

    found = False

    for index, saved_user in enumerate(user_list):
        if saved_user.id == user.id:
            user_list[index] = user
            found = True
    
    if not found:
        raise HTTPException(status_code=304, 
                            detail={"Error":"No se ha encontrado el usuario"}, 
                            headers={"304":"Usuario no encontrado"})

    return user

# Delete
@router.delete("/user/{id}")
async def user(id: int):
    found = False

    for index, saved_user in enumerate(user_list):
        if saved_user.id == id:
            del user_list[index]
            found = True
    
    if not found:
        raise HTTPException(status_code=405, 
                            detail="El usuario no existe", 
                            headers={"405": "El usuario no existe"})
    
    raise HTTPException(status_code=200, 
                            detail="Usuario eliminado con exito", 
                            headers={"200": "Usuario eliminado con exito"})


# Funcion para buscar id
def search_user(id: int):
    users = filter(lambda user: user.id == id, user_list)
    try:
        return list(users)[0]
    except:
        raise HTTPException(status_code=404, 
                            detail="User not found", 
                            headers={"404": "User not found"})

