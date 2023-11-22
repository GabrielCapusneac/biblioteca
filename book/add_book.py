from fastapi import APIRouter
from book.book_model import BookCreate
from book.book_id import get_book_data,add_book

carti_router = APIRouter()

#metoda de introducere a cartii folosind metoda post si respectant modelul de adaugare

@carti_router.post("/biblioteca/adaugare_carte", response_model=BookCreate)
def addbook(book_data: BookCreate):
    book = get_book_data(book_data)
    if not book:
        book = add_book(book_data)
    return book