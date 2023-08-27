# Write your MySQL query statement below

SELECT name
FROM SalesPerson AS s
WHERE s.sales_id NOT IN (SELECT Orders.sales_id
                         FROM Orders
                         LEFT JOIN Company
                         ON Orders.com_id = Company.com_id
                         WHERE name = "RED");