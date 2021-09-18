
import unittest
from modules.player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player("Carlos", "Rock")

    def test_player_has_name(self):
        self.assertEqual("Carlos", self.player.name)

    def test_player_has_choice(self):
        self.assertEqual("Rock", self.player.choice)