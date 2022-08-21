from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.owner import Owner

import repositories.owner_repository as owner_repository

owners_blueprint = Blueprint("owners", __name__)

@owners_blueprint.route("/owners/<id>", methods = ['GET'])
def get_owner(id):
    owner = owner_repository.select(id)
    return render_template("/owners/show.html", owner = owner)

# @pets_blueprint.route("/pets/<id>/edit", methods = ['GET'])
# def edit_pet(id):
#     pet = pet_repository.select(id)
#     vets = vet_repository.select_all()
#     owners = owner_repository.select_all()
#     return render_template('pets/edit.html', pet = pet, vets = vets, owners = owners)

# @pets_blueprint.route("/pets/<id>", methods = ['POST'])
# def update_pet(id):
#     pet_name = request.form['pet_name']
#     date_of_birth = request.form['date_of_birth']
#     pet_type = request.form['pet_type']
#     breed = request.form['breed']
#     treatment_notes = request.form['treatment_notes']
#     vet_id = request.form['vet_id']
#     owner_id = request.form['owner_id']
#     owner = owner_repository.select(owner_id)
#     vet = vet_repository.select(vet_id)
#     pet = Pet(pet_name, date_of_birth, pet_type, breed, owner, treatment_notes, vet, id)
#     pet_repository.update(pet)
#     print (pet)
#     return redirect('/pets')

@owners_blueprint.route('/owners/new', methods = ['GET'])
def new_owner():
    return render_template ("/owners/new.html")

# @pets_blueprint.route('/pets/new', methods = ['POST'])
# def create_new_pet():
#     pet_name = request.form['pet_name']
#     date_of_birth = request.form ['date_of_birth']
#     pet_type = request.form['pet_type']
#     breed = request.form['breed']
#     owner_id = request.form['owner_id']
#     vet_id = request.form['vet_id']
#     treatment_notes = request.form['treatment_notes']
#     owner = owner_repository.select(owner_id)
#     vet = vet_repository.select(vet_id)
#     pet = Pet(pet_name, date_of_birth, pet_type, breed, owner, treatment_notes, vet)
#     pet_repository.save(pet)
#     return redirect('/pets')

# @pets_blueprint.route("/pets/<id>/delete", methods = ['POST'])
# def delete_pet(id):
#     pet_repository.delete(id)
#     return redirect('/pets')