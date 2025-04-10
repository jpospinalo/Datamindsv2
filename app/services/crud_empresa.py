from sqlmodel import select, Session
from models.models import Empresa
from schemas.esquemas import EmpresaIn, EmpresaOut
from app.database import engine
from typing import List

def create_empresa(Empresa_in: EmpresaIn) -> EmpresaOut:
    with Session(engine) as session:
        new_empresa = Empresa(**Empresa_in.model_dump())
        session.add(new_empresa)
        session.commit()
        session.refresh(new_empresa)
    return new_empresa


def get_empresa_by_id(id_empresa: int) -> EmpresaOut | None:
    with Session(engine) as session:
        empresa = session.get(Empresa, id_empresa)
        return empresa

def get_all_empresas() -> List[EmpresaOut]:
    with Session(engine) as session:
        statement = select(Empresa)
        empresas = session.exec(statement).all()
        return empresas

def update_empresa(id_empresa: int, new_empresa: EmpresaIn) -> EmpresaOut | None:
    with Session(engine) as session:    
            db_empresa = session.get(Empresa, id_empresa)
            empresa_data = new_empresa.model_dump(exclude_unset=True)

            for key, value in empresa_data.items():
                setattr(db_empresa, key, value)
            session.add(db_empresa)
            session.commit()
            session.refresh(db_empresa)
            return db_empresa

def delete_empresa(id_empresa: int):
    with Session(engine) as session:
        empresa = session.get(Empresa, id_empresa)
        if empresa:
            session.delete(empresa)
            session.commit()
            return empresa