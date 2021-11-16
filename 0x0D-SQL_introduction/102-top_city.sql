-- script that displays the top 3 of cities WITH THEIR temperature during July and August ordered by temperature IN DESCENDING ORDER
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month=7 OR month=8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;