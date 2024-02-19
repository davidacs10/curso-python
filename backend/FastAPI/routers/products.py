from fastapi import APIRouter

router = APIRouter(prefix="/products",
                   tags= ["products"],
                   responses={404: {"message": "No encontrado"}})

list_products = ["Product 1", "Product 2", "Product 3", "Product 4", "Product 5"]

@router.get("/{products}")
async def products():
    return list_products

@router.get("/{id}")
async def products(id: int):
    return list_products[id]