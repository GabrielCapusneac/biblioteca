from pydantic import BaseModel


# Modelul introducerii unei noi carti, daca modelul nu este respectat nu putem introduce carti
class BookCreate(BaseModel):
    titlu: str
    autor: str
    an: str
