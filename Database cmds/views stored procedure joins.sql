CREATE TABLE customers ( 
	customer_id INT PRIMARY KEY,
    name VARCHAR(50),
    city VARCHAR(50)
);
    
INSERT INTO customers VALUES 
(1, 'Alice', 'Mumbai'), 
(2, 'Bob', 'Delhi'), 
(3, 'Charlie', 'Bangalore'), 
(4, 'David', 'Mumbai');

CREATE TABLE orders ( 
	order_id INT PRIMARY KEY, 
    customer_id INT, 
    amount INT
); 
    
INSERT INTO orders 
VALUES
(101, 1, 500), 
(102, 1, 900), 
(103, 2, 300),
(104, 5, 700);

SELECT * FROM customers;
SELECT * FROM orders;

-- inner join 
SELECT * 
FROM customers c
INNER JOIN orders o
ON c.customer_id = o.customer_id;

-- left join 
SELECT * 
FROM customers c
LEFT JOIN orders o
ON c.customer_id = o.customer_id;

-- right join
SELECT * 
FROM customers c
RIGHT JOIN orders o
ON c.customer_id = o.customer_id;

-- Outer Join
SELECT * FROM customers as c
LEFT JOIN orders as O
ON c.customer_id = o.customer_id
UNION
SELECT * FROM customers as c
RIGHT JOIN orders as O
ON c.customer_id = o.customer_id;

-- Cross join
SELECT * 
FROM customers
CROSS JOIN orders;


-- Self Join
SELECT *
FROM customers as A
JOIN customers as B
ON A.customer_id = B.customer_id; 

-- Left Exclusive join
 SELECT * 
 FROM customers as c
 LEFT JOIN orders as o
 ON c.customer_id = o.customer_id
 WHERE o.customer_id IS NULL;
 
 -- Right Exclusive join 
 SELECT * 
 FROM customers as c
 RIGHT JOIN orders as o
 ON c.customer_id = o.customer_id
 WHERE c.customer_id IS NULL;
 
 -- Sub Queries
SELECT *
FROM orders
WHERE amount > (
	SELECT AVG(amount)
    FROM orders
);


SELECT name,
	( SELECT COUNT(*)
		FROM orders o
		WHERE o.customer_id = c.customer_id
	)as order_count
FROM customers c;


SELECT 
	summary.customer_id, 
	summary.avg_amount
FROM 
	(
		SELECT 
			customer_id, 
            AVG(amount) as avg_amount
		FROM orders
		GROUP BY customer_id
	) as summary;


-- Views in SQL
CREATE VIEW view1 AS
SELECT customer_id, name FROM customers; 

SELECT * FROM view1;

-- View with inner join
CREATE VIEW view2 AS
SELECT c.customer_id, c.name,o.order_id
FROM customers as c
INNER JOIN orders as o
ON c.customer_id = o.customer_id;

DESC customers;

SELECT * FROM view2;

DROP VIEW view1; 



CREATE TABLE accounts(
	account_id INT PRIMARY KEY,
	name VARCHAR(30),
	balance DECIMAL(10, 2),
	branch VARCHAR(50)
);

INSERT INTO accounts
VALUES
(1,"Adam",500.00,"Mumbai"),
(2,"Bob",300.00,"Delhi"),
(3,"Charlie",700.00,"Banglore"),
(4,"David",1000.00,"Noida");	 

CREATE INDEX idx_branch
ON accounts(branch);

SHOW INDEX FROM accounts;




-- Composite index 
CREATE INDEX idx2
ON accounts(branch,balance);

DROP INDEX idx2 ON accounts;


DELIMITER $$

CREATE PROCEDURE check_balance(IN acc_id INT, OUT bal DECIMAL(10, 2))
BEGIN
	SELECT balance INTO bal
    FROM accounts
    WHERE account_id = acc_id;
END$$
DELIMITER ;

CALL check_balance(1, @balance);
SELECT @balance;

DROP PROCEDURE IF EXISTS check_balance;