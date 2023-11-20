from pydantic import BaseModel

# Modelul introducerii unei noi carti
class  BookCreate(BaseModel):
    title : str
    autor : str
    an : str
