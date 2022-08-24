import unittest

from models.pet import Pet
from models.vet import Vet
from models.owner import Owner

class TestVet(unittest.TestCase):

    def setUp(self):
        self.vet1 = Vet('Benedict', 'Cumberbark', 'cats_off_to_you@pardontheinterrufftion.com', '07951 900 783')
        
        self.owner1 = Owner('Millficent', 'Helpmekill', '73 Great Walls of Fire, Edinburgh, EH6 76Y', 'ilostmyshoes@goalpost.com', '08877 637 736')

        self.pet1 = Pet("Spanish Jones the Third", "21/09/2019", "Primate", "Capuchin Monkey", self.owner1, "Has a weirdly shaped skull", self.vet1)

    def test_vet_has_surname(self):
        self.assertEqual('Cumberbark', self.vet1.surname)

    def test_vet_has_phone_number(self):
        self.assertEqual("07951 900 783", self.vet1.phone)

    def test_pet_has_breed(self):
        self.assertEqual("Capuchin Monkey", self.pet1.breed)

    def test_pet_has_vet(self):
        self.assertEqual("Cumberbark", self.pet1.vet.surname)

    def test_pet_has_owner(self):
        self.assertEqual("Helpmekill", self.pet1.owner.owner_surname)

    def test_owner_has_phone_number(self):
        self.assertEqual("08877 637 736", self.owner1.owner_phone)

