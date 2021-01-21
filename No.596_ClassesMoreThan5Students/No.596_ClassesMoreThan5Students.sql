# Write your MySQL query statement below

WITH result AS (
SELECT class,count(DISTINCT student) As nums FROM courses
GROUP BY class
)
SELECT class FROM result WHERE nums >= 5

