from sqlalchemy import create_engine, event
from sqlalchemy.orm import declarative_base, sessionmaker

from sqlalchemy.engine import Engine 

DATABASE_URL = "sqlite:///./app.db"

engine = create_engine(
  DATABASE_URL, 
  connect_args={"check_same_thread": False}
)

@event.listens_for(Engine, "connect") # Actually enforce my foreign-key constraints
def set_sqlite_pragma(dbapi_connection, connection_record): 
  cursor = dbapi_connection.cursor()
  cursor.execute("PRAGMA foreign_keys=ON")
  cursor.close()

SessionLocal = sessionmaker( # use it to query/create/update/delete database records
  autocommit=False,
  autoflush=False,
  bind=engine
)

Base = declarative_base()