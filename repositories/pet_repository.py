from db.run_sql import run_sql

from models.pet import Pets
from models.vet import Vets

def save(pet):
    sql = "INSERT INTO pets (pet_name, pet_type, owner_name, owner_contact, vet_id) VALUES (%s, %s, %s, %s, %s)returning id"
    values = 



