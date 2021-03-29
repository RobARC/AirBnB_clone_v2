-- Script that prepares a MySQL server for the project
-- database hbnb_test_db

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
USE hbnb_test_db;
GRANT ALL PRIVILEGES ON hbnb_test_db . * TO hbnb_test @localhost IDENTIFIED BY 'hbnb_test_pwd';
GRANT SELECT ON performance_schema . * TO hbnb_test @localhost;
FLUSH PRIVILEGES;
