-- Write your query below
SELECT DISTINCT customer_id,customer_name
FROM (
SELECT customers.customer_id, customers.customer_name,orders.product_name
FROM customers
LEFT JOIN orders ON customers.customer_id = orders.customer_id)
GROUP BY customer_id,customer_name
HAVING COUNT(CASE WHEN product_name = 'A' THEN 1 END) > 0   
   AND COUNT(CASE WHEN product_name = 'B' THEN 1 END) > 0  
   AND COUNT(CASE WHEN product_name = 'C' THEN 1 END) = 0
ORDER BY customer_name;  
