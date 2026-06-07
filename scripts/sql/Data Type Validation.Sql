#customer_id should never be null
SELECT customer_id
FROM customers
WHERE customer_id IS NULL;
