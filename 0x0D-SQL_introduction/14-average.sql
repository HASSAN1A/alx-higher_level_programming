-- script that computes the  average score  of all records in the table
SELECT SUM(score)/COUNT(score) AS average FROM second_table;