CREATE TABLE users (
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  age INTEGER NOT NULL,
  country TEXT NOT NULL,
  phone TEXT NOT NULL,
  balance INTEGER NOT NULL
);

-- SELECT
SELECT first_name, age FROM users;
SELECT * FROM users;
SELECT rowid, first_name FROM users;

-- ORDER BY
SELECT first_name, age FROM users ORDER BY age ASC; 
SELECT first_name, age, balance FROM users 
ORDER BY age ASC, balance DESC;


-- SELECT DISTINCT
SELECT country FROM users;
SELECT DISTINCT country FROM users;
SELECT DISTINCT first_name,country FROM users ORDER BY country;

-- WHERE
SELECT first_name, age, balance FROM users WHERE age >= 30;
SELECT first_name, last_name FROM users WHERE first_name LIKE '%호%';

-- LIKE 
SELECT first_name FROM users WHERE first_name LIKE '%준';
SELECT first_name, phone FROM users WHERE phone LIKE '02-%';
SELECT first_name, age FROM users WHERE age LIKE '2_';
SELECT first_name, phone FROM users WHERE phone LIKE '%-51__-%';

-- IN
SELECT first_name, country FROM users WHERE country NOT IN ('경기도', '강원도');

-- BETWEEN
SELECT first_name, age FROM users WHERE age BETWEEN 20 AND 30;
SELECT first_name, age FROM users WHERE age >= 20 AND age <= 30;
SELECT first_name, age FROM users WHERE age NOT BETWEEN 20 AND 30;
SELECT first_name, age FROM users WHERE age < 20 OR age > 30;

-- LIMIT
SELECT rowid, first_name FROM users LIMIT 10;
SELECT first_name, balance FROM users ORDER BY balance DESC LIMIT 10;
SELECT first_name, age FROM users ORDER BY age LIMIT 5;
SELECT rowid, first_name FROM users LIMIT 10 OFFSET 10;

-- AGGREGATE FUNC
SELECT COUNT(*) FROM users;
SELECT AVG(age) FROM users WHERE age >= 30;
SELECT AVG(balance) FROM users WHERE age >= 30;

-- GROUP BY
SELECT country FROM users GROUP BY country;
SELECT country, COUNT(*) FROM users GROUP BY country;
SELECT last_name, COUNT(*) FROM users GROUP BY last_name;
SELECT last_name, COUNT(*) AS number_of_name FROM users GROUP BY last_name;
SELECT last_name, COUNT(*) FROM users GROUP BY last_name ORDER BY COUNT(*) DESC;
SELECT country, AVG(age) FROM users GROUP BY country;



-- CREATE
CREATE TABLE classmates (
  name TEXT NOT NULL,
  age INTEGER NOT NULL,
  address TEXT NOT NULL
);

-- INSERT
INSERT INTO classmates (name, age, address)
VALUES ('홍길동', 23, '서울');

INSERT INTO classmates
VALUES ('홍길동', 23, '서울');

INSERT INTO classmates
VALUES 
  ('김철수', 30, '경기'),
  ('이영미', 31, '강원'),
  ('박진성', 26, '전라'),
  ('최지수', 12, '충청'),
  ('정요한', 28, '경상');

-- UPDATE
UPDATE classmates SET name='김철수한무두루미', address='제주도' WHERE rowid = 2;
SELECT rowid, * FROM classmates;

-- DELETE
DELETE FROM classmates WHERE rowid = 5;
DELETE FROM classmates WHERE name LIKE '%영%';
DELETE FROM classmates;
