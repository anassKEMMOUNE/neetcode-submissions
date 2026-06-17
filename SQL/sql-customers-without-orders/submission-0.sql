-- Write your query below
SELECT name
FROM customers
WHERE name NOT IN (
SELECT customers.name
FROM customers
RIGHT JOIN orders
ON customers.id = orders.customer_id)