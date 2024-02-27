from fastapi import APIRouter, HTTPException, status
from db.models.user import User
from db.schemas.user import user_schema, users_schema
from db.client import db_client
from bson import ObjectId


router = APIRouter(prefix="/usersdb", 
                   tags= ["usersdb"], 
                   responses= {status.HTTP_404_NOT_FOUND:{"message":"No encontrado"}})

@router.get("/", response_model=list[User])
async def get_users():
   return users_schema(db_client.users.find())

@router.get("/{id}")
async def user(id: str):
    return search_user("_id", ObjectId(id))

@router.get("/")
async def user(id: str):
    return search_user("_id", ObjectId(id))

# Create
@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def user(user: User):
    if type(search_user("email",user.email)) == User:
        raise HTTPException(status_code=409, detail="El usuario ya existe.")

    user_dict = dict(user)
    del user_dict["id"]

    id = db_client.users.insert_one(user_dict).inserted_id

    new_user = user_schema(db_client.users.find_one({"_id":id}))

    return User(**new_user)

# Update
@router.put("/", response_model=User)
async def user(user: User):

    user_dict = dict(user)
    del user_dict["id"]

    try:
        db_client.users.find_one_and_replace({"_id": ObjectId(user.id)}, user_dict)
    except:
        raise HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
                      detail="No se ha actualizado el usuario",
                      headers={"405": "No actualizado"})
        
    return search_user("_id", ObjectId(user.id))

# Delete
@router.delete("/{id}")
async def user(id: str):
    found = db_client.users.find_one_and_delete({"_id": ObjectId(id)})
    
    if not found:
        raise HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED, 
                            detail="El usuario no existe", 
                            headers={"405": "El usuario no existe"})
    
    raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, 
                            headers={"204": "Usuario eliminado con exito"})


# Funcion para buscar email
def search_user(field: str, key):
    try:
        user = db_client.users.find_one({field:key})
        if user:
            return User(**user_schema(user))
        else:
            return None
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500, detail=f"Error searching user: {e}")