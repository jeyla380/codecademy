<?php
  // Change player location
function changeLocation(){	
  // Write your code here:
  global $location;
  
  echo "Where do you want to go?\n";
  $go_to_location = readline(">> ");
  $go_to_location = strtolower($go_to_location);

  if($location === "kitchen")
  {
    if ($go_to_location === "bathroom")
    {
      echo "You go to: bathroom.\n";
      $location = $go_to_location;
    }
    elseif($go_to_location === "woods")
    {
      echo "You follow the winding path, shivering as you make your way deep into the Terror Woods.\n";
      $location = $go_to_location;
    }
  }
  elseif($location === "bathroom")
  {
    if($go_to_location === "kitchen")
    {
      echo "You go to: kitchen.\n";
      $location = $go_to_location;
    }
    else
    {
      echo "You can't go directly to $go_to_location. Try going somewhere else first.\n";
    }
  }
  elseif($location === "woods")
  {
    if($go_to_location === "kitchen")
    {
      echo "You go to: kitchen.\n";
      $location = $go_to_location;
    }
    else
    {
      echo "You can't go directly to $go_to_location. Try going somewhere else first.\n";
    }
  }
  else
  {
    echo "That doesn't make sense. Are you confused? Try 'look around'.\n";
  }
  
}
