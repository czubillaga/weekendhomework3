class Game():

    def __init__(self):
        self.winner = None

    def play(self, player_1, player_2):
        if player_1.choice == player_2.choice:
            return self.winner
        elif player_1 > player_2:
            return player_1.name + " wins"
        else: 
            return player_2.name + "wins"