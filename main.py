from fastapi import FastAPI
from app.routers.cliente import router
from app.routers.empresa import router_empresa
from app.routers.obligacion import router_obligacion
from app.routers.auth import *
from app.services.crud_cliente import *
from app.services.crud_empresa import *
from app.services.crud_obligacion import *
import sys

app = FastAPI()
app.include_router(router)  # Incluir las rutas
app.include_router(router_empresa)
app.include_router(router_obligacion)
app.include_router(router_auth)

