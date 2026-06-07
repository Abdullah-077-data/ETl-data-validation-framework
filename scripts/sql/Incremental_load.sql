SELECT *
FROM customers
WHERE last_updated_date >
(
    SELECT MAX(last_updated_date)
    FROM target_customers
);
