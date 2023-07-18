-- This script lists all records with a score >= 10 in the second_table table
-- Select the score and name columns from the second_table table where score >= 10, ordered by score
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
