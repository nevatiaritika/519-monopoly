from Adjudicator import Adjudicator
import os, threading, time


state_list = []

class Monopoly(threading.Thread):
    def __init__(self, gameid, bot1, bot2):
        threading.Thread.__init__(self)
        self.gameID = gameid
        self.player1 = bot1
        self.player2 = bot2

    def get_game_id(self):
        return self.gameID

    def run(self):
        game = Adjudicator(self.player1, self.player2)
        state_list = game.play()

        if not os.path.isdir('gamedata'):
            os.mkdir('gamedata')

        with open("gamedata/{}.csv".format(self.gameID), 'w') as f:
            for state in state_list:
                f.write(repr(state))
                f.write("\n")
