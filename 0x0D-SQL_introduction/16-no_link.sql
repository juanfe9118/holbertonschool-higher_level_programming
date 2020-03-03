-- Lists all records of "second_table" that have a name field and sorted by score.
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
