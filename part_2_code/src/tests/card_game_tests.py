import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.cardgame = CardGame()
        self.card1 = Card("Spades", 9)
        self.card2 = Card("Diamonds", 10)
        self.card3 = Card("Hearts", 7)
        self.cards = [self.card_1, self.card_2]

    def test_check_for_ace_true (self):
        self.assertEqual (True, self.cardgame.check_for_ace(self.card_1))


    def test_check_for_ace_false (self):
        self.assertEqual (False, self.cardgame.check_for_ace(self.card_2))

    
    def test_highest_card_returns_higher_value_card (self):
        self.assertEqual (self.card_2, self.cardgame.highest_card(self.card_1, self.card_2))
        self.assertEqual (self.card_3, self.cardgame.highest_card(self.card_3, self.card_2))
        self.assertEqual (self.card_3, self.cardgame.highest_card(self.card_1, self.card_3))


    def test_cards_total (self):
        self.assertEqual ("You have a total of 26", self.cardgame.cards_total(self.cards))