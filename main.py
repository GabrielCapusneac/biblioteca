from fastapi import FastAPI
from book.add_book import carti_router
from book.books_list import books_list_router
from search.title_search import search_router

biblioteca = FastAPI()

biblioteca.include_router(carti_router)
biblioteca.include_router(books_list_router)
biblioteca.include_router(search_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(biblioteca, host="0.0.0.0", port=8000)