## Code
```sql
-- #1
SELECT * FROM trips;
SELECT * FROM riders;
SELECT * FROM cars;

-- #3
SELECT riders.first, riders.last, cars.model 
FROM riders CROSS JOIN cars;

-- #4
SELECT riders.first, riders.last, trips.pickup, trips.dropoff 
FROM trips LEFT JOIN riders ON trips.rider_id = riders.id;

-- #5
SELECT * FROM trips JOIN cars 
ON trips.car_id = cars.id;

-- #6
SELECT * FROM riders
UNION
SELECT * FROM riders2;

-- #7
SELECT ROUND(AVG(cost), 2) FROM trips;

-- #8
SELECT * FROM riders WHERE total_trips < 500
UNION
SELECT * FROM riders2 WHERE total_trips < 500;

-- #9
SELECT status, COUNT(*) FROM cars WHERE status = 'active';

-- #10
SELECT * FROM cars ORDER BY trips_completed DESC LIMIT 2;
```

<br>

## Results

### Question 1:
![](https://github.com/jeyla380/codecademy_projects/blob/main/datascience/sql/lyft_trip_data/results/q1_result.png)

### Question 3:
![](https://github.com/jeyla380/codecademy_projects/blob/main/datascience/sql/lyft_trip_data/results/q3_result.png)

### Question 4:
![](https://github.com/jeyla380/codecademy_projects/blob/main/datascience/sql/lyft_trip_data/results/q4_result.png)

### Question 5:
![](https://github.com/jeyla380/codecademy_projects/blob/main/datascience/sql/lyft_trip_data/results/q5_result.png)

### Question 6:
![](https://github.com/jeyla380/codecademy_projects/blob/main/datascience/sql/lyft_trip_data/results/q6_result.png)

### Question 7:
![](https://github.com/jeyla380/codecademy_projects/blob/main/datascience/sql/lyft_trip_data/results/q7_result.png)

### Question 8:
![](https://github.com/jeyla380/codecademy_projects/blob/main/datascience/sql/lyft_trip_data/results/q8_result.png)

### Question 9:
![](https://github.com/jeyla380/codecademy_projects/blob/main/datascience/sql/lyft_trip_data/results/q9_result.png)

### Question 10:
![](https://github.com/jeyla380/codecademy_projects/blob/main/datascience/sql/lyft_trip_data/results/q10_result.png)
