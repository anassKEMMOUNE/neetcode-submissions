-- Write your query below
SELECT u.name,CASE WHEN sum(r.distance) is NULL THEN 0 ELSE sum(r.distance) END as travelled_distance
FROM rides r
RIGHT JOIN users u ON r.user_id=u.id
GROUP by name
ORDER BY travelled_distance DESC ,name ASC