from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import HTTPException, status

from product.schemas import Product
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

import json


class ProductManager:
    def __init__(self, _mongodb: AsyncIOMotorClient):
        self.mongodb = _mongodb

    async def get_products(self, name: str = None, params: str = None):
        search_filter = {}
        if name is not None:
            search_filter['name'] = name
        if params is not None:
            params = json.loads(params)
            for key, value in params.items():
                search_filter['params.' + key] = value
        query_products = await self.mongodb.find(search_filter).to_list(length=None)
        return query_products

    async def get_product_detail(self, pk: str):
        product = await self.mongodb.find_one({"_id": pk})
        if product is not None:
            return product
        raise HTTPException(status_code=404, detail=f"Product with _id={pk} not found")

    async def create_product(self, product: Product):
        product = jsonable_encoder(product)
        new_product = await self.mongodb.insert_one(product)
        created_product = await self.mongodb.find_one(
            {"_id": new_product.inserted_id}
        )
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_product)
