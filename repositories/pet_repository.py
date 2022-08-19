from db.run_sql import run_sql

from models.pet import Pets
from models.vet import Vets

import repositories.vet_repository as vet_repository

def save(pet):
    sql = "INSERT INTO pets (pet_name, pet_type, owner_contact, vet_id) VALUES (%s, %s, %s, %s)returning id"
    values = [pet.pet_name, pet.pet_type, pet.owner_contact, pet.vet.id]
    results = run_sql(sql, values)
    id = results [0]['id']
    pet.id = id
    return pet

def delete_all():
    sql = "DELETE  FROM pets"
    run_sql(sql)

# def save(book):
#     # print(book.author.__dict__)
#     sql = "INSERT INTO books(book_name, author_id, genre, isbn) VALUES (%s, %s, %s, %s) RETURNING *"
#     values = [book.book_name, book.author.id, book.genre, book.isbn]
#     results = run_sql(sql, values)
#     print(results)
#     # print("results in repo", results)
#     id = results[0]['id']
#     book.id = id
#     return book



