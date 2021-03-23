from fastapi import APIRouter, Body, Request, Query
from product.managers import ProductManager

from product.schemas import Product

router = APIRouter()


@router.get("/")
async def get_products(request: Request, name: str = Query(None), params=Query(None)):
    response = await ProductManager(request.app.mongodb["products"]).get_products(name, params)
    return response


@router.get("/{pk}")
async def get_product_detail(pk: str, request: Request):
    response = await ProductManager(request.app.mongodb["products"]).get_product_detail(pk)
    return response


@router.post("/")
async def create_product(request: Request, product: Product = Body(...)):
    response = await ProductManager(request.app.mongodb["products"]).create_product(product)
    return response
