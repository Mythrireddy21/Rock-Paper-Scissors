from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import random, csv, os

app = Flask(__name__)
app.secret_key = 'your_secret_key'
choices = ['rock', 'paper', 'scissors']
leaderboard_file = 'leaderboard.csv'

def update_leaderboard(username, score):
    records = []
    if os.path.exists(leaderboard_file):
        with open(leaderboard_file, 'r', newline='') as file:
            reader = csv.reader(file)
            records = [row for row in reader if len(row) >= 2 and row[1].isdigit()]

    updated = False
    for record in records:
        if record[0] == username:
            if int(record[1]) < score:
                record[1] = str(score)
            updated = True
            break

    if not updated:
        records.append([username, str(score)])

    records.sort(key=lambda x: int(x[1]), reverse=True)

    with open(leaderboard_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(records)

def read_leaderboard():
    if not os.path.exists(leaderboard_file):
        return []
    with open(leaderboard_file, 'r', newline='') as file:
        reader = csv.reader(file)
        valid_rows = [row for row in reader if len(row) >= 2 and row[1].isdigit()]
        return sorted(valid_rows, key=lambda x: int(x[1]), reverse=True)[:5]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username'].strip()
        if username:
            session['username'] = username
            session['user_score'] = 0
            session['computer_score'] = 0
            session['win_streak'] = 0
            session['total_games'] = 0
            session['first_win'] = False
            return redirect(url_for('game'))
    return render_template('index.html', leaderboard=read_leaderboard())

@app.route('/game')
def game():
    if 'username' not in session:
        return redirect(url_for('index'))
    return render_template('game.html', leaderboard=read_leaderboard())

@app.route('/play', methods=['POST'])
def play():
    data = request.get_json(force=True)
    user_choice = data.get('userChoice')
    if user_choice not in choices:
        user_choice = random.choice(choices)

    computer_choice = random.choice(choices)
    user_score = session.get('user_score', 0)
    computer_score = session.get('computer_score', 0)
    win_streak = session.get('win_streak', 0)
    total_games = session.get('total_games', 0)
    username = session.get('username')
    first_win = session.get('first_win', False)

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        result = "You win!"
        user_score += 1
        win_streak += 1
        if not first_win:
            first_win = True
    else:
        result = "Computer wins!"
        computer_score += 1
        win_streak = 0

    total_games += 1

    session.update({
        'user_score': user_score,
        'computer_score': computer_score,
        'win_streak': win_streak,
        'total_games': total_games,
        'first_win': first_win
    })

    update_leaderboard(username, user_score)

    achievements = []
    if win_streak >= 5:
        achievements.append("🏅 5 Wins in a Row!")
    if total_games >= 10:
        achievements.append("🎖️ 10 Total Games Played!")
    if first_win and user_score == 1:
        achievements.append("🥇 First Win!")
    if total_games >= 5 and computer_score == 0:
        achievements.append("🌟 Perfect Game (No Losses)!")

    return jsonify({
        'userChoice': user_choice,
        'computerChoice': computer_choice,
        'result': result,
        'userScore': user_score,
        'computerScore': computer_score,
        'username': username,
        'leaderboard': read_leaderboard(),
        'achievements': achievements
    })

if __name__ == '__main__':
    app.run(debug=True)
