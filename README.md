# MeerKAT S-band Survey Database
A dash-based frontend that interacts with a MySQL backend. 

## How to set up the MySQL database
1. Install MySQL using

    sudo apt install mysql-server

2. Secure your installation with 

    sudo mysql\_secure\_installation

3. Enter MySQL with

    mysql -u root -p

4. Create a non-root account

    create user 'reader'@'localhost' identified by 'PASSWORD';

5. Create a database with

    CREATE DATABASE meerkat;

6. Create a table inside this database

    CREATE TABLE meerkat (name varchar(20), obs_date DATE, status varchar(20));

7. Give read and edit access to user reader

    GRANT SELECT, UPDATE ON meerkat.meerkat TO 'reader'@'localhost';

8. As root, you can add pointings to meerkat.meerkat with

     INSERT INTO meerkat(name, status) values('Point 3', 'None');

## Columns in the meerkat.meerkat table

| Column name | Description      | MySQL type |
| ----------- | ---------------- | ---------- |
| name        | Pointing name    | varchar    |
| obs_date    | Observation date | date       |
| status      | Current status   | varchar    |
