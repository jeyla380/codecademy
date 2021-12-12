<?php
$initial = '555';

#octdec() converts to a base 8 system & an int/float
$a = octdec($initial);
echo $a;

#deg2rad() converts degrees to radians
$b = deg2rad($a);
echo $b;

#cos() finds the cosine of the float given
$c = cos($b);
echo $c;

#rounds $c to 3 decimal places
$d = round($c, 3);
echo $d;

#log() returns log-based 0, but it's not necessary to put the 0
$e = log($d);
echo $e;

$f = abs($e);
echo $f;

#acos() uses the arc cosine
$g = acos($f);
echo $g;

#rad2deg() converts the radians to degrees
$h = rad2deg($g);
echo $h;

#floor() will always round down
$i = floor($h);
echo $i;

$j = $i - 47;
echo $j;
