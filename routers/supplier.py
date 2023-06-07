from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from schemas.supplier import Supplier as SupplierSchemas
from service.supplier import SupplierService
from config.database import Session


supplier_router = APIRouter()

@supplier_router.get('/get_suppliers', tags=['Supplier'], status_code=200)
def get_supplier():
    db = Session()
    result = SupplierService(db).get_supplier()
    return JSONResponse(content=jsonable_encoder(result), status_code=200)


@supplier_router.get('/get_supplier_for_id', tags=['Supplier'],status_code=200)
def get_supplier_for_id(id:int):
    db = Session()
    result = SupplierService(db).get_supplier_for_id(id)
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@supplier_router.post('/created_supplier', tags=['Supplier'],status_code=201)
def post_supplier(supplier:SupplierSchemas):
    db = Session()
    SupplierService(db).create_supplier(supplier)
    return JSONResponse(content={'message':'Supplier created sucessfull', 'status_code':200})


@supplier_router.put('/update_supplier', tags=['Supplier'])
def update_supplier(id:int, supplier:SupplierSchemas):
    db = Session()
    result = SupplierService(db).get_supplier_for_id(id)
    if not result:
        return JSONResponse(content={'message':'Supplier don´t gound','status_code':404})
    SupplierService(db).update_supplier(supplier)
    return JSONResponse(content={'message':'supplier update succesfull','status_code':202},status_code=200)


@supplier_router.delete('/Delete_dupplier', tags=['Supplier'])
def delete_supplier(id:int):
    db = Session()
    result = SupplierService(db).delete_supplier(id)
    if not result:
        return JSONResponse(content={'message':'supplier delete succesfull','status_code':200},status_code=200)
    








    #el commit
    