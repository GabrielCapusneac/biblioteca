from fastapi import APIRouter
import json


def init_fake_db():
    return {
        'adaugare_carte': init_data_from_file("D:\\ProblemaBiblioteca\\stocare\\books.json")
    }


def init_data_from_file(path):
    try:
        with open(path, "r") as file:
            return json.load(file)
    except:
        return {}


fake_db = init_fake_db()