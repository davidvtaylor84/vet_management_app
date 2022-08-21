from models.vet import Vet
from models.pet import Pet
from models.owner import Owner

import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository
import repositories.owner_repository as owner_repository

pet_repository.delete_all()
vet_repository.delete_all()
owner_repository.delete_all()

vet1 = Vet('Benedict', 'Cumberbark', 'cats_off_to_you@pardontheinterrufftion.com', '07951 900 783')
vet_repository.save(vet1)
vet2 = Vet('Jon', 'Bone Jovi', 'you_have_to_be_kitten_me@pardontheinterrufftion.com', '07892 897 637')
vet_repository.save(vet2)
vet3 = Vet('Catalie', 'Portman', 'claws_and_effect@pardontheinterrufftion.com', '07892 7899 728')
vet_repository.save(vet3)

owner1 = Owner('Jonathan', 'Dinglehoffer', '17 Welshhead Drive, Edinburgh, UK, EH5 62P', 'having_a_swell_day@diegobeach.com', '0131 667 6723')
owner_repository.save(owner1)
owner2 = Owner('Jessica', 'Hellfire', '13 flat 3 Billy Crystal Drive, Livingston, UK', 'ohlord86@cripes.com', '07253 637 737')
owner_repository.save(owner2)

pet1 = Pet('Captain Purrcard', '21/02/2015', 'Cat', 'Persian', 'Henry', 'Bit of a sore leg', vet3)
pet_repository.save(pet1)
pet2 = Pet('Karl Barx', '02/03/2020', 'Dog', 'Irish Wolfhound', 'Billy', 'Listless and depressed', vet2)
pet_repository.save(pet2)





