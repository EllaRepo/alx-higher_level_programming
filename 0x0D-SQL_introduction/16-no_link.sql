-- Script that lists all records with a non-empty name value in the second_table table
-- Select the score and name columns from the second_table table where name is not empty, ordered by score
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
