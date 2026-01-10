/*
===========================================================
Author: Tanvi Chinnapa
Purpose: SQL practice examples covering joins, aggregations,
         window functions, subqueries, and analytics queries.
Source: Inspired by Alex the Analyst SQL tutorials
===========================================================
*/


-- =========================================================
-- 1. BASIC SELECT & FILTERING
-- =========================================================

-- Retrieve all employee data with salary above 50000
SELECT *
FROM employee_salary
WHERE salary > 50000;

-- =========================================================
-- 2. AGGREGATIONS
-- =========================================================

-- Maximum, average age of male and female, number of men and women
SELECT gender, 
       AVG(age) AS avg_age,
       MAX(age) AS oldest,
       COUNT(age) AS gender_count
FROM employee_demographics
GROUP BY gender;

-- =========================================================
-- 3. JOINS
-- =========================================================

-- Join employee demographics with employee salary
SELECT dem.employee_id,
       age,
       occupation
FROM employee_demographics AS dem
JOIN employee_salary AS sal
       ON dem.employee_id = sal.employee_id;

-- =========================================================
-- 4. CONDITIONAL LOGIC
-- =========================================================

--Determine pay increase 
SELECT first_name, 
       last_name, 
       salary,
CASE
       WHEN salary < 50000 THEN salary + (salary * 0.05)
       WHEN salary > 50000 THEN salary + (salary * 0.07)
       ELSE 'Same salary'
END AS new_salary
FROM employee_salary;

-- =========================================================
-- 5. SUBQUERIES
-- =========================================================

-- Retrieve employee details based on employee ID
SELECT *
FROM employee_demographics
WHERE employee_id IN
		(SELECT employee_id
		    FROM employee_salary
		    WHERE dept_id = 1);

-- =========================================================
-- 6. WINDOW FUNCTIONS
-- =========================================================

-- Average salary based on gender
SELECT
      dem.first_name,
      dem.last_name, 
      gender, 
      AVG(salary) OVER(PARTITION BY gender)
FROM employee_demographics dem
JOIN employee_salary sal
	ON dem.employee_id = sal.employee_id;

--Running total of salary 
SELECT
      dem.first_name,
      dem.last_name, 
      gender, 
      SUM(salary) OVER(PARTITION BY gender ORDER BY dem.employee_id) AS Running_total
FROM employee_demographics dem
JOIN employee_salary sal
	ON dem.employee_id = sal.employee_id;

--Ranking salary of employees
SELECT
      dem.first_name,
      dem.last_name, 
      gender, 
      RANK() OVER(PARTITION BY gender ORDER BY salary DESC) AS salary_rank
FROM employee_demographics dem
JOIN employee_salary sal
	ON dem.employee_id = sal.employee_id;

-- =========================================================
-- 7. CTEs
-- =========================================================

--Average of the salary from the new table 
WITH CTE_Example AS
(
SELECT gender, 
       AVG(salary) avg_sal, 
       MAX(salary) max_sal, 
       MIN(salary) min_sal, 
       COUNT(salary) count_sal
FROM employee_demographics
JOIN employee_salary sal
	ON dem.employee_id = sal.employee_id
GROUP BY gender
)
SELECT AVG(avg_sal)
FROM CTE_Example;

-- =========================================================
-- 8. DATA QUALITY CHECKS
-- =========================================================

--Checking for NULL values
SELECT *
FROM employee_demographics
WHERE employee_id IS NULL;

-- =========================================================
-- 9. DATE ANALYSIS
-- =========================================================

--Employee joining month
SELECT
    DATE_TRUNC('month', joining_date) AS month,
FROM employee_demographics
ORDER BY month;

-- =========================================================
-- END OF FILE
-- =========================================================