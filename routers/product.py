from fastapi import APIRouter, Body, Request, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from schemas import Product

router = APIRouter()


@router.get("/")
async def get_products(request: Request):
    products = await request.app.mongodb["products"].find().to_list(length=None)
    return products


@router.get("/{pk}")
async def get_product_detail(pk: str, request: Request):
    product = await request.app.mongodb["products"].find_one({"_id": pk})
    if product is not None:
        return product
    raise HTTPException(status_code=404, detail=f"Product with _id={pk} not found")


@router.post("/")
async def create_product(request: Request, product: Product = Body(...)):
    product = jsonable_encoder(product)
    await request.app.mongodb["products"].insert_one(product)
    return JSONResponse(
        status_code=status.HTTP_201_CREATED, content={"status": "created"}
    )
