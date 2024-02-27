from fastapi import APIRouter, HTTPException, status
from db.models.user import User
from db.schemas.user import user_schema
from db.client import db_client


user_list = []

router = APIRouter(prefix="/usersdb", 
                   tags= ["usersdb"], 
                   responses= {status.HTTP_404_NOT_FOUND:{"message":"No encontrado"}})

@router.get("/")
async def get_users():
    return db_client.users.find()

@router.get("{id}")
async def user(id: int):
        return search_user(id)

@router.get("/")
async def user(id: int):
    return search_user(id)

# Create
@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def user(user: User):
    if type(search_user_by_email(user.email)) == User:
        raise HTTPException(status_code=409, detail="El usuario ya existe.")

    user_dict = dict(user)
    del user_dict["id"]

    id = db_client.users.insert_one(user_dict).inserted_id

    new_user = user_schema(db_client.users.find_one({"_id":id}))

    return User(**new_user)

# Update
@router.put("/")
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
@router.delete("/{id}")
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


# Funcion para buscar email
def search_user_by_email(email: str):
    try:
        user = db_client.users.find_one({"email":email})
        return User(**user_schema(user))
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="User not found", 
                            headers={"404": "User not found"})

async def search_user():
    pass