from fastapi import FastAPI, APIRouter, HTTPException
from typing import List
from app.schemas.esquemas import EmpresaIn, EmpresaOut
from app.services.crud_empresa import get_all_empresas, get_empresa_by_id, create_empresa, delete_empresa, update_empresa

router_empresa = APIRouter()

@router_empresa.get("/empresa/", response_model=List[EmpresaOut], tags=['Empresa'])
async def read_all_empresas():
    """
    Obtener todos los empresas de la base de datos.
    Retorna una lista de empresas.
    """
    empresas = get_all_empresas()
    if not empresas:
        raise HTTPException(status_code=404, detail="Company not found")
    return empresas

@router_empresa.get("/empresa/{id_empresa}", response_model=EmpresaOut, tags=['Empresa'])
async def read_empresa_by_id(id_empresa: int):
    """
    Obtener una empresa por su ID.
    Retorna una empresa si es encontrado, de lo contrario lanza un error 404.
    """
    empresa = get_empresa_by_id(id_empresa)
    if empresa is None:
        raise HTTPException(status_code=404, detail="Company not found")
    return empresa

@router_empresa.post("/empresa/", response_model=EmpresaOut, tags=['Empresa'])
async def create_empresa_db(empresa: EmpresaIn):
    """
    Crear una nueva empresa en la base de datos.
    Retorna la empresa recién creado.
    """
    created_empresa = create_empresa(empresa)
    return created_empresa

@router_empresa.delete("/empresa/{id_empresa}", response_model=EmpresaOut, tags=['Empresa'])
async def delete_empresa_db(id_empresa: int):
    """
    Eliminar una empresa  de la base de datos por su ID.
    Retorna la empresa  eliminado si es encontrado, de lo contrario lanza un error 404.
    """
    deleted_empresa = delete_empresa(id_empresa)
    if deleted_empresa is None:
        raise HTTPException(status_code=404, detail="Company not found")
    return deleted_empresa

@router_empresa.put("/empresa/{id_empresa}", response_model=EmpresaOut, tags=['Empresa'])
async def update_empresa_db(id_empresa: int, new_empresa: EmpresaIn):
    """
    Actualizar la información de un empresa existente.
    Retorna la empresa actualizado.
    """