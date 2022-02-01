-- lists records in desc order of the table second_table where name column is not null
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
