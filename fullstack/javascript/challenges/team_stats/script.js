var team = {
  _players: [
    {firstName: 'Radhika', lastName: 'Acosta', age: 9}, 
    {firstName: 'Darcy', lastName: 'Welsh', age: 10}, 
    {firstName: 'Kiara', lastName: 'Vu', age: 9}],
  _games: [
    {opponent: 'Kings', teamPoints: 32, opponentPoints: 29},
    {opponent: 'Badgers', teamPoints: 27, opponentPoints: 34},
    {opponent: 'Chords', teamPoints: 15, opponentPoints: 15}],
  get games() {
    return this._games;
  },
  get players() {
    return this._players;
  },

  //method
  addPlayer(firstName, lastName, age)
  {
    var player = {
      firstName: firstName,
      lastName: lastName,
      age: age
    };
    this._players.push(player);
  },

  //method
  addGame(oppName, teamPoints, oppPoints)
  {
    var game = {
      opponent: oppName,
      teamPoints: teamPoints,
      opponentPoints: oppPoints
    };
    this._games.push(game);
  }
};

team.addPlayer('Steph', 'Curry', 28);
team.addPlayer('Lisa', 'Leslie', 44);
team.addPlayer('Bugs', 'Bunny', 76);
console.log(team.players);

team.addGame('Titans', 100, 98);
console.log(team.games);
