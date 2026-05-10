-- Business question: How is the business growing month over month?
-- This is the most fundamental e-commerce KPI

SELECT
    order_year,
    order_month,
    COUNT(DISTINCT order_id)        AS total_orders,
    ROUND(SUM(price), 2)            AS monthly_revenue,
    ROUND(AVG(price), 2)            AS avg_order_value,
    COUNT(DISTINCT customer_id)     AS unique_customers
FROM fact_orders
WHERE order_status = 'delivered'
GROUP BY order_year, order_month
ORDER BY order_year, order_month;
