-- Create schema
CREATE SCHEMA IF NOT EXISTS rankings_board;

-- Create country codes table under rankings_board schema
CREATE TABLE IF NOT EXISTS rankings_board.country_codes (
    country_name VARCHAR(255) NOT NULL,
    country_code CHAR(2) PRIMARY KEY
);

-- Check the data existense after executing the script populate_country_codes.py
SELECT * FROM rankings_board.country_codes;
SELECT COUNT(*) FROM rankings_board.country_codes;


-- Create the player_names table (if it does not already exist)
DROP TABLE rankings_board.player_names;
DROP TABLE rankings_board.player_stats;

CREATE TABLE IF NOT EXISTS rankings_board.player_names (
    unique_id VARCHAR(24) PRIMARY KEY,  -- fixed length id will be generated.
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
    unique_id VARCHAR(24) PRIMARY KEY,
    matches INTEGER NOT NULL,
    goals INTEGER NOT NULL,
    assists INTEGER NOT NULL,
    fouls INTEGER NOT NULL,
    injuries INTEGER NOT NULL,
    FOREIGN KEY (unique_id) REFERENCES rankings_board.player_names(unique_id)
);

-- Check the data existense after player_names table creation and executing the script insert_new_player_data.py
SELECT COUNT(*) FROM rankings_board.player_names;
SELECT * FROM rankings_board.player_names where country_code='IN';