let humanScore = 0;
let computerScore = 0;
let currentRoundNumber = 1;

//This is code I created

// Write your code below:
function generateTarget()
{
	return Math.floor(Math.random() * 10);
}


function compareGuesses(userGuess, computerGuess, targetNum)
{
	if(targetNum == userGuess)
	{
		//user wins
		return true;
	}
	else if(targetNum == computerGuess)
	{
		//computer wins
		return false;
	}
	
	if(userGuess == computerGuess)
	{
		//user wins if computer and user guess the same number
		return true;
	}
	
	closeToTargetUser = Math.abs(userGuess - targetNum);
	closeToTargetComp = Math.abs(computerGuess - targetNum);
	if(closeToTargetUser < closeToTargetComp)
	{
		//user wins since closeToTargetUser has the smaller number
		return true;
	}
	else
	{
		//computer wins since closeToTargetComp has the smaller number
		return false;
	}
}


function updateScore(string)
{
	if(string == "human")
	{
		humanScore++;
	}
	else if(string == "computer")
	{
		computerScore++;
	}
}


function advanceRound()
{
	currentRoundNumber++;
}
