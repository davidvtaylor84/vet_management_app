from db.run_sql import run_sql

from models.vet import Vet
from models.pet import Pet

def save(vet):
    sql = "INSERT INTO vets (firstname, surname, email, phone) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [vet.firstname, vet.surname, vet.email, vet.phone]
    results = run_sql(sql, values)
    vet.id = results[0] ['id']
    return vet


def select_all():
    vets = []

    sql = "SELECT * FROM vets"
    results = run_sql(sql)

    for result in results:
        vet = Vet(result['firstname'], result['surname'], result['email'], result['phone'], result['id'])
        vets.append(vet)
    return vets

def select(id):
    vet = None
    sql = "SELECT * FROM vets WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    
    if results:
        result = results[0]
        vet = Vet(result['firstname'], result['surname'], result['email'], result['phone'], result['id'])
    return vet

def update(vet):
    sql = "UPDATE vets SET(firstname, surname, email, phone) = (%s, %s, %s, %s) WHERE id = %s"
    values = [vet.firstname, vet.surname, vet.email, vet.phone, vet.id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE  FROM vets"
    run_sql(sql)


# def check_in_pets(customer):
#         self.guests_in_room.append(customer)
#         return self.guests_in_room