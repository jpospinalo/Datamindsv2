from sqlmodel import select, Session
from app.models.models import Client
from app.schemas.esquemas import ClientIn, ClientOut
from app.database import engine
from typing import List

def create_client(client_in: ClientIn) -> ClientOut:
    with Session(engine) as session:
        new_client = Client(**client_in.model_dump())
        session.add(new_client)
        session.commit()
        session.refresh(new_client)
    return new_client

def get_client_by_id(client_id: str) -> ClientOut | None:
    with Session(engine) as session:
        client = session.get(Client, client_id)
        return client

def get_all_clients() -> List[ClientOut]:
    with Session(engine) as session:
        statement = select(Client)
        clients = session.exec(statement).all()
        return clients

def update_client(client_id: str, new_client: ClientIn) -> ClientOut | None:
    with Session(engine) as session:    
            db_client = session.get(Client, client_id)
            client_data = new_client.model_dump(exclude_unset=True)

            for key, value in client_data.items():
                setattr(db_client, key, value)
            session.add(db_client)
            session.commit()
            session.refresh(db_client)
            return db_client

def delete_client(client_id: str):
    with Session(engine) as session:
        client = session.get(Client, client_id)
        if client:
            session.delete(client)
            session.commit()
            return client
        return None
