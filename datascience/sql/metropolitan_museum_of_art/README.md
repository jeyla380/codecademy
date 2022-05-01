## Code
```sql
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
```

<br>

## Results

### Question 1:
![](https://github.com/jeyla380/codecademy_projects/blob/main/datascience/sql/metropolitan_museum_of_art/results/Q1_Result.png)

### Question 2:
![](https://github.com/jeyla380/codecademy_projects/blob/main/datascience/sql/metropolitan_museum_of_art/results/Q2_Result.png)

### Question 3:
![](https://github.com/jeyla380/codecademy_projects/blob/main/datascience/sql/metropolitan_museum_of_art/results/Q3_Result.png)

### Question 4:
![](https://github.com/jeyla380/codecademy_projects/blob/main/datascience/sql/metropolitan_museum_of_art/results/Q4_Result.png)

### Question 5:
![](https://github.com/jeyla380/codecademy_projects/blob/main/datascience/sql/metropolitan_museum_of_art/results/Q5_Result.png)

### Question 6:
![](https://github.com/jeyla380/codecademy_projects/blob/main/datascience/sql/metropolitan_museum_of_art/results/Q6_Result.png)

### Question 7:
![](https://github.com/jeyla380/codecademy_projects/blob/main/datascience/sql/metropolitan_museum_of_art/results/Q7_Result.png)
