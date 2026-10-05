from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship 
from sqlalchemy.sql import func
from app.database import Base

class User(Base): 
  # 'One to many' relationship
  #   User
  #  │
  #  ├── Course 1
  #  ├── Course 2
  #  └── Course 3

  __tablename__ = "users" 

  id = Column(Integer, primary_key=True, index=True)
  email = Column(String, unique=True, nullable=False, index=True)
  hashed_password = Column(String, nullable=False)
  created_at = Column(DateTime(timezone=True), server_default=func.now())

  courses = relationship(
    "Course",
    back_populates="owner", # back_populates → tells SQLAlchemy that both relationships are two sides of the same relationship
    cascade="all, delete-orphan" # means deleting a User deletes all their Courses too — matches what you confirmed earlier.
  )