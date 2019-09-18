import unittest
from blackjack import BlackjackGame

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.game = BlackjackGame()

    def test_card_values(self):
        self.assertEqual(BlackjackGame.get_card_value('10♥'), 10)


if __name__ == '__main__':
    unittest.main()
