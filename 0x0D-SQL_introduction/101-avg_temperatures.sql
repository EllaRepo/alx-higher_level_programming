-- Script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending)
-- Display the average temperatur by city ordered by temperature(dec)
SELECT city, AVG(value) AS avg_temp
FROM temperatures
Group BY city
ORDER BY avg_temp DESC;
