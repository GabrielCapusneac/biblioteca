import json
# from fastapi import HTTPException
from uuid import uuid4
from library.fake_db import fake_db


def get_book_data(data):
    books = fake_db.get("books", {}).values()
    for book in books:
        title = book.get("title")
        autor = book.get("autor")
        an = book.get("an")


def add_book(data):
    books = fake_db.get("add_book", {})

    existing_book = next(
        (book for book in books.values() if
         book["titlu"].lower() == data.titlu.lower() and
         book["autor"].lower() == data.autor.lower() and
         book["an"] == data.an),
        None
    )

    # if existing_book:
    #     return None
    # if existing_book:
    #     raise HTTPException(status_code=404, detail="Cartea introdusa este deja existenta")

    book_id = str(uuid4())

    book_data = data.model_dump()
    book_data["id"] = book_id
    books[book_id] = book_data

    with open("D:\\biblioteca2\\library\\books.json", "w") as file:
        json.dump(books, file, default=str)

    return book_data
