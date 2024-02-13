from fastapi import FastAPI
from enum import Enum

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

# Order matters

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "current_user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {user_id: "user_id"}

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    
    return {"model_name": model_name, "message": "Have some residuals"}


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}

"""
la ruta /files/documentos/archivo.txt coincidiría con la ruta 
definida en @app.get("/files/{file_path:path}"), y la parte 
documentos/archivo.txt sería capturada como el valor del parámetro 
file_path. Luego, este valor se devuelve como una respuesta JSON 
que contiene la clave "file_path" y el valor "documentos/archivo.txt"
"""
