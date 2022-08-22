from db.run_sql import run_sql

from models.owner import Owner
from models.pet import Pet

import repositories.vet_repository as vet_repository
import repositories.owner_repository as owner_repository

def save(owner):
    sql = "INSERT INTO owners (owner_firstname, owner_surname, owner_address, owner_email, owner_phone) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [owner.owner_firstname, owner.owner_surname, owner.owner_address, owner.owner_email, owner.owner_phone]
    results = run_sql(sql, values)
    owner.id = results[0] ['id']
    return owner


def select_all():
    owners = []

    sql = "SELECT * FROM owners"
    results = run_sql(sql)

    for result in results:
        owner = Owner(result['owner_firstname'], result['owner_surname'], result['owner_address'], result['owner_email'], result['owner_phone'], result['id'])
        owners.append(owner)
    return owners


def select(id):
    owner = None
    sql = "SELECT * FROM owners WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    
    if results:
        result = results[0]
        owner = Owner(result['owner_firstname'], result['owner_surname'], result['owner_address'], result['owner_email'], result['owner_phone'], result['id'])
    return owner


def delete_all():
    sql = "DELETE  FROM owners"
    run_sql(sql)

def update(owner):
    sql = "UPDATE owners SET(owner_firstname, owner_surname, owner_address, owner_email, owner_phone) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [owner.owner_firstname, owner.owner_surname, owner.owner_address, owner.owner_email, owner.owner_phone, owner.id]
    run_sql(sql, values)


def owns_which_pets(id):
    pets = []
    values = [id]

    sql = "SELECT * FROM pets WHERE owner_id = %s"
    results = run_sql(sql, values)

    for result in results:
        owner = owner_repository.select(result['owner_id'])
        vet = vet_repository.select(result['vet_id'])
        pet = Pet(result['pet_name'], result['date_of_birth'], result['pet_type'], result['breed'], owner, result['treatment_notes'], vet, result['id'])
        pets.append(pet)
    return pets
