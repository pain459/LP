-- Create the schema (if it does not already exist)
CREATE SCHEMA IF NOT EXISTS rankings_board;

-- Create the country_codes table (if it does not already exist)
CREATE TABLE IF NOT EXISTS rankings_board.country_codes (
    country_name VARCHAR(255) NOT NULL,
    country_code CHAR(2) PRIMARY KEY
);

-- Create the player_names table (if it does not already exist)
CREATE TABLE IF NOT EXISTS rankings_board.player_names (
    unique_id CHAR(64) PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    middle_name VARCHAR(255),
    last_name VARCHAR(255) NOT NULL,
    country_code CHAR(2),
    DOB DATE NOT NULL,
    Sex CHAR(1) CHECK (Sex IN ('M', 'F')),
    FOREIGN KEY (country_code) REFERENCES rankings_board.country_codes(country_code)
);

-- Create the player_stats table
CREATE TABLE IF NOT EXISTS rankings_board.player_stats (
    unique_id CHAR(64) PRIMARY KEY,
    matches INTEGER NOT NULL,
    goals INTEGER NOT NULL,
    assists INTEGER NOT NULL,
    fouls INTEGER NOT NULL,
    injuries INTEGER NOT NULL,
    FOREIGN KEY (unique_id) REFERENCES rankings_board.player_names(unique_id)
);

-- Verify the creation
\dt rankings_board.*
\d rankings_board.country_codes
\d rankings_board.player_names
\d rankings_board.player_stats
