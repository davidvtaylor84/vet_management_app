from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.vet import Vet

import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository

vets_blueprint = Blueprint("vets", __name__)