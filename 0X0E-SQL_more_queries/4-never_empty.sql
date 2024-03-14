-- creates table id_not_null with description:
-- id INT with default value 1
-- name VARCHAR(256)
-- db name will be passed as argument of mysql command
-- if table already exists, script shouldn't fail

CREATE TABLE IF NOT EXISTS id_not_null (
	id INT DEFAULT 1,
	name VARCHAR(256)
	);
