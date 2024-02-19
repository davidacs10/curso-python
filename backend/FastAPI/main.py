from fastapi import FastAPI
from routers import products, users

# Esta app es la misma a la que nos referimos cuando usamos el comando de uvicorn
app = FastAPI()

app.include_router(products.router)
app.include_router(users.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}

"""             EN RESUMEN
Importa FastAPI. # Linea 1
Crea un instance de app. # Linea 4
Escribe un decorador de operación de path (como @app.get("/")). # Linea 6
Escribe una función de la operación de path (como def root(): ... arriba). # Linea 7
Corre el servidor de desarrollo (como uvicorn main:app --reload). # Esto lo ejecutas en consola
"""