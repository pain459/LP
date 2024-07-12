-- Create the schema
CREATE SCHEMA rankings_board;

-- Create the country_codes table
CREATE TABLE rankings_board.country_codes (
    country_name VARCHAR(255) NOT NULL,
    country_code CHAR(2) PRIMARY KEY
);

-- Create the player_names table
CREATE TABLE rankings_board.player_names (
    unique_id CHAR(64) PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    middle_name VARCHAR(255),
    last_name VARCHAR(255) NOT NULL,
    country_code CHAR(2),
    DOB DATE NOT NULL,
    Sex CHAR(1) CHECK (Sex IN ('M', 'F')),
    FOREIGN KEY (country_code) REFERENCES rankings_board.country_codes(country_code)
);

-- Verify the creation
\dt rankings_board.*
\d rankings_board.country_codes
\d rankings_board.player_names
