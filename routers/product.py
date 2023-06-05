from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from service.product import ProducService
from schemas.product import Product as ProductSchema
from config.database import Session

product_router = APIRouter()

@product_router.get('/products', tags=['products'], status_code=200)
def get_product():
    db = Session()
    result = ProducService(db).get_product()
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@product_router.get('/product_for_id', tags=['products'], status_code=200)
def get_product_for_id(id:int):
    db = Session()
    result = ProducService(db).get_product_for_id(id)
    return JSONResponse(content=jsonable_encoder(result), status_code=200)


@product_router.post('/Create_products', tags=['products'], status_code=201)
def create_product(products:ProductSchema):
    db = Session()
    ProducService(db).create_product(products)
    return JSONResponse(content={'message':'Product created sucessfull','status_code':200})


@product_router.put('/Update_product{id}', tags=['products'])
def update_product(id:int, product:ProductSchema):
    db = Session()
    result = ProducService(db).get_product_for_id(id)
    if not result:
        return JSONResponse(content={'message':'product don´t gound','status_code':404})
    ProducService(db).update_product(product)
    return JSONResponse(content={'message':'product update sucessful','status_code':202}, status_code=200)

@product_router.delete('/Delete_product{id}', tags=['products'])
def delete_product(id:int):
    db = Session()
    result = ProducService(db).get_product_for_id(id)
    if not result:
        return JSONResponse(content={'message':'product dong´t gound','status_code':404})
    ProducService(db).delete_product(id)
    return JSONResponse(content={'message':'product delete sucessfull','status_code':200},status_code=200)