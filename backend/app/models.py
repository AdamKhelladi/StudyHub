from sqlalchemy import Column, Integer, String
from app.database import Base

class User(Base): 
  __tabelname__ = "users"

  id = Column(Integer, primary_key=True, index=True)
  username = Column(String, unique=True, nullable=False, index=True)

class Product(Base): 
  __tablename__ = "Products"

  id = Column(Integer, index=True)
  product_name = Column(String, nullable=False)
  price = Column(Integer)
