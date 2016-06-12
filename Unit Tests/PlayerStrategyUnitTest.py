import unittest
from PlayerStrategy import move
from Card import Card


class PlayerTestCase(unittest.TestCase):

    def test_player_strategy(self):
        self.assertTrue(move([Card(0, 0), Card(1, 4)]) == 'h')  # Ace and 3 = hit
        self.assertTrue(move([Card(0, 4), Card(1, 3)]) == 'h')  # 4 and 3 = hit
        self.assertTrue(move([Card(0, 10), Card(1, 7)]) == 's')  # 10 and 7 = stay
        self.assertTrue(move([Card(0, 1), Card(1, 3)]) == 'h')  # 1 and 3 = hit
        self.assertTrue(move([Card(0, 10), Card(1, 7)]) == 's')  # 10 and 6 = hit
        self.assertTrue(move([Card(0, 1), Card(1, 6)]) == 'h')  # Ace and 6 = hit
        self.assertTrue(move([Card(0, 10), Card(1, 11)]) == 's')  # 10 and Jack = stay
        self.assertTrue(move([Card(0, 11), Card(1, 10)]) == 's')  # Ace and Jack = stay

if __name__ == '__main__':
    unittest.main()