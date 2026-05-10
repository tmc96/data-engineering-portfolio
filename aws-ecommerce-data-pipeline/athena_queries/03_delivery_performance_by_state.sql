-- Business question: Which regions have the worst delivery performance?
-- Late deliveries directly impact customer satisfaction scores

SELECT
    s.seller_state,
    COUNT(DISTINCT f.order_id)              AS total_orders,
    ROUND(AVG(CAST(f.delivery_delay_days AS DOUBLE)), 2)    AS avg_delay_days,
    ROUND(
        SUM(CASE WHEN f.is_late_delivery = true THEN 1 ELSE 0 END) 
        * 100.0 / COUNT(*), 2
    )                                        AS late_delivery_pct,
    ROUND(AVG(CAST(f.review_score AS DOUBLE)), 2)           AS avg_review_score
FROM fact_orders f
JOIN dim_sellers s 
    ON f.seller_id = s.seller_id
WHERE f.order_status = 'delivered'
    AND f.delivery_delay_days IS NOT NULL
GROUP BY s.seller_state
HAVING COUNT(DISTINCT f.order_id) > 50
ORDER BY late_delivery_pct DESC;
