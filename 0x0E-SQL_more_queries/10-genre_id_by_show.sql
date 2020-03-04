-- lists all shows from "hbtn_0d_tvshows" that have at least one genre linked
-- The database is imported to the SQL server
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id WHERE tv_show_genres.genre_id IS NOT NULL ORDER BY tv_shows.title, tv_show_genres.genre_id;
