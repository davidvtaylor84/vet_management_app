DROP TABLE pets;
DROP TABLE vets;

CREATE TABLE vets (
    id SERIAL PRIMARY KEY,
    firstname VARCHAR(255),
    surname VARCHAR(255),
    email VARCHAR(255),
    phone VARCHAR(255)
);

CREATE TABLE pets (
    id SERIAL PRIMARY KEY,
    pet_name VARCHAR(255),
    pet_type VARCHAR(255),
    owner_contact VARCHAR(255)
    vet_id INT REFERENCES vets(id) 
);