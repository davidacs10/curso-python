from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}, 
                 {"item_name": "Foo2"}, {"item_name": "Bar2"}, {"item_name": "Baz2"}, 
                 {"item_name": "Foo3"}, {"item_name": "Bar3"}, {"item_name": "Baz3"}, ]

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

### http://127.0.0.1:8000/items/?skip=0&limit=9


# Parametros opcionales
@app.get("/optional_items/{item_id}")
async def read_item(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

### http://127.0.0.1:8000/optional_items/un_item?q=test

# Conversion de tipo de parametro
@app.get("/items_conversion_parameter/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

### http://127.0.0.1:8000/items_conversion_parameter/1008?q=test

#Multiples path y parametros query
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: str | None = None, short: bool = False
    ):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "This is an amazing item that has a long description"})
    return item

### http://127.0.0.1:8000/users/100897/items/fastapi?q=test

# Parametros query requeridos
@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy":needy}
    return item

### http://127.0.0.1:8000/items/foo-item?needy=sooooneedy

# Query con los 3 tipos de parametros (Requeridos, predeterminados, opcionales)
@app.get("/items_with_all_parameters/{item_id}")
async def read_user_item(item_id: str, needy: str, skip: int = 0, limit: int| None = None):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item

### http://127.0.0.1:8000/items_with_all_parameters/foo-item?needy=sooooneedy&skip=10&limit=1000



