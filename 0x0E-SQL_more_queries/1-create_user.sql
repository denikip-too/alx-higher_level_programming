-- creates the MySQL server user user_0d_1 if only exist and set password to user_0d_1_pwd
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhoat' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
