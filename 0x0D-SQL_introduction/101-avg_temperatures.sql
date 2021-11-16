-- script that displays the average temperature by city ordered by temperature DESC
SELECT city, AVG(value) as avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;