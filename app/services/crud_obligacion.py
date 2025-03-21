from sqlmodel import select, Session
from .models import Obligacion
from .schemas import ObligacionIn, ObligacionOut
from .database import engine
from typing import List

def create_obligacion(Obligacion_in: ObligacionIn) -> ObligacionOut:
    with Session(engine) as session:
        new_obligacion = Obligacion(**Obligacion_in.model_dump())
        session.add(new_obligacion)
        session.commit()
        session.refresh(new_obligacion)
    return new_obligacion

def get_obligacion_by_id(id_obligacion: int) -> ObligacionOut | None:
    with Session(engine) as session:
        obligacion = session.get(Obligacion, id_obligacion)
        return obligacion

def get_all_obligacion() -> List[ObligacionOut]:
    with Session(engine) as session:
        statement = select(Obligacion)
        obligacion = session.exec(statement).all()
        return obligacion

def update_obligacion(id_obligacion: int, new_obligacion: ObligacionIn) -> ObligacionOut | None:
    with Session(engine) as session:    
            db_obligacion = session.get(Obligacion, id_obligacion)
            obligacion_data = new_obligacion.model_dump(exclude_unset=True)

            for key, value in obligacion_data.items():
                setattr(db_obligacion, key, value)
            session.add(db_obligacion)
            session.commit()
            session.refresh(db_obligacion)
            return db_obligacion

def delete_obligacion(id_obligacion: int):
    with Session(engine) as session:
        obligacion = session.get(Obligacion, id_obligacion)
        if obligacion:
            session.delete(obligacion)
            session.commit()
            return obligacion
