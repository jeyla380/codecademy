-- 1
-- What are the column names?
SELECT * FROM users
LIMIT 20;
 
-- 2
-- Find the email addresses and birthdays of users whose 
-- birthday is between 1980-01-01 and 1989-12-31.
SELECT email, birthday FROM users
WHERE birthday BETWEEN '1980-01-01' AND '1989-12-31'
LIMIT 30;
   
-- 3
-- Find the emails and creation date of users 
-- whose created_at date matches this condition.
SELECT email, created_at FROM users
WHERE created_at < '2017-05-01'
LIMIT 25;

-- 4
-- Find the emails of the users who received the ‘bears’ test.
SELECT email, test FROM users
WHERE test = 'bears'
LIMIT 20;

-- 5
-- Find all the emails of all users who 
-- received a campaign on website BBB.
SELECT email, campaign FROM users
WHERE campaign LIKE 'BBB%'
LIMIT 20;

-- 6
-- Find all the emails of all users who received ad copy 2 in their campaign.
SELECT email, campaign FROM users
WHERE campaign LIKE '%-2'
LIMIT 20;

-- 7
-- Find the emails for all users who received both a campaign and a test. 
-- These users will have non-empty entries in the campaign and test columns.
SELECT email, campaign, test FROM users
WHERE campaign IS NOT NULL AND test IS NOT NULL
LIMIT 20;

-- 8
-- Challenge
-- One of the members of the marketing team had an idea of calculating how old users were when they signed up.

-- Turn the date into a decimal, subtract the numbers, then turn the numbers back into INT (so it's not a float)
SELECT email, created_at, birthday, cast(strftime('%Y.%m%d', created_at) - strftime('%Y.%m%d', birthday) AS int) AS age FROM users
LIMIT 20;
