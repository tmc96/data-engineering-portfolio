-- Business question: Who are our best performing sellers?
-- Useful for seller incentive programs and partnership decisions

SELECT
    f.seller_id,
    s.seller_state,
    COUNT(DISTINCT f.order_id)              AS total_orders,
    ROUND(SUM(f.price), 2)                  AS total_revenue,
    ROUND(AVG(CAST(f.review_score AS DOUBLE)), 2)           AS avg_review_score,
    ROUND(AVG(CAST(f.delivery_delay_days AS DOUBLE)), 2)    AS avg_delay_days,
    ROUND(
        SUM(CASE WHEN f.is_late_delivery = true THEN 1 ELSE 0 END) 
        * 100.0 / COUNT(*), 2
    )                                        AS late_delivery_pct,
    ROUND(AVG(f.freight_ratio), 2)          AS avg_freight_ratio_pct
FROM fact_orders f
JOIN dim_sellers s 
    ON f.seller_id = s.seller_id
WHERE f.order_status = 'delivered'
GROUP BY f.seller_id, s.seller_state
HAVING COUNT(DISTINCT f.order_id) > 20
ORDER BY total_revenue DESC
LIMIT 10;
