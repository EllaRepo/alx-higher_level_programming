-- Script lists the number of records with the same score in the second_table table
-- Select the score and count of records with that score, with column labels "score" and "number"
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY score DESC;
