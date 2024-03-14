-- creates table unique_id with description:
-- id INT w/ default value 1 and must be unique
-- name VARCHAR(256)
-- db name will be passed as arg of mysql command
-- if table already exists, script shouldn't fail

CREATE TABLE IF NOT EXISTS unique_id (
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
	);
