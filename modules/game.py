import random
from modules.player import *
import random

def computer_choice():

    choice_list = ['narf','rock', 'paper', 'scissors']
    return choice_list[random.randrange(1,4)]

class Game():

    def __init__(self):
        self.winner = None

    def play(self, player_1 = Player('Computer', computer_choice()), player_2 = Player('Computer', computer_choice())):
        if player_1.choice == player_2.choice:
            return "Tie"
        elif player_1 > player_2:
            return player_1.name + " wins by playing " + player_1.choice + " against " + player_2.choice
        else: 
            return player_2.name + " wins by playing " + player_2.choice + " against " + player_1.choice



