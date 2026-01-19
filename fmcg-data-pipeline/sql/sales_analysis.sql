-- FMCG Sales Analysis
-- Dataset: Grocery Store Sales
-- Purpose: Exploratory analysis and KPI validation

-- 1. View sample data
SELECT *
FROM grocery_chain_data
LIMIT 10;


-- 2. Total sales by product
SELECT
    product_name,
    SUM(final_amount) AS total_sales
FROM grocery_chain_data
GROUP BY product_name
ORDER BY total_sales DESC
LIMIT 10;


-- 3. Total sales by store
SELECT
    store_name,
    SUM(final_amount) AS total_sales
FROM grocery_chain_data
GROUP BY store_name
ORDER BY total_sales DESC;


-- 4. Total sales by aisle
SELECT
    aisle,
    SUM(final_amount) AS total_sales
FROM grocery_chain_data
GROUP BY aisle
ORDER BY total_sales DESC;


-- 5. Daily sales trend
SELECT
    transaction_date,
    SUM(final_amount) AS daily_sales
FROM grocery_chain_data
GROUP BY transaction_date
ORDER BY transaction_date;


-- 6. Average transaction value
SELECT
    AVG(final_amount) AS avg_transaction_value
FROM grocery_chain_data;


-- 7. Sales for a specific store (filter example)
SELECT
    transaction_date,
    SUM(final_amount) AS store_daily_sales
FROM grocery_chain_data
WHERE store_name = 'SuperSave Central'
GROUP BY transaction_date
ORDER BY transaction_date;
