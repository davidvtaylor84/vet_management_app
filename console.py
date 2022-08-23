from models.vet import Vet
from models.pet import Pet
from models.owner import Owner

import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository
import repositories.owner_repository as owner_repository

pet_repository.delete_all()
vet_repository.delete_all()
owner_repository.delete_all()

vet1 = Vet('Dr. Benedict', 'Cumberbark', 'cats_off_to_you@pardontheinterrufftion.com', '07951 900 783')
vet_repository.save(vet1)
vet2 = Vet('Dr. Jon', 'Bone Jovi', 'you_have_to_be_kitten_me@pardontheinterrufftion.com', '07892 897 637')
vet_repository.save(vet2)
vet3 = Vet('Dr. Catalie', 'Portman', 'claws_and_effect@pardontheinterrufftion.com', '07892 7899 728')
vet_repository.save(vet3)

owner1 = Owner('Jonathan', 'Dinglehoffer', '17 Welshhead Drive, Edinburgh, UK, EH5 62P', 'having_a_swell_day@diegobeach.com', '0131 667 6723')
owner_repository.save(owner1)
owner2 = Owner('Jessica', 'Hellfire', '13 flat 3 Billy Crystal Drive, Livingston, UK', 'ohlord86@cripes.com', '07253 637 737')
owner_repository.save(owner2)
owner3 = Owner('Jimmy', 'The Snitch', '84 Welsh Rabbit Hellscape, Edinburgh, EH6 7HY', 'the_merry_wines_of_mysore@grip.com', '08832 828 828')
owner_repository.save(owner3)
owner4 = Owner('Phillipa', 'Sightforsoreeyes', '76/3 Johnny Cash Way, Edinburgh, EH5 7YH', 'where_are_the_beef_sticks@yahoo.co.uk', '637 7276')
owner_repository.save(owner4)
owner5 = Owner('Frankenhoffer', 'Alexander', '899 Mansion Willed to the Bone, Edinburgh, EH8 6YH', 'holymenof the east@willis.com', '07788 896 987')
owner_repository.save(owner5)
owner6 = Owner('Millficent', 'Helpmekill', '73 Great Walls of Fire, Edinburgh, EH6 76Y', 'ilostmyshoes@goalpost.com', '08877 637 736')
owner_repository.save(owner6)

pet1 = Pet('Captain Purrcard', '21/02/2015', 'Cat', 'Persian', owner1, '21/01/2022: Bit of a sore leg and, to be honest, his hair is going. He lost his car during a trip to Torquay and was attacked by a flock of seagulls who ate the contents of his handbag. A tough time overrall', vet3)
pet_repository.save(pet1)
pet2 = Pet('Karl Barx', '02/03/2020', 'Dog', 'Irish Wolfhound', owner2, '15/03/2022: Listless and depressed. Cannot get up in the morning. His tongue is furred. Too much cream in the diet. And also let me tell you about the time he saw Boris Johnson in an air balloon.', vet2)
pet_repository.save(pet2)
pet3 = Pet('Margaret Scratcher', '07/09/2017', 'Alien', 'Xenomorph', owner4, '06/04/2022: A bit bitey tbh. He likes to create havok wherever he goes. I caught him on Friday night keying somebodys car. He ate the neighbours dog and threw up in the sink afterwards. May have been food poisoning.', vet1)
pet_repository.save(pet3)
pet4 = Pet('Andy Warhowl', '09/08/2014', 'Ape', 'Gorilla', owner4, '07/09/2021: Not seen this guy for a while. He ate a chocolate watch owned by a clown. He attacked him during his stint as a circus clown. His act involved bamboozling people with a cup and ball con trick.', vet2)
pet_repository.save(pet4)
pet5 = Pet('Indiana Bones', '08/04/2018', 'Horse', 'Fabulous Horse', owner5, '01/01/2019: He is sad. You could say that he has a long face. Hahaha. Oh boy. I am such a joker. Forget it. He broke his leg and his owner decided he should do some yoga in order to get back into shape. I concurred.', vet1)
pet_repository.save(pet5)
pet6 = Pet('Sarah Jessica Barker', '01/05/2019', 'Cryptid', 'Sasquatch', owner4, '03/05/2022: What a character! He has terrible breath though. He eats like 15 buckets of fingernails a day. Its the only thing that satisfies him. Also, thirteen times a day he likes to challenge people to an arm wrestle and has a tendency to rip arms off an use them as drumsticks. He likes to play the drums you see. I diagnose a profound insanity borne from years of living in the woods and talking to squirrels who are known for their foul tempers.', vet3)
pet_repository.save(pet6)
pet7 = Pet('Kanye Westie', '08/12/2019', 'Dream Figment', 'Nightmare', owner4, '09/09/2022: Its a tough day in the jail. Many people have asked me where they can find the time to carry on. I have been treating this nightmare creature for the last three weeks and he will not go away.', vet2)
pet_repository.save(pet7)





