from models.vet import Vets
from models.pet import Pets

import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository

pet_repository.delete_all()
vet_repository.delete_all()

vet1 = Vets('Benedict', 'Cumberbark', 'cats_off_to_you@pardontheinterrufftion.com', '07951 900 783')
vet_repository.save(vet1)
vet2 = Vets('Jon', 'Bone Jovi', 'you_have_to_be_kitten_me@pardontheinterrufftion.com', '07892 897 637')
vet_repository.save(vet2)
vet3 = Vets('Catalie', 'Portman', 'claws_and_effect@pardontheinterrufftion.com', '07892 7899 728')
vet_repository.save(vet3)

pet1 = Pets('Captain Purrcard', '21/02/2015', 'Cat', 'Persian', 'Mike Rophone', 'Bit of a sore leg', vet3)
pet_repository.save(pet1)
pet2 = Pets('Karl Barx', '02/03/2020', 'Dog', 'Irish Wolfhound', 'Helen Hywater', 'Listless and depressed', vet2)
pet_repository.save(pet2)





