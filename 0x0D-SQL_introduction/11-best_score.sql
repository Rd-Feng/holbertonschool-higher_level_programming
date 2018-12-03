-- list all rows in the table second_table
-- ordered by score desc
-- display rows with score >= 10
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
