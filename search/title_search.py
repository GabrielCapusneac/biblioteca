from fastapi import APIRouter
from typing import List
from book.book_model import BookCreate
# from book.books_list import get_full_books_list
from library.fake_db import fake_db

# search_title_router = APIRouter()
# search_autor_router = APIRouter()
# search_an_router = APIRouter()
#
# # cautam caretea in funtie de caractere introduse dupa / din url
# @search_title_router.get("/biblioteca/search/titlu/{titlu}", response_model=List[BookCreate])
# def search_titlu(titlu: str):
#     books = fake_db.get("add_book", {}).values()
#     # books_list=get_full_books_list()
#     # search_books=[book for book in books_list if titlu.lower() in book.get("search" , " ").lower()]
#     search_books = [book for book in books if titlu.lower() in book.get("titlu", " ").lower()]
#     return search_books
# @search_autor_router.get("/biblioteca/search/autor/{autor}", response_model=List[BookCreate])
# def search_autor(autor: str):
#     books = fake_db.get("add_book", {}).values()
#     search_books = [book for book in books if autor.lower() in book.get("autor", " ").lower() ]
#     return search_books
# @search_an_router.get("/biblioteca/search/an/{an}", response_model=List[BookCreate])
# def search_an(an: str):
#     books = fake_db.get("add_book", {}).values()
#     search_books = [book for book in books if an.lower() in book.get("an", " ").lower() ]
#     return search_books

search_results_router = APIRouter()


@search_results_router.get("/biblioteca/search/{data}")
def search(data):
    books = fake_db.get("add_book", {}).values()
    search_results = []

    for book in books:
        data = data.lower()
        if data in book["titlu"].lower() or data in book["autor"].lower() or data in book["an"].lower():
            search_results.append(book)
    # for book in books:
    #     results_filter = ((titlu.lower() in book.get("titlu", "").lower()) or
    #                       (autor.lower() in book.get("autor", "").lower()) or
    #                       (an == book.get("an")))
    #     if results_filter:
    #         search_results.append(book)
    return search_results
