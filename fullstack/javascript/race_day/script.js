let raceNumber = Math.floor(Math.random() * 1000); //0 to 999

var earlyReg = true
var runnerAge = 17

if(earlyReg && runnerAge > 18)
{
  raceNumber += 1000
}

if(runnerAge > 18 && earlyReg)
{
  console.log(`${raceNumber} will race adults at 9:30am`)
}
else if(runnerAge > 18 && !earlyReg)
{
  console.log(`${raceNumber} will race adults at 11:00am`)
}
else if(runnerAge == 18)
{
  console.log(`${raceNumber} please see the registration desk`)
}
else
{
  console.log(`${raceNumber} will race youth at 12:30, regardless of registration`)
}
