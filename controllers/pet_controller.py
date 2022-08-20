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


    