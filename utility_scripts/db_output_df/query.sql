-- SELECT * FROM your_table;

SELECT 
    u.name, 
    u.email, 
    COUNT(o.order_id) AS total_orders, 
    SUM(o.amount) AS total_amount_spent,
    AVG(o.amount) AS avg_order_value
FROM 
    users u
LEFT JOIN 
    orders o ON u.user_id = o.user_id
GROUP BY 
    u.user_id, u.name, u.email
HAVING 
    SUM(o.amount) > 200
ORDER BY 
    total_amount_spent DESC;
