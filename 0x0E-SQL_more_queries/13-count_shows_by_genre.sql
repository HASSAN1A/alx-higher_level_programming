-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT x.name AS genre, count(y.show_id) AS number_of_shows
       FROM tv_genres AS x INNER JOIN tv_show_genres AS y on x.id = y.genre_id
       	    GROUP BY genre ORDER BY number_of_shows DESC;