-- Business question: Which product categories generate the most revenue?
-- This tells us where to focus marketing and inventory investment

SELECT 
    p.product_category_name,
    COUNT(DISTINCT f.order_id)          AS total_orders,
    ROUND(SUM(f.price), 2)              AS total_revenue,
    ROUND(AVG(f.price), 2)              AS avg_order_value,
    ROUND(SUM(f.freight_value), 2)      AS total_freight_cost
FROM fact_orders f
-- Join to dimension table to get category name
JOIN dim_products p 
    ON f.product_id = p.product_id
-- Only include delivered orders for accurate revenue figures
WHERE f.order_status = 'delivered'
GROUP BY p.product_category_name
ORDER BY total_revenue DESC
LIMIT 10;
