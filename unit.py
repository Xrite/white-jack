import unittest
from Card import *

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.game = BlackjackGame()

    def test_card_values(self):
        self.assertEqual(Card('♥', '10').get_card_value(), 10)
        self.assertEqual(Card('♥', 'J').get_card_value(), 10)
        self.assertEqual(Card('♥', 'A').get_card_value(), 11)
        self.assertEqual(Card('♥', '2').get_card_value(), 2)


if __name__ == '__main__':
    unittest.main()
