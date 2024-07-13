select count(*) from rankings_board.country_codes;

select count(*) from rankings_board.player_names;
select count(*) from rankings_board.player_stats;
select count(*) from rankings_board.player_status_materialized;


select * from rankings_board.player_stats limit 100;

-- Create new table 

-- CREATE TABLE IF NOT EXISTS rankings_board.player_ratings (
--     unique_id CHAR(64) PRIMARY KEY,
--     rating_points FLOAT
-- );

select count(*) from rankings_board.player_ratings;

-- 401766
-- 365173






