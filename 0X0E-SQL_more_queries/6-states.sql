-- creates database `hbtn_0d_usa` and table `states` w/ description:
-- id INT unique, auto generated, can't be null & is a primary key
-- if database based already exists, script shouldn't fail
-- if table already exists, script shouldn't fail

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
	id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
	name VARCHAR(256) NOT NULL
	);
