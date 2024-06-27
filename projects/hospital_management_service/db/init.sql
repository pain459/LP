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
    name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS medicines (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS doctor_analysis_and_tests (
    id SERIAL PRIMARY KEY,
    patient_unique_id VARCHAR(64) NOT NULL,
    analysis JSONB NOT NULL,
    tests JSONB NOT NULL,
    medicines JSONB NOT NULL
);

CREATE INDEX idx_patient_unique_id ON doctor_analysis_and_tests (patient_unique_id);

INSERT INTO symptoms (name) VALUES
('flu'),
('cold'),
('cough'),
('fever')
ON CONFLICT DO NOTHING;

INSERT INTO tests (name) VALUES
('blood test'),
('x-ray'),
('mri'),
('covid test')
ON CONFLICT DO NOTHING;

INSERT INTO medicines (name) VALUES
('paracetamol'),
('ibuprofen'),
('antibiotic'),
('antihistamine')
ON CONFLICT DO NOTHING;
