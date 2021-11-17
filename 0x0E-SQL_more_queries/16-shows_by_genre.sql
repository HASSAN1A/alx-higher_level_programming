-- script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
SELECT a.title, b.name FROM tv_shows AS a
       LEFT JOIN tv_show_genres AS c on a.id = c.show_id
       LEFT JOIN tv_genres AS b on c.genre_id = b.id
ORDER BY a.title ASC, b.name ASC;