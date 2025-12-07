from sqlalchemy.orm import Session
from .models import Book


def get_all(db: Session):
    return db.query(Book).all()

def get_by_id(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()

def create_book(db: Session, book: dict):
    new_book = Book(**book)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

def update(db:Session, book_id:int, book:dict):
    book = get_by_id(db, book_id)
    if not book:
        return None
    for key, value in book.items():
        setattr(book, key, value)

    db.commit()
    db.refresh(book)
    return book

def delete(db: Session, book_id: int):
    book = get_by_id(db, book_id)
    if not book:
        return None
    db.delete(book)
    db.commit()
    return book