//function getUserChoice(userInput)
const getUserChoice = userInput =>
{
  userInput = userInput.toLowerCase();

  if(userInput == "rock")
  {
    return userInput;
  }
  else if(userInput == "paper")
  {
    return userInput;
  }
  else if(userInput == "scissors")
  {
    return userInput;
  }
  else if(userInput == "bomb")
  {
    return userInput;
  }
  else
  {
    console.log("Error! You can only use 'rock', 'paper', or 'scissors' to play.");
  }
}

//console.log(getUserChoice('paper'));
//console.log(getUserChoice('not paper'));

function getComputerChoice()
{
  //.floor will make it round down to 2
  random_number = Math.floor(Math.random() * 3);
  switch(random_number)
  {
    case 0:
      return 'rock';
      break;
    case 1:
      return 'paper';
      break;
    case 2:
      return 'scissors';
      break;
    default:
      return 'Error!';
  }
}

//console.log(getComputerChoice());
//console.log(getComputerChoice());
//console.log(getComputerChoice());

function determineWinner(userChoice, computerChoice)
{
  if(userChoice == computerChoice)
  {
    return "It's a tie!";
  }
  if(userChoice == "rock")
  {
    if(computerChoice == "paper")
    {
      return "Computer won, you lost:(";
    }
    else if(computerChoice == "scissors")
    {
      return "You won!!!";
    }
  }
  else if(userChoice == "paper")
  {
    if(computerChoice == "scissors")
    {
      return "Computer won, you lost:(";
    }
    else if(computerChoice == "rock")
    {
      return "You won!!!";
    }
  }
  else if(userChoice == "scissors")
  {
    if(computerChoice == "rock")
    {
      return "Computer won, you lost:(";
    }
    else if(computerChoice == "paper")
    {
      return "You won!!!";
    }
  }
  //secret easter egg
  else if(userChoice == "bomb")
  {
    return "You won!!!";
  }
}

//console.log(determineWinner("rock", "rock"));
//console.log(determineWinner("paper", "rock"));
//console.log(determineWinner("scissors", "rock"));
//console.log(determineWinner("scissors", "paper"));

function playGame()
{
  userChoice = getUserChoice('bomb');
  computerChoice = getComputerChoice();
  console.log("Your move: " + userChoice);
  console.log("Computer move: " + computerChoice);
  console.log(determineWinner(userChoice, computerChoice));
}

playGame();
