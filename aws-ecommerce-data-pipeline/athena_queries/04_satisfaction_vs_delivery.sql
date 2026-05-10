-- Business question: Does late delivery actually hurt review scores?
-- Quantifies the business impact of logistics on customer experience

SELECT
    -- Group orders by whether they were late or not
    CASE 
        WHEN is_late_delivery = true  THEN 'Late'
        WHEN is_late_delivery = false THEN 'On Time'
        ELSE 'Not Delivered'
    END                                     AS delivery_status,
    COUNT(DISTINCT order_id)                AS total_orders,
    ROUND(AVG(CAST(review_score AS DOUBLE)), 2)             AS avg_review_score,
    -- Distribution of review scores
    SUM(CASE WHEN CAST(review_score AS INT) = 5 THEN 1 ELSE 0 END) AS five_star,
    SUM(CASE WHEN CAST(review_score AS INT) = 4 THEN 1 ELSE 0 END) AS four_star,
    SUM(CASE WHEN CAST(review_score AS INT) = 3 THEN 1 ELSE 0 END) AS three_star,
    SUM(CASE WHEN CAST(review_score AS INT) = 2 THEN 1 ELSE 0 END) AS two_star,
    SUM(CASE WHEN CAST(review_score AS INT) = 1 THEN 1 ELSE 0 END) AS one_star
FROM fact_orders
WHERE review_score IS NOT NULL
GROUP BY is_late_delivery
ORDER BY avg_review_score DESC;
