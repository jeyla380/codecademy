<?php

class StringUtilities
{
  public static function secondCase($string)
  {
    $string = strtolower($string);
    if(strlen($string) >= 2)
    {
      $string[1] = strtoupper($string[1]);
    }
    return $string;
  }
}

echo StringUtilities::secondCase("b");
echo "\n";
echo StringUtilities::secondCase("be");
echo "\n";
echo StringUtilities::secondCase("pineapple");
echo "\n";
echo "\n";


class Pajamas
{
  private $owner, $fit, $color;
  function __construct($owner = "Jane", $fit = "S", $color = "pink")
  {
    $this->owner = StringUtilities::secondCase($owner);
    $this->fit = $fit;
    $this->color = $color;
  }
  public function setFit($new_fit)
  {
    $this->fit = $new_fit;
  }
  public function describe()
  {
    return $this->owner . " owns a(n) " . $this->fit . " sized " . $this->color . "-colored pair of pajamas.";
  }
}

$chicken_PJs = new Pajamas("CHICKEN", "M", "lavender");
echo $chicken_PJs->describe();
echo "\n....but they washed their PJs too many times and shrunk....";
$chicken_PJs->setFit("tightly fit M");
echo "\n";
echo $chicken_PJs->describe();
echo "\n";
echo "\n";


class ButtonablePajamas extends Pajamas
{
  private $button_state = "unbuttoned";
  function describe()
  {
    return parent::describe() . " They also have buttons which are currently $this->button_state";
  }
  function toggleButtons()
  {
    if($this->button_state == "unbuttoned")
    {
      $this->button_state = "buttoned";
    }
    else
    {
      $this->button_state = "unbuttoned";
    }
  }
}

$moose_PJs = new ButtonablePajamas("moose");
echo $moose_PJs->toggleButtons();
echo $moose_PJs->describe();
