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


select * from rankings_board.player_ratings where unique_id = 'WS202407121720806958187ZEVLWE';

select * from rankings_board.player_stats where unique_id = 'WS202407121720806958187ZEVLWE';

select * from rankings_board.player_names where player_names.unique_id = 'WS202407121720806958187ZEVLWE'

select * from rankings_board.country_codes where country_codes.country_code = 'WS'

UPDATE rankings_board.player_stats
-- SET unique_id = unique_id
SET goals = 150
WHERE unique_id = 'WS202407121720806958187ZEVLWE';
