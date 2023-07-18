-- script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)
-- Display top e cities temperature during July and August ordered by temperature(dec)
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month = 7 or month = 8
Group BY city
ORDER BY avg_temp DESC
LIMIT 3;
