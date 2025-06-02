# Rock Paper Scissors Game

A simple Rock Paper Scissors game built with Flask, featuring user login, real-time gameplay, a leaderboard, and achievements.


## Features

- User login with name entry
- Play Rock, Paper, Scissors against the computer
- Real-time score tracking (user and computer)
- Win streak tracking and total games played
- Achievements system (5 wins in a row, first win, perfect game, etc.)
- Persistent leaderboard saved to CSV file showing top 5 players
- Responsive and interactive UI (frontend with HTML, CSS, and JavaScript)
- Flask backend serving REST API and templates


## File Structure

```
Rock-Paper-Scissors/
│
├── app.py                 # Flask backend application
├── leaderboard.csv        # CSV file storing leaderboard data (created automatically)
├── requirements.txt       # Python dependencies
├── templates/
│   ├── index.html         # Login page template
│   ├── game.html          # Main game page template
├── static/
│   ├── style.css          # CSS styles
│   └── script.js          # JavaScript logic for gameplay and UI
└── README.md              # This file
```


## Installation

1. **Clone the repository**

```bash
git clone https://github.com/Mythrireddy21/Rock-Paper-Scissors.git
cd Rock-Paper-Scissors
````

2. **Create a Python virtual environment (optional but recommended)**

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the Flask app**

```bash
python app.py
```

5. **Open your browser**

Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) to start playing!

---

## How to Play

1. Enter your username on the landing page.
2. Click "Start Game" to enter the game page.
3. Select Rock, Paper, or Scissors by clicking buttons.
4. View results, scores, and achievements live.
5. Your highest score is saved to the leaderboard.


## Achievements

* 🏅 **5 Wins in a Row!**
* 🎖️ **10 Total Games Played!**
* 🥇 **First Win!**
* 🌟 **Perfect Game (No Losses in 5 games)!**


## Dependencies

* Python 3.x
* Flask

Install dependencies with:

```bash
pip install Flask
```

## Customization

* Change the secret key in `app.py` for session security.
* Modify `leaderboard.csv` location or handling in `app.py`.
* Enhance frontend UI by editing files in `templates/` and `static/`.


## License

This project is licensed under the MIT License.

## Acknowledgements

* Inspired by classic Rock Paper Scissors game logic.
* Built with Flask for backend simplicity and quick prototyping.



**Enjoy playing Rock Paper Scissors!** ✊ 🖐 ✌

