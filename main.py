from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

from product.routers import router as product_router

app = FastAPI()

app.include_router(product_router, prefix="/api/product")


@app.on_event("startup")
async def startup_db_client():
    app.mongodb_client = AsyncIOMotorClient("mongodb://localhost:27017")
    app.mongodb = app.mongodb_client["product"]


@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongodb_client.close()
