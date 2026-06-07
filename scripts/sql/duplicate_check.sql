SELECT emp_id,
       COUNT(*)
FROM employees
GROUP BY emp_id
HAVING COUNT(*) > 1;
