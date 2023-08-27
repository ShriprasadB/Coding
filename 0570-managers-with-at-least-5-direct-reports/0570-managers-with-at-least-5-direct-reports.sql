# Write your MySQL query statement below

SELECT t1.name
FROM Employee as t1
JOIN
(SELECT managerId
    FROM Employee
    GROUP BY managerId
    HAVING COUNT(managerId) >= 5) as t2
ON t1.id = t2.managerId;