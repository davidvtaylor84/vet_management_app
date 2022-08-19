import unittest

from models.pet import Pet
from models.vet import Vet

class TestPet(unittest.TestCase):

    def setUp(self):
        self.pet1 = Pet("Spanish Jones the Third", "21/09/2019", "Primate", "Capuchin Monkey", "Henry Pathfinder", "Has a weirdly shaped skull")



pet_name, date_of_birth, pet_type, breed, pet_owner, treatment_notes, vet