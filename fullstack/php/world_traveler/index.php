<?php
  
$riel = 2103942;
$kyat = 19092;
$krones = 109;
$lek = 9094;

echo "$riel riel";
echo "\n${kyat} kyat";
echo "\n${krones} krones";
echo "\n${lek} lek";

$riel_to_usd = 0.00026;
$kyat_to_usd = 0.00066;
$krones_to_usd = 0.11;
$lek_to_usd = 0.0090;

echo "\n";
echo "\nThe exchange rate for riel to usd is $riel_to_usd";
echo "\nThe exchange rate for kyat to usd is $kyat_to_usd";
echo "\nThe exchange rate for krones to usd is $krones_to_usd";
echo "\nThe exchange rate for lek to usd is $lek_to_usd";

$usd_from_riel = $riel * $riel_to_usd;
$usd_from_kyat = $kyat * $kyat_to_usd;
$usd_from_krones = $krones * $krones_to_usd;
$usd_from_lek = $lek * $lek_to_usd;

$usd_from_riel = number_format($usd_from_riel, 2);
$usd_from_kyat = number_format($usd_from_kyat, 2);
$usd_from_krones = number_format($usd_from_krones, 2);
$usd_from_lek = number_format($usd_from_lek, 2);

echo "\n";
echo "\nYour $riel riel was exchanged for $usd_from_riel usd";
echo "\nYour $kyat kyat was exchanged for $usd_from_kyat usd";
echo "\nYour $krones krones was exchanged for $usd_from_krones usd";
echo "\nYour $lek lek was exchanged for $usd_from_lek usd";

$new_usd_from_riel = $usd_from_riel - 1;
$new_usd_from_kyat = $usd_from_kyat - 1;
$new_usd_from_krones = $usd_from_krones - 1;
$new_usd_from_lek = $usd_from_lek - 1;

$final_amount = $new_usd_from_riel + $new_usd_from_kyat + $new_usd_from_krones + $new_usd_from_lek;
echo "\n";
echo "\nThe final amount is $final_amount usd";
