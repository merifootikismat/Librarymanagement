from sqlalchemy.orm import Session
from .models import Book
from .models import Anime


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

def update(db: Session, book_id: int, data: dict):
    existing = get_by_id(db, book_id)
    if not existing:
        return None

    # apply only keys provided in the incoming data dict
    for key, value in data.items():
        # avoid setting attributes that don't exist on the model
        if hasattr(existing, key):
            setattr(existing, key, value)

    db.commit()
    db.refresh(existing)
    return existing

def delete(db: Session, book_id: int):
    book = get_by_id(db, book_id)
    if not book:
        return None
    db.delete(book)
    db.commit()
    return book



def get_all_anime(db: Session):
    return db.query(Anime).all()

def get_anime_by_id(db: Session, anime_id: int):
    return db.query(Anime).filter(Anime.id == anime_id).first()

def create_anime(db: Session, anime: dict):
    new_anime = Anime(**anime)
    db.add(new_anime)
    db.commit()
    db.refresh(new_anime)
    return new_anime



def update_anime(db: Session, anime_id: int, data: dict):
    existing = get_anime_by_id(db, anime_id)
    if not existing:
        return None

    for key, value in data.items():
        if hasattr(existing, key):
            setattr(existing, key, value)

    db.commit()
    db.refresh(existing)
    return existing

def delete_anime(db: Session, anime_id: int):
    anime = get_anime_by_id(db, anime_id)
    if not anime:
        return None
    db.delete(anime)
    db.commit()
    return anime