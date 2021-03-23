from pydantic import BaseModel, Field
import uuid


class Product(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str
    description: str
    params: dict
