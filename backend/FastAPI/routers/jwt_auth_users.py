from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta

router = APIRouter(prefix="/jwtauth",
                   tags=["jwtauth"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})

ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 1
SECRET = "320e85372b2ea9636a2d84f395d54da6ccdea7bedbae04e71a0bf21270ce1847"
crypt = CryptContext(schemes=["bcrypt"])

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool

class UserDB(User):
    password: str

users_db = {
    "david2010":{
        "username": "david2010", 
        "full_name": "David Campos",
        "email": "david@campos.com",
        "disabled": False,
        "password": "$2a$12$aYad9AxyvEKBKwB0Tae9z.f4XG429yzf5.HbUToUkpKgIG00l2PZe"
    },
        "david2011":{
        "username": "david2011", 
        "full_name": "David Gonzalez",
        "email": "david@thebest.com",
        "disabled": True,
        "password": "$2a$12$Nziji1SELrvNw7CQiE2EC.gVlvAbBU9Yz9EUiW5HM8pUhzG8apr4C"
    }
}

def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])
    
def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])
    
async def auth_user(token: str = Depends(oauth2)):

    exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                              detail="Credenciales de autenticacion invalidas", 
                              headers={"WWW-Authenticate": "Bearer"})

    try:
        username = jwt.decode(token, SECRET, ALGORITHM).get("sub")
        if username is None:
            raise exception

    except JWTError:
        raise exception
    
    return search_user(username)

async def current_user(user: User = Depends(auth_user)):
    if user.disabled:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail="Usuario inactivo",
                            headers={"WWW-Authenticate": "Bearer"})        
    return user
    
@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail="El usuario no es correcto")
    
    user = search_user_db(form.username)

    if not crypt.verify(form.password, user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail="La contraseña no es correcta")
    
    access_token = {"sub": user.username,
                    "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION)}
    
    return {"access_token": jwt.encode(access_token, SECRET, algorithm=ALGORITHM), "token_type": "bearer"}

@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user