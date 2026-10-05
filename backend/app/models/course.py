from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship 
from sqlalchemy.sql import func
from app.database import Base

class Course(Base): 
  __tablename__ = "courses"

  id = Column(Integer, primary_key=True, index=True)
  title = Column(String, nullable=False)
  description = Column(String, nullable=True)
  created_at = Column(DateTime(timezone=True), server_default=func.now())

  user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

  owner = relationship("User", back_populates="courses")

  documents = relationship(
    "Document",
    back_populates="course",
    cascade="all, delete-orphan"
  )

  flashcard_decks = relationship(
    "FlashcardDeck",
    back_populates="course",
    cascade="all, delete-orphan"
  )