from models.vet import Vets
from models.pet import Pets

import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository

vet1 = Vets('Benedict', 'Cumberbark', 'cats_off_to_you@gmail.com', '07951 900 783')
vet_repository.save(vet1)
vet2 = Vets('Jon', 'Bone Jovi', 'you_have_to_be_kitten_me@gmail.com', '07892 897 637')
vet_repository.save(vet2)