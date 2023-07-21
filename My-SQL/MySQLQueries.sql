-- Query = question = ask for smth 

-- CRUD = Decribes Everything we can do with Data Ever

-- CRUD is an acronym for :Create READ , UPDATE , DELETE 


-- CREATE
-- SQL command : INSERT

-- SYNTAX : INSERT Into table_name (coolumn_name_1,coolumn_name_2) VALUES (value_1, value_2);

INSERT INTO users (first_name, last_name, email, password) VALUES('Jhon', 'wick', 'john@email.com')

--INSERT MANY 



-- ! READ 
-- SQL Command : SELECT 

-- SYNTAX : SELECT * column_name_1 , column_name_2 FROM table_name ;
-- SYNTAX : SELECT * column_name_1 , column_name_2 FROM table_name ;

SELECT * FROM users

SELECT * FROM users WHERE last_name = "jhon"

SELECT first_name, last_name FROM users WHERE id = 2;2;

SELECT * FROM users ORDER BY first_name DESC;

SELECT * FROM users ORDER BY first_name ASC;

SELECT * FROM users WHERE first_name LIKE "j%";

SELECT * FROM users ORDER BY id LIMIT 2; 

SELECT * FROM users WHERE id > 3 ; 

-- SYNTAX : UPDATE table_name SET column_name_1 = new_value2 , column_name_2 = new_value2 WHERE condition = id;

UPDATE user SET first_name = 'test', last_name = 'test' WHERE id = 3;




-- SYNTAX : DELETE FROM table_name WHERE condition 

DELETE FROM users WHERE last_name = 'wick';


INSERT INTO adresses (street , city , zip_code ) VALUES ('Jhon Street', 'Campton', '6155')


SELECT * FROM users JOIN adresses ON users.id = adresses.user_id;

INSERT INTO products (name, price, description) VALUES ("IPHONE", 1100.5,"Very Good Phone"),
("T-shirt"),("");



