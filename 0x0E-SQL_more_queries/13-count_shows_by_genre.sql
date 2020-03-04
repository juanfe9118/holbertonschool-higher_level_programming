-- Lists all genres in "hbtn_0d_tvshows"
-- Counts the shows linked to each genre
SELECT tv_genres.name AS genre, COUNT(*) AS number_of_shows FROM tv_show_genres LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id GROUP BY genre ORDER BY number_of_shows DESC;
