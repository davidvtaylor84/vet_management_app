import unittest

from models.pet import Pet
from models.vet import Vet

class TestVet(unittest.TestCase):

    def setUp(self):
        self.vet1 = Vet('Benedict', 'Cumberbark', 'cats_off_to_you@pardontheinterrufftion.com', '07951 900 783')

        self.pet1 = Pet("Spanish Jones the Third", "21/09/2019", "Primate", "Capuchin Monkey", "Henry Pathfinder", "Has a weirdly shaped skull", self.vet1)

    def test_vet_has_surname(self):
        self.assertEqual("Cumberbark", self.vet1.surname)

    def test_vet_has_phone_number(self):
        self.assertEqual("07951 900 783", self.vet1.phone)

    def test_pet_has_breed(self):
        self.assertEqual("Capuchin Monkey", self.pet1.breed)

    def test_pet_has_vet(self):
        self.assertEqual("Cumberbark", self.pet1.vet.surname)
