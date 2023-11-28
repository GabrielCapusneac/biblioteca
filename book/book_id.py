import json
from fastapi import HTTPException
from uuid import uuid4
from library.fake_db import fake_db


# afisam toata lista aflata in locatia de introducere din fake db
def get_book_data(data):
    books = fake_db.get("books", {}).values()
    for book in books:
        title = book.get("title")
        autor = book.get("autor")
        an = book.get("an")


# adaugam cartile noi in locatia precizata in fake db
def add_book(data):
    books = fake_db.get("add_book", {})

    # verificam prentru fiecare element al cartii daca sunt identice cu altele din cele pe care le am introdus interior

    duplicate = next(
        (book for book in books.values() if
         book["titlu"].lower() == data.titlu.lower() and
         book["autor"].lower() == data.autor.lower() and
         book["an"] == data.an),
        None
    )

    # afisam un mesaj in postman la detectarea unei carti identice cu cele introduse si lansam eroare in cod
    if duplicate:
        raise HTTPException(status_code=400, detail="Cartea introdusa este deja existenta")

    # initializam cate un id unic pentru fiecare carte introduse si ii atribuim acesteia un sigur id
    book_id = str(uuid4())

    book_data = data.model_dump()
    book_data["id"] = book_id
    books[book_id] = book_data

    with open("D:\\biblioteca2\\library\\books.json", "w") as file:
        json.dump(books, file, default=str)

    return book_data
