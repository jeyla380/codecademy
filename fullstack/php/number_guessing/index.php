<?php

$play_count = 0;
$correct_guesses = 0;
$guess_high = 0;
$guess_low = 0;

echo "I'm going to think of numbers between 1 and 10 (inclusive). Do you think you can guess correctly?\n";


function guessNumber()
{
  global $play_count;
  global $correct_guesses;
  global $guess_high;
  global $guess_low;

  $play_count++;

  $rand_num = rand(1, 10);

  echo "\nMake your guess...\n";
  $guess = intval(readline(">> "));
  #intval() converts a string to an int

  echo "Round: $play_count\nMy Number: $rand_num\nYour guess: $guess";
  if ($guess === $rand_num)
  {
    $correct_guesses++;
  }
  elseif($guess > $rand_num)
  {
    $guess_high++;
  }
  else
  {
    $guess_low++;
  }
}

#five rounds of the game
guessNumber();
guessNumber();
guessNumber();
guessNumber();
guessNumber();

#this shows up after completing the game
$percent_correct = ($correct_guesses/$play_count) * 100;
  echo "\nAfter $play_count rounds, you guessed the number correctly $percent_correct% of the time.\n";  

if($guess_high > $guess_low)
  {
    echo "\nWhen you guessed wrong, you tended to guess high\n";
  }
elseif($guess_high < $guess_low)
  {
    echo "\nWhen you guessed wrong, you tended to guess low\n";
  }
