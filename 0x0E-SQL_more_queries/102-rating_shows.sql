-- lists all shows from hbtn_0d_tvshows_rate by their rating in dscending order
SELECT a.title, sum(b.rate) AS rating FROM tv_shows a
       LEFT JOIN tv_show_ratings b ON a.id = b.show_id
GROUP BY a.title ORDER BY rating DESC, a.title;