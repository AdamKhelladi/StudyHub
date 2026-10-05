from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship 
from sqlalchemy.sql import func
from app.database import Base

class Document(Base): 
  __tablename__ = "documents"

  id = Column(Integer, primary_key=True, index=True)
  title = Column(String, nullable=False)
  content = Column(String, nullable=False)
  created_at = Column(DateTime(timezone=True), server_default=func.now())
  updated_at = Column(DateTime(timezone=True), onupdate=func.now())

  course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)

  course = relationship("Course", back_populates="documents")

  flashcard_decks = relationship(
    "FlashcardDeck",
    back_populates="source_document"
  )