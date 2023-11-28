from fastapi import APIRouter
from library.fake_db import fake_db

# afisam toata lista existenta in folderul in care introducem cartile

books_list_router = APIRouter()


@books_list_router.get("/biblioteca/catalog_carti")
def get_full_books_list():
    books = fake_db.get("add_book", {}).values()
    return list(books)
