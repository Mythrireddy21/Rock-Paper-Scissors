document.addEventListener('DOMContentLoaded', () => {
  const nameForm = document.getElementById('name-form');
  const nameSection = document.getElementById('name-section');
  const gameSection = document.getElementById('game-section');
  const leaderboardSection = document.getElementById('leaderboard-section');
  const usernameDisplay = document.getElementById('username');

  // Handle name form submit
  nameForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const username = document.getElementById('player-name').value.trim();
    if (username) {
      // Set username display
      usernameDisplay.textContent = username;

      // Hide name input, show game and leaderboard
      nameSection.style.display = 'none';
      gameSection.style.display = 'block';
      leaderboardSection.style.display = 'block';

      // Send POST request to server to set session username and init scores
      fetch('/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: `username=${encodeURIComponent(username)}`
      });
    }
  });
});

// Your existing play function (updated to handle errors)
function play(userChoice) {
  fetch('/play', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ userChoice: userChoice })
  })
  .then(res => res.json())
  .then(data => {
    document.getElementById('user-choice').textContent = data.userChoice;
    document.getElementById('computer-choice').textContent = data.computerChoice;
    document.getElementById('result').textContent = data.result;
    document.getElementById('user-score').textContent = data.userScore;
    document.getElementById('computer-score').textContent = data.computerScore;
    document.getElementById('username').textContent = data.username;

    let leaderboardHTML = '';
    data.leaderboard.forEach(user => {
      leaderboardHTML += `<li><strong>${user[0]}</strong>: ${user[1]}</li>`;
    });
    document.getElementById('leaderboard-list').innerHTML = leaderboardHTML;
  })
  .catch(error => {
    console.error('Error:', error);
  });
}
