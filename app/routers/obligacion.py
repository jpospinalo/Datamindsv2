from fastapi import FastAPI, APIRouter, HTTPException
from typing import List
from schemas.esquemas import ObligacionIn, ObligacionOut
from services.crud_obligacion import get_all_obligacion, get_obligacion_by_id, create_obligacion, delete_obligacion, update_obligacion

router_obligacion = APIRouter()

@router_obligacion.get("/obligacion/", response_model=List[ObligacionOut], tags=['Obligacion'])
async def read_all_obligacion():
    """
    Obtener todos las obligaciones de la base de datos.
    Retorna una lista de las obligaciones.
    """
    obligaciones = get_all_obligacion()
    if not obligaciones:
        raise HTTPException(status_code=404, detail="Obligacion not found")
    return obligaciones

@router_obligacion.get("/obligacion/{id_obligacion}", response_model=ObligacionOut, tags=['Obligacion'])
async def read_obligacion_by_id(id_obligacion: int):
    """
    Obtener una obligacion por su ID.
    Retorna una obligacion si es encontrado, de lo contrario lanza un error 404.
    """
    obligacion = get_obligacion_by_id(id_obligacion)
    if obligacion is None:
        raise HTTPException(status_code=404, detail="Obligacion not found")
    return obligacion

@router_obligacion.post("/obligacion/", response_model=ObligacionOut, tags=['Obligacion'])
async def create_empresa_db(obligacion: ObligacionIn):
    """
    Crear una nueva Obligación en la base de datos.
    Retorna la obligacion recién creada.
    """
    created_obligacion = create_obligacion(obligacion)
    return created_obligacion

@router_obligacion.delete("/obligacion/{id_obligacion}", response_model=ObligacionOut, tags=['Obligacion'])
async def delete_obligacion_db(id_obligacion: int):
    """
    Eliminar una obligacion  de la base de datos por su ID.
    Retorna la obligacion eliminado si es encontrado, de lo contrario lanza un error 404.
    """
    deleted_obligacion = deleted_obligacion(id_obligacion)
    if deleted_obligacion is None:
        raise HTTPException(status_code=404, detail="Obligacion not found")
    return deleted_obligacion

@router_obligacion.put("/obligacion/{id_obligacion}", response_model=ObligacionOut, tags=['Obligacion'])
async def update_obligacion_db(id_obligacion: int, new_obligacion: ObligacionIn):
    """
    Actualizar la información de una obligacion existente.
    Retorna la obligacion actualizada.
    """