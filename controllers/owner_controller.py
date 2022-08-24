from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.owner import Owner

import repositories.owner_repository as owner_repository

owners_blueprint = Blueprint("owners", __name__)

@owners_blueprint.route("/owners/<id>", methods = ['GET'])
def get_owner(id):
    owner = owner_repository.select(id)
    pets_list = owner_repository.owns_which_pets(id)
    return render_template("/owners/show.html", owner = owner, pets = pets_list )

@owners_blueprint.route("/owners/<id>/edit", methods = ['GET'])
def edit_owner(id):
    owner = owner_repository.select(id)
    return render_template('owners/edit.html', owner = owner)

@owners_blueprint.route("/owners/<id>", methods = ['POST'])
def update_owner(id):
    owner_firstname = request.form['owner_firstname']
    owner_surname = request.form['owner_surname']
    owner_address = request.form['owner_address']
    owner_email = request.form['owner_email']
    owner_phone = request.form['owner_phone']
    owner = Owner(owner_firstname, owner_surname, owner_address, owner_email, owner_phone, id)
    owner_repository.update(owner)
    pets_list = owner_repository.owns_which_pets(id)
    return render_template("/owners/show.html", owner = owner, pets=pets_list)
    # return redirect('/pets')

@owners_blueprint.route('/owners/new', methods = ['GET'])
def new_owner():
    return render_template ("/owners/new.html")

@owners_blueprint.route('/owners/new', methods = ['POST'])
def create_new_owner():
    owner_firstname = request.form['owner_firstname']
    owner_surname = request.form['owner_surname']
    owner_address = request.form['owner_address']
    owner_email = request.form['owner_email']
    owner_phone = request.form['owner_phone']
    owner = Owner(owner_firstname, owner_surname, owner_address, owner_email, owner_phone)
    owner_repository.save(owner)
    return redirect('/pets/new')

@owners_blueprint.route("/owners/<id>/delete", methods = ['POST'])
def delete_owner(id):
    owner_repository.delete(id)
    return redirect('/pets')
