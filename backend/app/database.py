from sqlalchemy import create_engine, event
from sqlalchemy.orm import declarative_base, sessionmaker

from sqlalchemy.engine import Engine 

DATABASE_URL = "sqlite:///./app.db"

engine = create_engine(
  DATABASE_URL, 
  connect_args={"check_same_thread": False}
)



SessionLocal = sessionmaker( # use it to query/create/update/delete database records
  autocommit=False,
  autoflush=False,
  bind=engine
)

Base = declarative_base()