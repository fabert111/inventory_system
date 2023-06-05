from pydantic import BaseModel, Field
from typing import Optional


class Product(BaseModel):
    id : Optional[int] = None
    name : str = Field(max_length=200, min_length=3, description="Name of product")
    brand : str = Field(max_length=200,min_length=3, description="Name of brand")
    description : str = Field(max_length=400, min_length=10, description="Description of product")
    price : float = Field(description="Price of producto")
    entry_date : str = Field(max_length=15, min_length=10, description="entry date of producto")
    availability : str = Field(max_length=2,min_length=1,description="Writer the letter Y for yes and the letter N for no")
    available_quantity : int = Field(description="available quantity of producto")

    class Config:
        schema_extra = {
            "example":{
                "id":1,
                "name": "Rice",
                "brand":"Diana",
                "description":"rice of Colombia",
                "price":1250,
                "entry_date":"05-08-2022",
                "availability":"Y",
                "available_quantity":10
            }
        }