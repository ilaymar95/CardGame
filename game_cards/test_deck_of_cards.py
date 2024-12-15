from unittest import TestCase
from game_cards.deck_of_cards import DeckOfCards

class TestDeckOfCards(TestCase):
    def setUp(self):
        print('This is a setUp')
        self.deck = DeckOfCards()

    def tearDown(self):
        print('This is a tearDown')
        self.deck = None

    def test__init__(self):
        """
        The test verifies that the init is creating a deck of 52 cards
        """
        print('test__init__')
        self.assertTrue(type(self.deck)==DeckOfCards)
        self.assertTrue(len(self.deck.card_deck)==52)

    def test_cards_shuffle(self):
        """
        The test verifies that the cards are shuffled correctly
        """
        print('test_cards_shuffle')
        deck = self.deck.card_deck.copy()
        self.deck.cards_shuffle()
        self.assertNotEqual(deck, self.deck.card_deck)
        self.assertEqual(len(deck),len(self.deck.card_deck))

    def test_cards_shuffle_empty_deck(self):
        print('test_cards_shuffle_empty_deck')
        deck = self.deck
        for i in range(len(deck.card_deck)):
            deck.card_deck.pop()
        with self.assertRaises(ValueError):
            deck.cards_shuffle()



    def test_deal_one(self):
        """
        The test checks that deal_one() method pop the card correctly and that it is not in the deck anymore
        """
        print('test_deal_one')
        card = self.deck.deal_one()
        self.assertNotIn(card, self.deck.card_deck)
        self.assertEqual(len(self.deck.card_deck),51)

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
        print('test_deal_when_empty')
        deck = self.deck
        for i in range(len(deck.card_deck)):
            deck.deal_one()
        self.assertEqual(None,deck.deal_one())