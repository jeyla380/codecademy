<?php
  
function cookSoup(){
	// Write your code here:
  global $location, $has_mushrooms, $has_soup;
  
  if($location !== "kitchen")
  {
    if (!$has_mushrooms)
    {
      echo "You can't cook like this! You need something to cook AND be in the kitchen.\n";
    }
    else
    {
      echo "Even though you have mushrooms, you need somewhere to cook this...maybe the kitchen?\n";
    }
  }
  elseif($location === "kitchen")
  {
    if($has_mushrooms)
    {
      echo "You made some mushroom soup. Mushroom is the queen of all soups!\n";
      $has_mushrooms = false;
      $has_soup = true;
    }
    else
    {
      echo "You need something to cook!\n";
    }
  }
  
  
  
  
}
