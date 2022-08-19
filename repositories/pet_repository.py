from db.run_sql import run_sql

from models.pet import Pet
from models.vet import Vet

import repositories.vet_repository as vet_repository

def save(pet):
    sql = "INSERT INTO pets (pet_name, date_of_birth, pet_type, breed,pet_owner, treatment_notes, vet_id) VALUES (%s, %s, %s, %s, %s, %s, %s)returning id"
    values = [pet.pet_name, pet.date_of_birth, pet.pet_type, pet.breed, pet.pet_owner, pet.treatment_notes, pet.vet.id]
    results = run_sql(sql, values)
    id = results [0]['id']
    pet.id = id
    return pet

def delete_all():
    sql = "DELETE  FROM pets"
    run_sql(sql)





