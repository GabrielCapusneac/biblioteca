from fastapi import APIRouter
from library.fake_db import fake_db

# from carte.modelcarte import BookCreate

books_list_router = APIRouter()


@books_list_router.get("/biblioteca/catalog_carti")
def get_full_books_list():
    books = fake_db.get("adaugare_carte", {}).values()
    return list(books)
