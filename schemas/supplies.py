from pydantic import BaseModel, Field
from typing import Optional


class Supplies(BaseModel):
    id : Optional[int] = None
    supplier_id : int = Field(su = 1, description="ForegnKey of supplier")
    product_id : int = Field(pr = 1, description="ForeignKey of product")

    class Config:
        schema_extra = {
            "example":{
                "id":1,
                "supplier_id":2,
                "product_id":2
            }
        }