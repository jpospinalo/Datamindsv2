import os
from fastapi import FastAPI
from app.routers.cliente import router
from app.routers.empresa import router_empresa
from app.routers.obligacion import router_obligacion
from app.routers.auth import router_auth
from app.database import create_db_and_tables
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

app = FastAPI(
    title="DataMinds API",
    description="API para gestión de clientes, obligaciones y empresas",
    version="0.1.0"
)

# Include routers
app.include_router(router)
app.include_router(router_empresa)
app.include_router(router_obligacion)
app.include_router(router_auth)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()
    
@app.get("/")
async def root():
    return {"message": "Welcome to DataMinds API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app", 
        host=os.getenv("APP_HOST"),
        port=int(os.getenv("APP_PORT")),
        reload=os.getenv("DEBUG", "False").lower() == "true"
    )

