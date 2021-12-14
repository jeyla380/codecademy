<html>
<body>
<!--Your code goes here-->
<h3>Addition</h3>
<form method="get" action="addition.php">
  First Number: <input type="text" name="first_num_add"> <br>
  Second Number: <input type="text" name="second_num_add"> <br>
  <button type="submit">Add!</button> <br>
  #<?php print_r($_GET)?>
</form>
<hr>

<h3>Division</h3>
<form method="get" action="division.php">
  First Number: <input type="text" name="first_num_div"> <br>
  Second Number: <input type="text" name="second_num_div"> <br>
  <button type="submit">Divide!</button> <br>
  #<?php print_r($_GET)?>
</form>
<hr>

<h3>Pythagorean Theorem</h3>
<form method="get" action="pythagorean_theorem.php">
  First Number: <input type="text" name="first_num_pt"> <br>
  Second Number: <input type="text" name="second_num_pt"> <br>
  <button type="submit">Calculate!</button> <br>
  #<?php print_r($_GET)?>
</form>

<a href="index.php">Reset</a>
</body>
</html>
