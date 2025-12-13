from sql import crud
from sqlalchemy.orm import Session
from sql.models import Anime

def list_anime(db: Session):
    return crud.get_all_anime(db)


def get_anime(db: Session, anime_id: int):
    return crud.get_anime_by_id(db, anime_id)

def create_anime(db: Session, data: dict):
    anime_data = {
        "title": data.get("title"),
        "genre": data.get("genre"),
        "episodes": data.get("episodes"),
        "availability": data.get("availability"),
        "rating": data.get("rating"),
        "book_id": data.get("book_id")
    }
    return crud.create_anime(db, anime_data)

def delete_anime(db: Session, anime_id: int):
    return crud.delete_anime(db, anime_id)


def update_anime(db: Session, anime_id: int, update: dict):
    anime= crud.update_anime(db, anime_id, update)
    book = None
    #case 1 (rating<5)
    if anime.rating<5:
        book.available = False
    elif 5 <= anime.rating <= 7:
        book.available = True
    elif anime.rating>7:
        anime.episodes = anime.episodes*2
    db.commit()
    db.refresh(anime)
    return anime