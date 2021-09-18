import unittest

from modules.player import Player
from modules.game import Game

class TestGame(unittest.TestCase):

    def setUp(self): 
        self.player_1 = Player("Carlos", "Rock")
        self.player_2 = Player("Ali", "Scissors")
        self.player_3 = Player("Oscar", "Rock")
        self.player_4 = Player("Miguel", "Paper")
        self.game = Game()

    def test_game_returns_none(self):
        self.assertEqual(None, self.game.play(self.player_1, self.player_3))

    def test_game_returns_winner(self):
        self.assertEqual("Carlos wins", self.game.play(self.player_1, self.player_2))
        self.assertEqual("Miguel wins", self.game.play(self.player_4, self.player_1))
        self.assertEqual("Ali wins", self.game.play(self.player_2, self.player_4))