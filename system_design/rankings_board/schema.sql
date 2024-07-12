-- Create the schema (optional, PostgreSQL uses public schema by default)
CREATE SCHEMA rankings_board;

-- Create the country_codes table
CREATE TABLE country_codes (
    country_name VARCHAR(255) NOT NULL,
    country_code CHAR(2) PRIMARY KEY
);

-- Create the player_names table
CREATE TABLE player_names (
    unique_id CHAR(64) PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    middle_name VARCHAR(255),
    last_name VARCHAR(255) NOT NULL,
    country_code CHAR(2),
    FOREIGN KEY (country_code) REFERENCES country_codes(country_code)
);
