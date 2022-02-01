-- import table to hbtn_0c_0 database
-- displays the average temperature (Fahrenheit) by city ordered by temperature (descending)
CREATE DATABASE hbtn_0c_0;
SELECT city, AVG(value) 'avg_temp' from temperatures GROUP BY city ORDER BY avg_temp DESC;
