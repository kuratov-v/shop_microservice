from pydantic import BaseModel, Field
import uuid


class Product(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str
    description: str
    params: dict

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "name": "Product name",
                "description": "Description for product",
                "params": {"param1": "value1", "param2": "value2"},
            }
        }
