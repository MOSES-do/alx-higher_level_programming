-- creates table `force_name` with given description
-- force_name description:
-- 	id INT
-- 	name VARCHAR(256) can't be null
-- if table already exists, script shouldn't fail

CREATE TABLE IF NOT EXISTS force_name (
	id INT,
	name VARCHAR(256) NOT NULL
	);
