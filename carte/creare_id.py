import json
from uuid import uuid4
from stocare.fake_db import fake_db

def get_book_data(data):
    books = fake_db.get("books",{}).values()
    for book in books:
        title = book.get("title")
        autor = book.get("autor")
        an = book.get("an")

def add_book(data):
    books = fake_db.get("books", {})

    book_id = str(uuid4())

    book_data = data.model_dump()
    book_data["id"] = book_id
    books[book_id] = book_data

    with open("D:\\ProblemaBiblioteca\\stocare\\books.json", "w") as file:
        json.dump(books, file, default=str)

    return book_data