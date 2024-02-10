from fastapi import FastAPI
from pydantic import BaseModel

class Users(BaseModel):
    first_name: str
    last_name: str
    age: int
    weight: float | None = None

user_list = [Users(first_name="David", last_name="Campos", age=26, weight=1.75),
            Users(first_name="Jose", last_name="Campos", age=24, weight=1.79),
            Users(first_name="Enny", last_name="Galanton", age=27, weight=1.70)]

app = FastAPI()

@app.get("/users")
async def create_user():
    return user_list

@app.get("/usersjson")
async def create_user_json():
    return [{"first_name": "David", "last_name": "Campos", "age": 26, "weight": 1.75},
            {"first_name": "Jose", "last_name": "Campos", "age": 24, "weight": 1.79},
            {"first_name": "Enny", "last_name": "Galanton", "age": 27, "weight": 1.70}]


