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

-- Check the data existense after player_names & player_stats table creation and executing the script insert_new_player_data.py
SELECT COUNT(*) FROM rankings_board.player_names;
SELECT COUNT(*) FROM rankings_board.player_names where country_code='IN';
SELECT * FROM rankings_board.player_names where country_code='IN' LIMIT 5;
SELECT * FROM rankings_board.player_stats WHERE unique_id = 'bbb235c5fc1eee0e1f367fe5' LIMIT 5;

-- Create the table player_ratings
CREATE TABLE IF NOT EXISTS rankings_board.player_ratings (
    unique_id VARCHAR(24) PRIMARY KEY,
    rating_points FLOAT
);

-- Check the existense of data at player_ratings after executing the script populate_player_ratings_one_time.py
SELECT COUNT(*) FROM rankings_board.player_ratings; -- should be 372551


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

-- Check for data
SELECT COUNT(*) FROM rankings_board.player_status_materialized;
SELECT * FROM rankings_board.player_status_materialized LIMIT 5;
