-- #1 
SELECT * FROM met LIMIT 10;
-- columns: id, department, category, title, artist, date, medium, country

-- #2
SELECT COUNT(*)
FROM met WHERE department = 'American Decorative Arts';

-- #3
SELECT category, COUNT(*)
FROM met WHERE category LIKE '%celery%';

-- #4
SELECT title, medium, date
FROM met WHERE date LIKE '%1600%';

-- #5
SELECT title, country, COUNT(*)
FROM met GROUP BY country ORDER BY COUNT(*) DESC LIMIT 10;

-- #6
SELECT category, COUNT(*)
FROM met GROUP BY category HAVING COUNT(*) > 100;

-- #7
SELECT medium, COUNT(*)
FROM met WHERE medium LIKE '%gold%' OR medium LIKE '%silver%' GROUP BY medium ORDER BY COUNT(*) DESC LIMIT 10;
