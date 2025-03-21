-- Retrieves all shows and their linked genres from the database hbtn_0d_tvshows
-- Selects all rows from one table that are linked to another table
SELECT title, name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY title ASC, name ASC;
