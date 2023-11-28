from fastapi import APIRouter
from library.fake_db import fake_db

search_results_router = APIRouter()


# cautam siruri de caractere in cartile existente in cele 3 elemente ale acesteia(titlu,autor,an), sirul de caractere pe care dorim sa il cautam in iltroducem la sfarsitul urlului de cautare

@search_results_router.get("/biblioteca/search/{data}")
def search(data):
    books = fake_db.get("add_book", {}).values()
    search_results = []  # creem o lista in care introcem cartle ce respecta sirul de caractere introdus in url

    # verificam sirul de caractere din url daca corespunde cu cele din cartile existente
    for book in books:
        data = data.lower()
        if data in book["titlu"].lower() or data in book["autor"].lower() or data in book["an"].lower():
            search_results.append(
                book)  # daca se gasesc similitudini intre sirul de caractere din url si cele din elementele cartii il adaugam in lista creata anterior
    return search_results
