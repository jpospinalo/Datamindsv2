from fastapi import FastAPI, APIRouter, HTTPException, Path
from typing import List, Annotated
from .schemas import ClientIn, ClientOut
from .crud_cliente import get_all_clients, get_client_by_id, create_client, delete_client, update_client


router = APIRouter()

@router.get("/client/", response_model=List[ClientOut], tags=['Cliente'])
async def read_all_clients():
    """
    Obtener todos los clientes de la base de datos.
    Retorna una lista de clientes.
    """
    clients = get_all_clients()
    if not clients:
        raise HTTPException(status_code=404, detail="No clients found")
    return clients

@router.get("/client/{client_id}", response_model=ClientOut, tags=['Cliente'])
async def read_client_by_id(
    client_id: Annotated[
        str, 
        Path(
            title="id cliente",
            description="Identificador del cliente en la base de datos", 
            max_lenght = 50
        )
    ]
): 
    """
    Obtener un cliente por su ID.
    Retorna un cliente si es encontrado, de lo contrario lanza un error 404.
    """
    client = get_client_by_id(client_id)
    if client is None:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return client

@router.post("/client/", response_model=ClientOut, tags=['Cliente'])
async def create_client_db(client: ClientIn):
    """
    Crear un nuevo cliente en la base de datos.
    Retorna el cliente recién creado.
    """
    created_client = create_client(client)
    return created_client

@router.delete("/client/{client_id}", response_model=ClientOut, tags=['Cliente'])
async def delete_client_db(client_id: str):
    """
    Eliminar un cliente de la base de datos por su ID.
    Retorna el cliente eliminado si es encontrado, de lo contrario lanza un error 404.
    """
    deleted_client = delete_client(client_id)
    if deleted_client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return deleted_client

@router.put("/client/{client_id}", response_model=ClientOut, tags=['Cliente'])
async def update_client_db(client_id: str, new_client: ClientIn):
    """
    Actualizar la información de un cliente existente.
    Retorna el cliente actualizado.
    """
    updated_client = update_client(client_id, new_client)
    if updated_client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return updated_client
