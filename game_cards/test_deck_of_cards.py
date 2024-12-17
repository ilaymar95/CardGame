from unittest import TestCase
from game_cards.deck_of_cards import DeckOfCards
from game_cards.card import Card

class TestDeckOfCards(TestCase):
    def setUp(self):
        print('This is a setUp')
        self.deck = DeckOfCards()

    def tearDown(self):
        print('This is a tearDown')
        self.deck = None
    # add another init test to check every card is unique
    def test__init__len(self):
        """
        The test verifies that the init is creating a deck of 52 cards
        """
        self.assertTrue(len(self.deck.card_deck)==52)

    def test__init_unique_cards(self):
        """
        Tests that every card in the deck is unique
        """
        for i in range(len(self.deck.card_deck)-1):
            for j in range(i+1,len(self.deck.card_deck)):
                self.assertNotEqual(self.deck.card_deck[i], self.deck.card_deck[j])

    def test_cards_shuffle(self):
        """
        The test verifies that the cards are shuffled correctly
        """
        deck = self.deck.card_deck.copy()
        self.deck.cards_shuffle()
        self.assertNotEqual(deck, self.deck.card_deck)
        self.assertEqual(len(deck),len(self.deck.card_deck))

    def test_deal_one(self):
        """
        The test checks that deal_one() method pop the card correctly and that it is not in the deck anymore
        """
        card = self.deck.deal_one()
        self.assertEqual(len(self.deck.card_deck),51)
        self.assertTrue(type(card) == Card)

    def test_deal_all_cards(self):
        """
        Tests that the function deals all the cards correctly
        """
        print('test_deal_all_cards')
        deck = self.deck
        for i in range(len(deck.card_deck)):
            deck.deal_one()
        self.assertEqual(len(deck.card_deck),0)

    def test_deal_when_empty(self):
        """
        Tests when the card deck is empty, the function will return None
        """
        deck = self.deck
        for i in range(len(deck.card_deck)):
            deck.deal_one()
        self.assertEqual(None,deck.deal_one())