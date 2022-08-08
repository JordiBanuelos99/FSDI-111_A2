CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(45),
    last_name VARCHAR(45),
    hobbies TEXT,
    active BOOLEAN DEFAULT 1
);

CREATE TABLE vehicle (
    id_vehicle INTEGER PRIMARY KEY AUTOINCREMENT,
    vehicle_model VARCHAR(45),
    vehicle_type VARCHAR(45),
    vehicle_year INTEGER,
    vehicle_brand VARCHAR(45),
    vehicle_transmission VARCHAR(45),
    id_user INTEGER,

    CONSTRAINT fk_user
        FOREIGN KEY (id_user) REFERENCES user(id)
);

-- INSERT test records:

INSERT INTO user (
    first_name,
    last_name,
    hobbies
) VALUES (
    "John",
    "Doe",
    "Playing golf"
);

INSERT INTO user (
    first_name,
    last_name,
    hobbies
) VALUES (
    "Jane",
    "Doe",
    "Playing tennis"
);

INSERT INTO user (
    first_name,
    last_name,
    hobbies
) VALUES (
    "Bob",
    "Robertson",
    "Watching movies"
);

INSERT INTO vehicle (
    vehicle_model,
    vehicle_type,
    vehicle_year,
    vehicle_brand,
    vehicle_transmission,
    id_user
) VALUES (
    "Elantra",
    "Compact",
    2003,
    "Hyundai",
    "Automatic",
    1
);