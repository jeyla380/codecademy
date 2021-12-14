<?php
  
$annualExpenses = [
    "vacations" => 1000,
    "carRepairs" => 1000,    
];

$monthlyExpenses = [
    "rent" => 1500,
    "utilities" => 200,
    "healthInsurance" => 200
];

$grossSalary = 48150;
$socialSecurity = $grossSalary * .062;

$incomeSegments = [[9700, .88], [29775, .78], [8675, .76]];

// Write your code below:

#TAXES
$netIncome = ($incomeSegments[0][0] * $incomeSegments[0][1]) + ($incomeSegments[1][0] * $incomeSegments[1][1]) + ($incomeSegments[2][0] * $incomeSegments[2][1]);
echo "Net Income: \$$netIncome\n";

$annualIncome = abs($netIncome - $socialSecurity);
echo "Annual Income: \$$annualIncome\n";
echo "\n";


#ANNUAL EXPENSES
$newAnnualIncome = abs($annualIncome - ($annualExpenses['vacations'] + $annualExpenses['carRepairs']));
echo "New Annual Income (after Annual Expenses): \$$newAnnualIncome\n";
echo "\n";


#MONTHLY EXPENSES
$monthlyIncome = $newAnnualIncome / 12;
echo "Monthly Income: \$$monthlyIncome\n";

$newMonthlyIncome = abs($monthlyIncome - ($monthlyExpenses['rent'] + $monthlyExpenses['utilities'] + $monthlyExpenses['healthInsurance']));
echo "New Monthly Income (after Monthly Expenses): \$$newMonthlyIncome\n";
echo "\n";


#WEEKLY EXPENSES
$weeklyIncome = $newMonthlyIncome / 4.33;
echo "Weekly Income: \$$weeklyIncome\n";

$weeklyExpenses = ["gas" => 25, "food" => 90, "entertainment" => 47];
$totalWeeklyExpenses = $weeklyExpenses['gas'] + $weeklyExpenses['food'] + $weeklyExpenses['entertainment'];

$newWeeklyIncome = abs($weeklyIncome - $totalWeeklyExpenses);
echo "Weekly Income (after Weekly Expenses): \$$newWeeklyIncome\n";
echo "\n";


#SAVINGS
$savings = $newWeeklyIncome * 52;
echo "Remaining Income for Savings: \$$savings\n";
