-- creates database `hbtn_0d_2` and user `user_0d_2`
-- `user_0d_2` should only have SELECT privilege in the database
-- `user_0d_2` password should be set to `user_0d_2_pwd`
-- if database based already exists, script shouldn't fail
-- if user `user_0d_2` already exists, script shouldn't fail

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
