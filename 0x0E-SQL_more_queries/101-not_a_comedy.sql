-- lists all shows without the genre Comedy in the database hbtn_0d_tvshows
SELECT tv_shows.title FROM tv_genres JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id WHERE tv_genres.name <> Comedy ORDER BY tv_shows.title ASC;
