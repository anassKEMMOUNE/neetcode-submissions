-- Write your query below
SELECT s.name as name
FROM
(
SELECT o.sales_id,c.name as company_name
FROM orders o
LEFT JOIN company c on o.com_id = c.com_id
 ) j
RIGHT JOIN sales_person s on j.sales_id = s.sales_id
GROUP BY s.sales_id
HAVING SUM(CASE WHEN company_name = 'CRIMSON' then 1 Else 0 END) = 0
ORDER By name