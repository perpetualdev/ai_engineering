CREATE DATABASE IF NOT EXISTS backend_db;

CREATE TABLE user (
	id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);

USE backend_db;

INSERT INTO user 
VALUES
("Sam Larry", "sam@gmail.com", "sam123"),
("Sam Ayomide", "ayomide@gmail.com", "ayo123");