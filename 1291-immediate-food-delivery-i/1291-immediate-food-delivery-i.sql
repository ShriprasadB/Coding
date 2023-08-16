# Write your MySQL query statement below
# Write your MySQL query statement below

SELECT ROUND(
    COUNT(delivery_id)
    /
    (SELECT COUNT(DISTINCT delivery_id)FROM delivery)*100,
    2) as immediate_percentage
FROM delivery
WHERE order_date = customer_pref_delivery_date