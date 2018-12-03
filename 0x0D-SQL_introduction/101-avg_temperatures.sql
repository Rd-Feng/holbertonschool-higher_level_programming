-- display average temperature by city
-- order by temperature desc
-- from table temperatures
SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
