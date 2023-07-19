--script that lists all privileges of the MySQL users
--Query to list all privileges of the MySQL users
SELECT *
FROM mysql.user
WHERE User IN ('user_0d_1', 'user_0d_2')
    AND Host = 'localhost';
