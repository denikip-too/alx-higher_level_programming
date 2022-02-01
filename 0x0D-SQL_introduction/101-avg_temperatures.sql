-- displays the average temperature by city ordered by temperature in descending
SELECT city, AVG(value) 'avg_temp' FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
