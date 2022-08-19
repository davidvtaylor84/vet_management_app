DROP TABLE pets;
DROP TABLE vets;

CREATE TABLE vets (
    id SERIAL PRIMARY KEY,
    vet_firstname VARCHAR(255),
    vet_surname VARCHAR(255),
    vet_email VARCHAR(255),
    vet_phone VARCHAR(255)
);

CREATE TABLE pets (
    id SERIAL PRIMARY KEY,
    vet_id INT REFERENCES vets(id) ON DELETE CASCADE,
    pet_name VARCHAR(255),
    pet_type VARCHAR(255),
    owner_contact VARCHAR(255)
);