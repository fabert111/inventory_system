from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from schemas.supplies import Supplies as SuppliesSchemas
from service.supplies import SuppliesService
from config.database import Session


supplies_router = APIRouter()


@supplies_router.get('/get_supplies', tags=['Supplies'], status_code=200)
def get_supplies():
    db = Session()
    result = SuppliesService(db).get_supplies()
    return JSONResponse(content=jsonable_encoder(result), status_code=200)


@supplies_router.post('/create_supplies', tags=['Supplies'], status_code=200)
def create_supplies(supplies:SuppliesSchemas):
    db = Session()
    SuppliesService(db).create_supplies(supplies)
    return JSONResponse(content={'message':'Created supplies succesfull','status_code':200})
    

@supplies_router.get('/get_supplies_for_id', tags=['Supplies'],status_code=200)
def get_supplies_for_id(id:int):
    db = Session()
    result = SuppliesService(db).get_supplies_for_id(id)
    return JSONResponse(content=jsonable_encoder(result), status_code=200)


@supplies_router.put('/Update_supplies', tags=['Supplies'])
def Update_supplies(id:int,supplies:SuppliesSchemas):
    db = Session()
    result = SuppliesService(db).get_supplies_for_id(id)
    if not result:
        return JSONResponse(content={'message':'supplies don´t gound', 'status_code':404})
    SuppliesService(db).update_supplies(supplies)
    return JSONResponse(content={'message':'Update supplies succesfull','status_code':202},status_code=200)


@supplies_router.delete('/Delete_supplies',tags=['Supplies'])
def delete_supplies(id:int):
    db = Session()
    result = SuppliesService(db).get_supplies_for_id(id)
    if not result:
        return JSONResponse(content={'message':'Supplies don´t gound','status_code':404})
    SuppliesService(db).delete_supplies(id)
    return JSONResponse(content={'message':'supplies delete succesfull','status_code':200},status_code=200)