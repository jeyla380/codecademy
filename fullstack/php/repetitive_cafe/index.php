<?php
  $drinks = ["Milk Tea" => 2.50, "Taro Latte" => 4.00, "Matcha Green Tea" => 1.25, "Italian Soda" => 2.75, "Milkis" => 1.50, "Yakult" => 1.00];
  $snacks = ["Croissant", "Fruit Tarte", "Mille-Feuille", "Mini Cheesecake", "Nata Bread", "Portuguese Custard Tart"];
?>

<h1>Welcome to the Repetitive Cafe</h1>

<h3>Drinks!</h3>
<ul>
  <?php
    foreach($drinks as $d => $price):
  ?>
  <li><?="$d: \$$price"?></li>
  <?php endforeach; ?>
</ul>
<h3>Pastries! ($2 each)</h3>
<ul>
  <?php
    for($i = 0; $i < count($snacks); $i++):
  ?>
  <li><?="$snacks[$i]" ?></li>
  <?php
    endfor;
  ?>
</ul>
