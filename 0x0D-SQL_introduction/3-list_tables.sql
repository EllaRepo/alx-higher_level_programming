-- Script that lists all tables in a database

-- Set the database name as a variable
SET @dbName = 'mysql';

-- Show the names of all tables in the database
SELECT table_name
FROM information_schema.tables
WHERE table_schema = @dbName;
