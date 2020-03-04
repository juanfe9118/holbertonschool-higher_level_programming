-- Creates the table "unique_id"
-- Where id is 1 by default and it is unique always
CREATE TABLE IF NOT EXISTS unique_id(id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
