from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.pet import Pet

import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository

pets_blueprint = Blueprint("pets", __name__)