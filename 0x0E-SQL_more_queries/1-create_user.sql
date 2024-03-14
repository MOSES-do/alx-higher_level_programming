-- creates MySQL server user `user_0d_1` w/ pswd, `user_0d_1_pwd`
-- if user_0d_1 already exists, the script should not fail
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
