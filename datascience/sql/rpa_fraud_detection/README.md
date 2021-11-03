## Schema
![](https://github.com/jeyla380/codecademy_projects/blob/main/datascience/sql/rpa_fraud_detection/rpa_fraud_detection_schema.PNG)

<br>

## Code

```sql
-- 1
-- What are the column names?
SELECT * FROM transaction_data 
LIMIT 10;

-- 2
-- Find the full_names and emails
-- of the transactions listing 20252 as the zip code.
SELECT full_name, email, zip FROM transaction_data
WHERE zip = 20252;

-- 3
-- Use a query to find the names 
-- and emails associated with these transactions.
SELECT full_name, email FROM transaction_data
WHERE full_name = 'Art Vandelay' OR full_name LIKE '% der %';

-- 4
-- Find the ip_addresses and emails listed with these transactions.
SELECT ip_address, email FROM transaction_data
WHERE ip_address LIKE '10.%';

-- 5
-- Find the emails in transaction_data with
-- ‘temp_email.com’ as a domain.
SELECT email FROM transaction_data
WHERE email LIKE '%temp_email.com';

-- 6
-- The finance department is looking for a specific transaction. 
-- They know that the transaction occurred from an ip address starting 
-- with ‘120.’ and their full name starts with ‘John’.
-- Can you find the transaction?
SELECT full_name, ip_address FROM transaction_data
WHERE full_name LIKE 'John%' AND ip_address LIKE '120.%';

-- 7
-- Challenge
-- Return only those customers residing in GA. Use the list of ZIP CODE prefixes
-- (https://en.wikipedia.org/wiki/List_of_ZIP_Code_prefixes)
-- to determine the best query for zip codes belonging to Georgia(GA).
SELECT full_name, email, zip FROM transaction_data
WHERE zip BETWEEN 30000 AND 31999;
```

<br>

## Results
### Question 1: ![](https://github.com/jeyla380/codecademy_projects/blob/main/datascience/sql/rpa_fraud_detection/results/test_q1_result.PNG)

### Question 2: ![](https://github.com/jeyla380/codecademy_projects/blob/main/datascience/sql/rpa_fraud_detection/results/test_q2_result.PNG)

### Question 3: ![](https://github.com/jeyla380/codecademy_projects/blob/main/datascience/sql/rpa_fraud_detection/results/test_q3_result.PNG)

### Question 4: ![](https://github.com/jeyla380/codecademy_projects/blob/main/datascience/sql/rpa_fraud_detection/results/test_q4_result.PNG)

### Question 5: ![](https://github.com/jeyla380/codecademy_projects/blob/main/datascience/sql/rpa_fraud_detection/results/test_q5_result.PNG)

### Question 6: ![](https://github.com/jeyla380/codecademy_projects/blob/main/datascience/sql/rpa_fraud_detection/results/test_q6_result.PNG)

### Question 7 (Challenge): ![](https://github.com/jeyla380/codecademy_projects/blob/main/datascience/sql/rpa_fraud_detection/results/test_q7_result.PNG)
