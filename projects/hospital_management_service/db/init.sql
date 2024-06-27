CREATE TABLE IF NOT EXISTS patients (
    patient_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    gender VARCHAR(10) NOT NULL,
    address TEXT,
    contact VARCHAR(15) UNIQUE NOT NULL,
    unique_id VARCHAR(64) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS symptoms (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS tests (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    price DECIMAL(10, 2) NOT NULL
);

CREATE TABLE IF NOT EXISTS medicines (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    price DECIMAL(10, 2) NOT NULL
);

CREATE TABLE IF NOT EXISTS doctor_analysis_and_tests (
    id SERIAL PRIMARY KEY,
    patient_unique_id VARCHAR(64) NOT NULL,
    analysis JSONB NOT NULL,
    tests JSONB NOT NULL,
    medicines JSONB NOT NULL
);

CREATE TABLE IF NOT EXISTS doctor_analysis_and_tests_archive (
    id SERIAL PRIMARY KEY,
    patient_unique_id VARCHAR(64) NOT NULL,
    analysis JSONB NOT NULL,
    tests JSONB NOT NULL,
    medicines JSONB NOT NULL,
    paid_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

COPY symptoms(id, name) FROM '/docker-entrypoint-initdb.d/symptoms.csv' WITH CSV HEADER;
COPY tests(id, name, price) FROM '/docker-entrypoint-initdb.d/tests.csv' WITH CSV HEADER;
COPY medicines(id, name, price) FROM '/docker-entrypoint-initdb.d/medicines.csv' WITH CSV HEADER;
