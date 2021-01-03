import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame (unittest.TestCase):

    def setUp(self):
        self.cardgame = CardGame ()
        self.card_1 = Card ('hearts', 1)
        self.card_2 = Card ('diamonds', 9)
        self.card_3 = Card ('hearts', 2)
        self.cards = [self.card_1, self.card_2, self.card_3]


    
    def test_highest_card_returns_higher_value_card (self):
        self.assertEqual (self.card_2, self.cardgame.highest_card(self.card_1, self.card_2))
        self.assertEqual (self.card_2, self.cardgame.highest_card(self.card_3, self.card_2))
        self.assertEqual (self.card_3, self.cardgame.highest_card(self.card_1, self.card_3))


    def test_cards_total (self):
        self.assertEqual ("You have a total of 12", self.cardgame.cards_total(self.cards))