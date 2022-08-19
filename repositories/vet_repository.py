from db.run_sql import run_sql

from models.vet import Vets
from models.pet import Pets

def save(vet):
    sql = "INSERT INTO vets (firstname, surname, email, phone) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [vet.firstname, vet.surname, vet.email, vet.phone]
    results = run_sql(sql, values)
    vet.id = results[0] ['id']
    return vet