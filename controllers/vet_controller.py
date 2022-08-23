from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.vet import Vet

import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository

vets_blueprint = Blueprint("vets", __name__)

@vets_blueprint.route('/vets')
def vets():
    vets = vet_repository.select_all()
    return render_template("vets/index.html", vets = vets)

@vets_blueprint.route("/vets/<id>/edit", methods = ['GET'])
def edit_vet(id):
    vet = vet_repository.select(id)
    return render_template('vets/edit.html', vet = vet)

@vets_blueprint.route("/vets/<id>", methods = ['POST'])
def update_vet(id):
    firstname = request.form['firstname']
    surname = request.form['surname']
    email = request.form['email']
    phone = request.form['phone']
    vet = Vet(firstname, surname, email, phone, id)
    vet_repository.update(vet)
    return redirect('/vets')