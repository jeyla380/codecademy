-- #1
SELECT * FROM transactions LIMIT 10;
-- columns: id, user_id, date, currency, money_in, money_out


-- #2
SELECT SUM(money_in)
FROM transactions;


-- #3
SELECT SUM(money_out)
FROM transactions;


-- #4
-- How many money_in transactions are in this table?
SELECT COUNT(money_in)
FROM transactions;

-- How many money_in transactions are in this table where ‘BIT’ is the currency?
SELECT COUNT(money_in)
FROM transactions WHERE currency = 'BIT';


-- #5
SELECT MAX(money_in)
FROM transactions;

SELECT MAX(money_out)
FROM transactions;


-- #6
SELECT AVG(money_in)
FROM transactions WHERE currency = 'ETH';


-- #7
SELECT date, AVG(money_in), AVG(money_out)
FROM transactions GROUP BY date;


-- #8
SELECT date, ROUND(AVG(money_in), 2) AS 'average_buy', ROUND(AVG(money_out), 2) AS 'average_sell'
FROM transactions GROUP BY date;
