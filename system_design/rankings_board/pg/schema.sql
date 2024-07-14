-- Create the schema (if it does not already exist)
CREATE SCHEMA IF NOT EXISTS rankings_board;

-- Create the country_codes table (if it does not already exist)
CREATE TABLE IF NOT EXISTS rankings_board.country_codes (
    country_name VARCHAR(255) NOT NULL,
    country_code CHAR(2) PRIMARY KEY
);

-- Create the player_names table (if it does not already exist)
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

-- Create the table player_ratings
CREATE TABLE IF NOT EXISTS rankings_board.player_ratings (
    unique_id CHAR(64) PRIMARY KEY,
    rating_points FLOAT
);


-- Verify the creation
\dt rankings_board.*
\d rankings_board.country_codes
\d rankings_board.player_names
\d rankings_board.player_stats
\d rankings_board.rating_points



-- Material view of the players information to determine wether they are retired or not
CREATE MATERIALIZED VIEW rankings_board.player_status_materialized AS
SELECT 
    unique_id,
    DATE_PART('year', AGE(DOB)) AS player_age,
    CASE 
        WHEN DATE_PART('year', AGE(DOB)) >= 40 THEN 'Retired'
        ELSE 'Active'
    END AS status
FROM 
    rankings_board.player_names;


------------------- notification mechanism in the event of player stats update---------------------
DROP FUNCTION notify_player_update;

-- Function creation

CREATE OR REPLACE FUNCTION notify_player_update()
RETURNS TRIGGER AS $$
BEGIN
    PERFORM pg_notify('player_update', NEW.unique_id::text);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Drop existing triggers

DROP TRIGGER player_update_trigger ON rankings_board.player_stats;

-- Create new trigger

CREATE TRIGGER player_update_trigger
AFTER INSERT OR UPDATE OR DELETE ON rankings_board.player_stats
FOR EACH ROW
EXECUTE FUNCTION notify_player_update();