import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card1 = Card("spade", 1)
        self.card2 = Card("heart", 5)
        self.card3 = Card("club", 8)

        self.card_game = CardGame()
        self.card_game.cards = [self.card1,self.card2,self.card3]

    def test_check_for_ace(self):
        result = self.card_game.check_for_ace(self.card1)
        result2 = self.card_game.check_for_ace(self.card2)
        self.assertEqual(True, result)
        self.assertEqual(False, result2)

    def test_highest_card(self):
        result = self.card_game.highest_card(self.card1, self.card2)
        self.assertEqual(self.card2, result)

    def test_cards_total(self):
        result = self.card_game.cards_total(self.card_game.cards)
        self.assertEqual("You have a total of 14", result)