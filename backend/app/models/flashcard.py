from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, Text
from sqlalchemy.orm import relationship 
from sqlalchemy.sql import func
from app.database import Base

# FlashcardDeck
#       │
#       └── flashcards
#               │
#               ├── Flashcard
#               ├── Flashcard
#               └── Flashcard

class FlashcardDeck(Base): 
  __tablename__ = "flashcard_decks"

  id = Column(Integer, primary_key=True, index=True)
  title = Column(String, nullable=False)
  created_at = Column(DateTime(timezone=True), server_default=func.now())

  course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)
  source_document_id = Column(Integer, ForeignKey("documents.id"), ondelete="SET NULL", nullable=True)

  course = relationship("Course", back_populates="flashcard_decks")
  source_document = relationship("Document", back_populates="flashcard_decks")

  flashcards = relationship(
    "Flashcard",
    back_populates="deck",
    cascade="all, delete-orphan"
  )

class Flashcard(Base): 
  __tablename__ = "flashcards"

  id = Column(Integer, primary_key=True, index=True)
  question = Column(Text, nullable=False)
  answer = Column(Text, nullable=False)
  ai_generated = Column(Boolean, default=False, nullable=False)
  created_at = Column(DateTime(timezone=True), server_default=func.now())

  deck_id = Column(Integer, ForeignKey("flashcard_decks.id"), nullable=False)

  deck = relationship("FlashcardDeck", back_populates="flashcards")

