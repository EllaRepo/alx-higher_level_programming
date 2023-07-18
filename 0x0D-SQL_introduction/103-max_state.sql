-- Script that displays the max temperature of each state (ordered by State name).
-- Display the average temperatur by city ordered by temperature(dec)
SELECT state, MAX(value) AS max_temp
FROM temperatures
Group BY state
ORDER BY State;
