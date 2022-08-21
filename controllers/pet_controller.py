from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.pet import Pet

import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository

pets_blueprint = Blueprint("pets", __name__)

@pets_blueprint.route('/pets')
def pets():
    pets_list = pet_repository.select_all()
    return render_template("pets/index.html", pets = pets_list)

@pets_blueprint.route("/pets/<id>", methods = ['GET'])
def get_pet(id):
    pet = pet_repository.select(id)
    return render_template("/pets/show.html", pet = pet)

@pets_blueprint.route('/pets/new', methods = ['GET'])
def new_pet():
    vets = vet_repository.select_all()
    return render_template ("pets/new.html", vets = vets)

@pets_blueprint.route('/pets/new', methods = ['POST'])
def create_new_pet():
    pet_name = request.form['pet_name']
    date_of_birth = request.form ['date_of_birth']
    pet_type = request.form['pet_type']
    breed = request.form['breed']
    pet_owner = request.form['pet_owner']
    vet_id = request.form['vet_id']
    treatment_notes = request.form['treatment_notes']
    vet = vet_repository.select(vet_id)
    pet = Pet(pet_name, date_of_birth, pet_type, breed, pet_owner, treatment_notes, vet)
    pet_repository.save(pet)
    return redirect('/pets')






    