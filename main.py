# create me a tic tac toe web based game for one person against computer on a 5*5 matrix in Python

from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)
game_state = [['' for _ in range(5)] for _ in range(5)]

@app.route('/')
def home():
    return render_template('index.html', game_state=game_state)

@app.route('/move', methods=['POST'])
def player_move():
    data = request.get_json()
    x, y = data['x'], data['y']
    game_state[x][y] = 'X'  # Player's move
    computer_move()
    return redirect(url_for('home'))

def computer_move():
    while True:
        x, y = random.randint(0, 4), random.randint(0, 4)
        if game_state[x][y] == '':
            game_state[x][y] = 'O'  # Computer's move
            break

if __name__ == '__main__':
    app.run(debug=True)