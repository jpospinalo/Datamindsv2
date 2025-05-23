from sqlmodel import Field, Relationship, SQLModel
from datetime import date, datetime, time, timedelta

# Modelo de usuario
class User(SQLModel, table=True):
    
    __tablename__ = "usuarios"
    
    id: int= Field(primary_key=True)
    usuario: str
    contrasena: str
    ultimo_inicio_sesion: datetime
    activo: bool
    fecha_creacion: datetime
    fecha_actualizacion: datetime
    

# Conexión con la base de datos de la tabla Cliente.
class Client(SQLModel, table=True):
    
    __tablename__ = "cliente"
 
    id_cliente: str = Field(primary_key=True)
    tipo_documento: str 
    primer_nombre: str
    segundo_nombre: str | None = None
    primer_apellido: str
    segundo_apellido: str | None = None
    obligaciones : list["Obligacion"] = Relationship(back_populates="cliente", cascade_delete=True)

# Conexión con la base de datos de la tabla Obligación.
class Obligacion(SQLModel, table=True):
    
    __tablename__ = "obligacion"
 
    id_obligacion: int | None = Field(primary_key=True)
    id_empresa: int = Field(foreign_key="empresa.id_empresa")

    id_cliente: str = Field(foreign_key="cliente.id_cliente")
    cliente : Client = Relationship(back_populates="obligaciones")

    
# Conexión con la base de datos de la tabla Empresa.
class Empresa(SQLModel, table=True):
    
    __tablename__ = "empresa"
 
    id_empresa: int | None = Field(primary_key=True)
    nombre_empresa: str