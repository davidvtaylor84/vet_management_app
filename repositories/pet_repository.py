from db.run_sql import run_sql

from models.pet import Pet
from models.vet import Vet
from models.owner import Owner

import repositories.vet_repository as vet_repository
import repositories.owner_repository as owner_repository

def save(pet):
    sql = "INSERT INTO pets (pet_name, date_of_birth, pet_type, breed, owner_id, treatment_notes, vet_id) VALUES (%s, %s, %s, %s, %s, %s, %s)returning id"
    values = [pet.pet_name, pet.date_of_birth, pet.pet_type, pet.breed, pet.owner.id, pet.treatment_notes, pet.vet.id]
    results = run_sql(sql, values)
    pet.id = results [0]['id']
    return pet

def select_all():
    pets =[]
    sql = "SELECT * FROM pets ORDER BY pet_name"
    results = run_sql(sql)

    for result in results:
        owner = owner_repository.select(result['owner_id'])
        vet = vet_repository.select(result['vet_id'])
        pet = Pet(result['pet_name'], result['date_of_birth'], result['pet_type'], result['breed'], owner, result['treatment_notes'], vet, result['id'])
        pets.append(pet)
    return pets

# select an individual pet
# define pet as None
# write Sql query - "select all from pets where id is etc"
# define Values as the pet id in a list
# write Results as equal to Run_SQl with SQL and Values as values.
# write if statement - Results
# result equals results
# define owner using Select from Owner Repository
# define vet using Select from Vet Repository
# define Pet with Result, putting in 'pet_name', date_of_birth etc, as well as defined owner and vet.
# return pet

def select(id):
    pet = None
    sql = "SELECT * FROM pets WHERE id = %s"
    values = [id]
    results = run_sql(sql, values) 

    if results:
        result = results[0]
        owner = owner_repository.select(result['owner_id'])
        vet = vet_repository.select(result['vet_id'])
        pet = Pet(result['pet_name'], result['date_of_birth'], result['pet_type'], result['breed'], owner, result['treatment_notes'], vet, result['id'])
    return pet


def delete_all():
    sql = "DELETE  FROM pets"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM pets WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(pet):
    sql = "UPDATE pets SET(pet_name, date_of_birth, pet_type, breed, owner_id, treatment_notes, vet_id) = (%s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [pet.pet_name, pet.date_of_birth, pet.pet_type, pet.breed, pet.owner.id, pet.treatment_notes, pet.vet.id, pet.id]
    run_sql(sql, values)

def pets_search_by_pet_name(almost_name):
    pets_list = []
    sql = """SELECT pets.* FROM pets 
        INNER JOIN owners
        ON owners.id = pets.owner_id
        WHERE lower(pet_name) LIKE %s 
        OR lower(owner_surname) LIKE %s"""
    values = ['%'+almost_name+'%', '%'+almost_name+'%']
    results = run_sql(sql, values)
    for row in results:
        owner = owner_repository.select(row['owner_id'])
        vet = vet_repository.select(row['vet_id'])
        pet = Pet(row['pet_name'], row['date_of_birth'], row['pet_type'], row['breed'], owner, row['treatment_notes'], vet, row['id'])
        pets_list.append(pet)
    return pets_list


