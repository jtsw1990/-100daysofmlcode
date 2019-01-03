var options = ['rock', 'paper', 'scissors'];
var play = function(userChoice) {
  if (userChoice === 'rock') {
    var computerChoice = options[Math.floor(Math.random() * options.length)];
    document.getElementById('playerChoice').innerHTML = 'Player chose Rock';
    if (computerChoice === 'rock') {
      document.getElementById('computerChoice').innerHTML = 'Comp chose Rock';
      document.getElementById('results').innerHTML = 'Draw';
    } else if (computerChoice === 'paper') {
      document.getElementById('computerChoice').innerHTML = 'Comp chose Paper';
      document.getElementById('results').innerHTML = 'Lose';
    } else if (computerChoice === 'scissors') {
      document.getElementById('computerChoice').innerHTML = 'Comp chose Scissors';
      document.getElementById('results').innerHTML = 'Win';
    }
  } else if (userChoice === 'paper') {
    var computerChoice = options[Math.floor(Math.random() * options.length)];
    document.getElementById('playerChoice').innerHTML = 'Player chose paper';
    if (computerChoice === 'paper') {
      document.getElementById('computerChoice').innerHTML = 'Comp chose Paper';
      document.getElementById('results').innerHTML = 'Draw';
    } else if (computerChoice === 'rock') {
      document.getElementById('computerChoice').innerHTML = 'Comp chose Rock';
      document.getElementById('results').innerHTML = 'Win';
    } else if (computerChoice === 'scissors') {
      document.getElementById('computerChoice').innerHTML = 'Comp chose Scissors';
      document.getElementById('results').innerHTML = 'Lose';
    }
  } else if (userChoice === 'scissors') {
    var computerChoice = options[Math.floor(Math.random() * options.length)];
    document.getElementById('playerChoice').innerHTML = 'Player chose scissors';
    if (computerChoice === 'paper') {
      document.getElementById('computerChoice').innerHTML = 'Comp chose Paper';
      document.getElementById('results').innerHTML = 'Win';
    } else if (computerChoice === 'rock') {
      document.getElementById('computerChoice').innerHTML = 'Comp chose Rock';
      document.getElementById('results').innerHTML = 'Lose';
    } else if (computerChoice === 'scissors') {
      document.getElementById('computerChoice').innerHTML = 'Comp chose Scissors';
      document.getElementById('results').innerHTML = 'Draw';
    }
  }
}
