from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.pet import Pet

import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository
import repositories.owner_repository as owner_repository

pets_blueprint = Blueprint("pets", __name__)

@pets_blueprint.route('/pets')
def pets():
    pets_list = pet_repository.select_all()
    return render_template("pets/index.html", pets = pets_list)

@pets_blueprint.route("/pets/<id>", methods = ['GET'])
def get_pet(id):
    pet = pet_repository.select(id)
    return render_template("/pets/show.html", pet = pet)

@pets_blueprint.route("/pets/<id>/edit", methods = ['GET'])
def edit_pet(id):
    pet = pet_repository.select(id)
    vets = vet_repository.select_all()
    owners = owner_repository.select_all()
    return render_template('pets/edit.html', pet = pet, vets = vets, owners = owners)

@pets_blueprint.route("/pets/<id>", methods = ['POST'])
def update_pet(id):
    pet_name = request.form['pet_name']
    date_of_birth = request.form['date_of_birth']
    pet_type = request.form['pet_type']
    breed = request.form['breed']
    treatment_notes = request.form['treatment_notes']
    vet_id = request.form['vet_id']
    owner_id = request.form['owner_id']
    owner = owner_repository.select(owner_id)
    vet = vet_repository.select(vet_id)
    pet = Pet(pet_name, date_of_birth, pet_type, breed, owner, treatment_notes, vet, id)
    pet_repository.update(pet)
    print (pet)
    return redirect('/pets')

@pets_blueprint.route('/pets/new', methods = ['GET'])
def new_pet():
    owners = owner_repository.select_all()
    vets = vet_repository.select_all()
    return render_template ("/pets/new.html", vets = vets, owners = owners)

@pets_blueprint.route('/pets/new', methods = ['POST'])
def create_new_pet():
    pet_name = request.form['pet_name']
    date_of_birth = request.form ['date_of_birth']
    pet_type = request.form['pet_type']
    breed = request.form['breed']
    owner_id = request.form['owner_id']
    vet_id = request.form['vet_id']
    treatment_notes = request.form['treatment_notes']
    owner = owner_repository.select(owner_id)
    vet = vet_repository.select(vet_id)
    pet = Pet(pet_name, date_of_birth, pet_type, breed, owner, treatment_notes, vet)
    pet_repository.save(pet)
    return redirect('/pets')

@pets_blueprint.route("/pets/<id>/delete", methods = ['POST'])
def delete_pet(id):
    pet_repository.delete(id)
    return redirect('/pets')






    