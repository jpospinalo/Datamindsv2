from fastapi import FastAPI
from .routes_cliente import router
from .routes_empresa import router_empresa
from .routes_obligacion import router_obligacion
from .routes.auth import *
from .crud_cliente import *
from .crud_empresa import *
from .crud_obligacion import *
import sys

app = FastAPI()
app.include_router(router)  # Incluir las rutas
app.include_router(router_empresa)
app.include_router(router_obligacion)
app.include_router(router_auth)

