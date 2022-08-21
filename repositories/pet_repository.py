from db.run_sql import run_sql

from models.pet import Pet
from models.vet import Vet

import repositories.vet_repository as vet_repository

def save(pet):
    sql = "INSERT INTO pets (pet_name, date_of_birth, pet_type, breed,pet_owner, treatment_notes, vet_id) VALUES (%s, %s, %s, %s, %s, %s, %s)returning id"
    values = [pet.pet_name, pet.date_of_birth, pet.pet_type, pet.breed, pet.pet_owner, pet.treatment_notes, pet.vet.id]
    results = run_sql(sql, values)
    pet.id = results [0]['id']
    return pet

def select_all():
    pets =[]
    sql = "SELECT * FROM pets"
    results = run_sql(sql)

    for result in results:
        vet = vet_repository.select(result['vet_id'])
        pet = Pet(result['pet_name'], result['date_of_birth'], result['pet_type'], result['breed'], result['pet_owner'], result['treatment_notes'], vet, result['id'])
        pets.append(pet)
    return pets


def select(id):
    pet = None
    sql = "SELECT * FROM pets WHERE id = %s"
    values = [id]
    results = run_sql(sql, values) 

    if results:
        result = results[0]
        vet = vet_repository.select(result['vet_id'])
        pet = Pet(result['pet_name'], result['date_of_birth'], result['pet_type'], result['breed'], result['pet_owner'], result['treatment_notes'], vet, result['id'])
    return pet


def delete_all():
    sql = "DELETE  FROM pets"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM pets WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(pet):
    sql = "UPDATE pets SET(pet_name, date_of_birth, pet_type, breed, pet_owner, treatment_notes, vet) = (%s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [pet.pet_name, pet.date_of_birth, pet.pet_type, pet.breed, pet.pet_owner, pet.treatment_notes, pet.vet.id, pet.id]
    run_sql(sql, values)
