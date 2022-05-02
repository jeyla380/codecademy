-- #1
SELECT * FROM state_climate LIMIT 5;

-- #2
SELECT state, year, tempf, AVG(tempf) OVER (
  PARTITION BY state
  ORDER BY year
) AS 'running_avg_temp'
FROM state_climate WHERE state = 'Alabama';

-- #3
SELECT state, year, tempf, FIRST_VALUE(tempf) OVER (
  PARTITION BY state
  ORDER BY tempf
) AS 'lowest_temp'
FROM state_climate WHERE state = 'Alabama';

-- #4
SELECT state, year, tempf, LAST_VALUE(tempf) OVER (
  PARTITION BY state
  ORDER BY tempf
  RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
) AS 'highest_temp'
FROM state_climate WHERE state = 'Alabama';

-- #5
SELECT state, year, tempf, LAG(tempf, 1, 0) OVER (
  PARTITION BY state
  ORDER BY year
) - tempf AS 'change_in_temp'
FROM state_climate ORDER BY change_in_temp DESC LIMIT 10;

-- #6
SELECT RANK() OVER (
  ORDER BY tempf
) AS 'coldest_rank', year, state, tempf
FROM state_climate LIMIT 20;

-- #7
SELECT RANK() OVER (
  PARTITION BY state
  ORDER BY tempf DESC
) AS 'warmest_rank', year, state, tempf
FROM state_climate LIMIT 20;

-- #8
SELECT NTILE(4) OVER (
  PARTITION BY state
  ORDER BY tempf
) AS 'quartile', year, state, tempf
FROM state_climate;

-- #9
SELECT NTILE(5) OVER (
  ORDER BY tempf
) AS 'quintile', year, state, tempf
FROM state_climate;
