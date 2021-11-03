## Schema
![](https://github.com/jeyla380/codecademy_projects/blob/main/datascience/sql/new_york_restaurants/new_york_restaurant_schema.PNG)

<br>

## Code

```sql
SELECT *,
  CASE
    WHEN review > 4.5 THEN 'Extraordinary'
    WHEN review > 4 THEN 'Excellent'
    WHEN review > 3 THEN 'Good'
    WHEN review > 2 THEN 'Fair'
    ELSE 'Poor'
  END AS 'rating'
FROM nomnom LIMIT 20;
```


<br>

## Result
![](https://github.com/jeyla380/codecademy_projects/blob/main/datascience/sql/new_york_restaurants/query_results.PNG)
