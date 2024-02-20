from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/products",
                   tags= ["products"],
                   responses={404: {"message": "No encontrado"}})

list_products = ["Product 1", "Product 2", "Product 3", "Product 4", "Product 5"]

@router.get("/")
async def products():
    return list_products

@router.get("/{id}")
async def products(id: int):
    try:
        return list_products[id]
    except:
        raise HTTPException(status_code=404, detail="Item not found", headers={"404":"Item not found"})
    