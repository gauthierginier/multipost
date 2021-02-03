DROP DATABASE IF EXISTS multipost;
CREATE DATABASE IF NOT EXISTS multipost DEFAULT CHARACTER SET utf8;
USE multipost;
CREATE TABLE client (
    id INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
    entreprise INT,
    nom TEXT,
    email TEXT,
    tel TEXT,
    adresse TEXT,
    codepostal TEXT,
    ville TEXT);
CREATE TABLE facture (
    id INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
    numclient INT,
    emission TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total INT DEFAULT 0,
    FOREIGN KEY (numclient) REFERENCES client(id)
);
CREATE TABLE lignes (
    id INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
    nomprod TEXT,
    refsku TEXT,
    quant INT,
    pu FLOAT,
    numfacture INT,
    FOREIGN KEY (numfacture) REFERENCES facture(id));

CREATE USER IF NOT EXISTS 'machine'@'192.168.1.62' IDENTIFIED WITH mysql_native_password BY 'aZeRtY123!';
GRANT ALL ON multipost.* TO 'machine'@'192.168.1.62';
FLUSH PRIVILEGES;

SHOW DATABASES; 
SHOW TABLES;
select user,host from mysql.user;