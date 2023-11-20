from fastapi import FastAPI
from carte.adaugare_carte import carti_router
from carte.lista_carti_full import books_list_router

biblioteca = FastAPI()

biblioteca.include_router(carti_router)
biblioteca.include_router(books_list_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(biblioteca, host="0.0.0.0", port=8000)