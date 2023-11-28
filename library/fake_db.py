import json


# datele introduse vor fi adaugate in fisierul mentionat in functie
def init_fake_db():
    return {
        'add_book': init_data_from_file("D:\\biblioteca2\\library\\books.json")
    }


def init_data_from_file(path):
    try:
        with open(path, "r") as file:
            return json.load(file)
    except:
        return {}


fake_db = init_fake_db()
