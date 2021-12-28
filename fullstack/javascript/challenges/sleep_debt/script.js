function getSleepHours(day)
{
  day = day.toLowerCase();
  switch(day)
  {
    case "monday":
      return 8;
      break;
    case 'tuesday':
      return 7;
      break;
    case 'wednesday':
      return 8;
      break;
    case 'thursday':
      return 6;
      break;
    case 'friday':
      return 7.5;
      break;
    case 'saturday':
      return 10;
      break;
    case 'sunday':
      return 9.5;
      break;
  }
}

//console.log(getSleepHours("Monday"));
//console.log(getSleepHours("Friday"));

function getActualSleepHours()
{
  totalSleepHours = getSleepHours('monday') + getSleepHours('tuesday') + getSleepHours('wednesday') + getSleepHours('thursday') + getSleepHours('friday') + getSleepHours('saturday') + getSleepHours('sunday');
  return totalSleepHours;
}
//console.log(getActualSleepHours());

function getIdealSleepHours()
{
  idealHours = 8;
  return idealHours * 7;
}
//console.log(getIdealSleepHours());

function calculateSleepDebt()
{
  actualSleepHours = getActualSleepHours(); //53.5 hrs
  idealSleepHours = getIdealSleepHours(); //56 hrs

  if(actualSleepHours == idealSleepHours)
  {
    console.log("You got the perfect amount of sleep:)");
  }
  else if(actualSleepHours < idealSleepHours)
  {
    console.log("You really need to get some rest. You need " + (idealSleepHours - actualSleepHours) + " more hours to get the perfect amount of sleep.");
  }
  else
  {
    console.log("You got more sleep than you needed, " + (actualSleepHours - idealSleepHours) + " hour(s) extra to be precise! But that's alright! Sleep is always good:)");
  }
}

calculateSleepDebt();
