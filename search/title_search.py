from fastapi import APIRouter, Path
from typing import List
from book.book_model import BookCreate
from book.books_list import get_full_books_list

search_router = APIRouter()

#cautam caretea in funtie de caractere introduse dupa / din url
@search_router.get("/biblioteca/search/{search}", response_model=List[BookCreate])
def search(titlu: str = Path(..., title="Titlul cărții", description="Introduceți titlul cărții pentru căutare")):
    books_list=get_full_books_list()
    search_books=[book for book in books_list if titlu.lower() in book["title"].lower()]
    return search_books