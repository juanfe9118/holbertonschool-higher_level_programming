-- Lists all cities in the database "hbtn_0d_usa"
-- Displayed as "cities.id" "cities.name" "states.name"
SELECT cities.id, cities.name, states.name FROM states RIGHT JOIN cities ON cities.state_id = states.id;
