from flask import render_template, request
from flask.helpers import url_for
from werkzeug.utils import redirect

from modules.game import Game
from modules.player import Player
from app import app

# @app.route('/player1')
# def player1():
#     return render_template('player1.html', title="Player 1 Details")

# @app.route('/<player2', methods=['POST'])
# def player2():
#     player_name = request.form["name"]
#     player_choice = request.form["choice"]
#     player = Player(player_name, player_choice)
#     return render_template('player2.html', title="Player 2 Details", player1=player)

# @app.route('/play_game')
# def play_game():
#     player_name = request.form["name"]
#     player_choice = request.form["choice"]
#     player2 = Player(player_name, player_choice)
#     game = Game()
#     return render_template('result.html', )

@app.route('/<choice1>/<choice2>')
def play(choice1, choice2):
    player1 = Player('Oscar', choice1)
    player2 = Player('Carlos', choice2)
    game = Game()
    result = game.play(player1, player2)
    return render_template('result.html', title='Result', result=result)

@app.route('/play/<name>/<choice>')
def play_computer(name, choice):
    player = Player(name, choice)
    game = Game()
    return render_template('result.html', title="Result", player=player, game=game)

@app.route('/play')
def enter_details():
    return render_template('player1.html', title ="Player Details")

@app.route('/play', methods=["POST"])
def redirection():
    name = request.form['name']
    choice = request.form['choice']
    player = Player(name,choice)
    game = Game()
    return render_template('result.html', title="Result", game=game, player=player)


