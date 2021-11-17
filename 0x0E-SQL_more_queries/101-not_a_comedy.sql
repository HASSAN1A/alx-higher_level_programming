SELECT a.title FROM tv_shows AS a
       LEFT JOIN
       	    (SELECT tv_shows.id FROM tv_genres
     	    	    JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
     		    JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
     		    WHERE tv_genres.name = 'Comedy') b

	ON a.id = b.id
WHERE b.id IS NULL
ORDER BY a.title ASC;