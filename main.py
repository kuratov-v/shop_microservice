from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

from product.routers import router as product_router

import config

app = FastAPI()

app.include_router(product_router, prefix="/api/product")


@app.on_event("startup")
async def startup_db_client():
    app.mongodb_client = AsyncIOMotorClient(config.MONGODB_URL)
    app.mongodb = app.mongodb_client[config.DB_NAME]


@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongodb_client.close()
