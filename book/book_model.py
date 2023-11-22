from pydantic import BaseModel


# Modelul introducerii unei noi carti
class BookCreate(BaseModel):
    titlu: str
    autor: str
    an: str
