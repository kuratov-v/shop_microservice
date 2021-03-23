from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def get_products():
    return {}


@router.get("/{pk}")
async def get_product_detail(pk: str):
    return {}


@router.post("/")
async def create_product():
    return {}
