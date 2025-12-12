# sql/models.py
from .database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    available = Column(Boolean, default=True)

class Anime(Base):
    __tablename__ = "anime"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    genre = Column(String, nullable=True)
    episodes = Column(Integer, nullable=True)
    availability = Column(Boolean, default=True)
    rating = Column(Integer, nullable=True)

    book_id = Column(Integer, ForeignKey("books.id"), nullable=True)

    book = relationship("Book", backref="anime_list") #for easy serialisation
