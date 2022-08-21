DROP TABLE pets;
DROP TABLE owners;
DROP TABLE vets;

CREATE TABLE vets (
    id SERIAL PRIMARY KEY,
    firstname VARCHAR(255),
    surname VARCHAR(255),
    email VARCHAR(255),
    phone VARCHAR(255)
);

CREATE TABLE owners (
    id SERIAL PRIMARY KEY,
    owner_firstname VARCHAR(255),
    owner_surname VARCHAR(255),
    owner_address VARCHAR(255),
    owner_email VARCHAR (255),
    owner_phone VARCHAR(255)
);

CREATE TABLE pets (
    id SERIAL PRIMARY KEY,
    pet_name VARCHAR(255),
    date_of_birth VARCHAR(255),
    pet_type VARCHAR(255),
    breed VARCHAR(255),
    owner_id INT REFERENCES owners(id),
    treatment_notes VARCHAR(255),
    vet_id INT REFERENCES vets(id) 
);