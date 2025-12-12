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



def update_anime(db: Session, anime_id: int, update: dict):
    return crud.update_anime(db, anime_id, update)

def delete_anime(db: Session, anime_id: int):
    return crud.delete_anime(db, anime_id)