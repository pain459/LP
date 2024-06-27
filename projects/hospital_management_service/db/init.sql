CREATE TABLE IF NOT EXISTS patients (
    patient_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    gender VARCHAR(10) NOT NULL,
    address TEXT,
    contact VARCHAR(15) UNIQUE NOT NULL,
    unique_id VARCHAR(64) UNIQUE NOT NULL
);
