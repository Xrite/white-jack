import unittest
from blackjack import *

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.game = BlackjackGame()

    def test_card_values(self):
        self.assertEqual(get_card_value('10♥'), 10)
        self.assertEqual(get_card_value('J♥'), 10)
        self.assertEqual(get_card_value('A♥'), 11)
        self.assertEqual(get_card_value('2♥'), 2)


if __name__ == '__main__':
    unittest.main()
