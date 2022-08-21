from db.run_sql import run_sql

from models.owner import Owner

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