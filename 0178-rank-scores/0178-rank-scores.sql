# Write your MySQL query statement below
# Write your MySQL query statement below
SELECT score, DENSE_RANK()
OVER(
    order by score DESC
    ) AS 'rank'
FROM Scores