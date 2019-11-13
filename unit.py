import unittest
from card import *
from blackjack import *

class TestCards(unittest.TestCase):
    def setUp(self):
        # self.game = BlackjackGame()
        pass

    def test_card_values_10(self):
        self.assertEqual(Card('♥', '10').value(), 10)
    def test_card_values_J(self):
        self.assertEqual(Card('♥', 'J').value(), 10)
    def test_card_values_A(self):
        self.assertEqual(Card('♥', 'A').value(), 11)
    def test_card_values_2(self):
        self.assertEqual(Card('♥', '2').value(), 2)

    def test_card_constructor_wrong_face_throws_valueException(self):
        with self.assertRaises(ValueError):
            Card('♠', "face")

    def test_card_constructor_wrong_suit_throws_valueException(self):
        with self.assertRaises(ValueError):
            Card('clubs', "A")


if __name__ == '__main__':
    unittest.main()
