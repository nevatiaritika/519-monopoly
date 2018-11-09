from flask import Flask, request, render_template
app = Flask(__name__)
import datetime
from mnply import Monopoly
import os
import _thread

def run_adjudicator(gameID, bot1, bot2):
    game_thread = Monopoly(gameID, bot1, bot2)
    game_thread.start()
    return game_thread

@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/startgame", methods=["POST", "GET"])
def start_game():
    if request.method == "POST":
        return_file = str(datetime.datetime.now().timestamp())
        try:
            f = request.files['bot1'], request.files['bot2']
            bot1 = pickle_load(f[0])
            bot2 = pickle_load(f[1])
        except KeyError:
            bot1, bot2 = [None] * 2
        run_adjudicator(return_file, bot1, bot2)
        return return_file
    elif request.method == "GET":
        # return the template for uploading the file
        return render_template('startgame.html')


@app.route("/gamedata/<filename>", methods=["GET"])
def return_game_data(filename):
    if os.path.isdir("gamedata"):
        if os.path.exists("gamedata/{}.csv".format(filename)):
            f = open('gamedata/{}.csv'.format(filename))
            game_data = f.readlines()
            f.close()
            return repr(game_data)
    return "No game data with filename {}.csv found".format(filename)
