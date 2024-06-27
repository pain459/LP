CREATE TABLE IF NOT EXISTS patients (
    patient_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    gender VARCHAR(10),
    address TEXT,
    contact VARCHAR(15)
);
