import os
from sqlmodel import create_engine, SQLModel

# Use environment variables with fallbacks
username = os.getenv('DB_USERNAME', 'admin')
password = os.getenv('DB_PASSWORD', 'adminadmin')
host = os.getenv('DB_HOST', '54.156.255.195')
database = os.getenv('DB_DATABASE', 'dataminds')

# Create a SQLModel engine
DATABASE_URL = f'mysql+mysqlconnector://{username}:{password}@{host}:3306/{database}'
engine = create_engine(DATABASE_URL)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)