<?php

function generateStory($singular_noun, $verb, $color, $distance_unit)
{
  $story = "The ${singular_noun}s are lovely, $color, and deep.\nBut I have promises to keep, \nAnd $distance_unit to go before I $verb, \nAnd $distance_unit to go before I $verb.\n\n";
  return $story;
}

echo generateStory("dog", "eat", "purple", "kilometers");
echo generateStory("book", "read", "red", "yards");
echo generateStory("pizza", "sleep", "orange", "feet");

#----------------------------------------------------------------#
#Alternate without function

$story = "The woods are lovely, dark, and deep.\nBut I have promises to keep, \nAnd miles to go before I sleep, \nAnd miles to go before I sleep.\n\n";

$var_list = array("wood", "sleep", "dark", "miles");
$first_list = array("dog", "eat", "purple", "kilometers");
$second_list = array("book", "read", "red", "yards");
$third_list = array("pizza", "sleep", "orange", "feet");

$phrase_one = str_replace($var_list, $first_list, $story);
$phrase_two = str_replace($var_list, $second_list, $story);
$phrase_three = str_replace($var_list, $third_list, $story);

echo $phrase_one;
echo $phrase_two;
echo $phrase_three;
