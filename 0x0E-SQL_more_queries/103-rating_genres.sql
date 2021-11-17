-- lists all genres in the database hbtn_0d_tvshows_rate by their rating by joining.
SELECT d.name, SUM(b.rate) AS rating FROM tv_genres d
       LEFT JOIN tv_show_genres c ON d.id = c.genre_id
       LEFT JOIN tv_show_ratings b ON c.show_id = b.show_id
GROUP BY d.name ORDER BY rating DESC, d.name;