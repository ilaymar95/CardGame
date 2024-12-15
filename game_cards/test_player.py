from unittest import TestCase
from game_cards.player import Player
from game_cards.deck_of_cards import DeckOfCards
from game_cards.card import Card
from unittest import mock
from unittest.mock import patch


class TestPlayer(TestCase):
    def setUp(self):
        print('This is setUp')
        self.deck = DeckOfCards()
        self.player = Player('ilay',26)

    def tearDown(self):
        print('This is tearDown')
        self.player = None

    def test_init_valid(self):
        """
        Creates a valid Player object
        """
        print('This is test_init_valid')
        self.assertTrue(type(self.player) == Player)
        self.assertEqual(self.player.name, 'ilay')

    def test_init_invalid_name_type(self):
        """
        Tests that the function raises TypeError when given invalid player name type
        """
        print('test_init_invalid_name_type')
        with self.assertRaises(TypeError):
            player = Player(['ilay'],25)

    def test_invalid_name_empty(self):
        """
        Tests that the function raises ValueError when given empty player name
        """
        print('test_invalid_name_empty')
        with self.assertRaises(ValueError):
            player = Player('',26)

    def test_valid_name_length_1(self):
        """
        Tests that the function makes a player with name length of 1 which is valid for the game
        """
        print('test_valid_name_length_1')
        player = Player('i',26)
        self.assertTrue(type(player)==Player)
        self.assertEqual(player.name, 'i')

    def test_valid_cards_to_deal_0(self):
        """
        Tests the player init that cards_to_deal is set to 26
        """
        print('test_valid_cards_to_deal_0')
        player = Player('ilay',0)
        self.assertTrue(player.cards_to_deal==26)

    def test_valid_cards_to_deal_10_26(self):
        """
        Tests the player init that cards_to_deal is set to 26 or 10 (edge values)
        """
        print('test_valid_cards_to_deal_10')
        player = Player('ilay', 10)
        player2 = Player('david',26)
        self.assertTrue(player.cards_to_deal==10)
        self.assertTrue(player2.cards_to_deal==26)

    def test_valid_cards_to_deal_26_27(self):
        print('test_valid_cards_to_deal_26_27')
        player = Player('ilay', 26)
        player2 = Player('david',27)
        self.assertTrue(player.cards_to_deal==26)
        self.assertTrue(player2.cards_to_deal == player.cards_to_deal)

    def test_invalid_cards_to_deal_type(self):
        """
        Tests that the function raises TypeError when given invalid cards_to_deal type
        """
        print('test_invalid_cards_to_deal_type')
        with self.assertRaises(TypeError):
            player = Player('ilay','26')


    def test_set_hand_valid(self):
        """
        Tests that set_hand function sets the player's hand correctly
        """
        print('test_set_hand_valid')
        self.player.set_hand(self.deck)
        self.assertTrue(len(self.player.cards_deck) == self.player.cards_to_deal)
        self.assertTrue(len(self.player.cards_deck) == 26)

    def test_set_hand_invalid_deck_type(self):
        """
        Tests that the function raises TypeError when given an invalid deck type
        """
        print('test_set_hand_invalid_deck_type')
        with self.assertRaises(TypeError):
            deck = [DeckOfCards()]
            self.player.set_hand(deck)

    def test_set_hand_deck_length_lower(self):
        """
        Tests what happens when the deck's length is less than the amount of cards to deal.
        In this case, the function should set the cards in the player's deck according to the deck's length
        """
        print('test_set_hand_deck_length_lower')
        for i in range(self.player.cards_to_deal+1): # cards_to_deal == 26 so running 27 times to make deck length 25
            self.deck.card_deck.pop()
        self.assertTrue(len(self.deck.card_deck) < self.player.cards_to_deal)
        self.player.set_hand(self.deck)
        self.assertTrue(len(self.player.cards_deck) < self.player.cards_to_deal)

    def test_get_card_deck_full(self):
        """
        Tests that the function returns a card correctly, the card is unique and not in the Deck.
        Deck length changes
        """
        print('test_get_card_deck_full')
        card = self.deck.deal_one()
        print(f'{card} of {type(card)}')
        self.assertNotIn(card,self.deck.card_deck)
        self.assertTrue(len(self.deck.card_deck)==51)
        self.assertTrue(isinstance(card,Card))

    def test_get_card_deck_empty(self):
        """
        Tests the function ValueError raise when player's deck is empty
        """
        print('test_get_card_deck_empty')
        self.player.set_hand(self.deck)
        for i in range(len(self.deck.card_deck)):
            self.player.get_card()
        with self.assertRaises(ValueError):
            self.player.get_card()

    def test_add_card_valid_card(self):
        """
        Tests the function adding the card correctly and making sure it's of Card object
        """
        print('test_add_card_valid_card')
        self.player.set_hand(self.deck)
        card = self.deck.deal_one()
        self.player.add_card(card)
        self.assertIn(card,self.player.cards_deck)
        self.assertNotIn(card,self.deck.card_deck)
        self.assertTrue(type(card) == Card)

    def test_add_card_invalid_card_type(self):
        """
        Tests the function raises TypeError when given an invalid card type
        """
        print('test_add_card_invalid_card_type')
        self.player.set_hand(self.deck)
        with self.assertRaises(TypeError):
            self.player.add_card(1)

    def test_add_card_already_exists(self):
        """
        Tests the function raises ValueError when given an already existing card
        """
        print('test_add_card_already_exists')
        card = self.deck.deal_one()
        self.player.add_card(card)
        with self.assertRaises(ValueError):
            self.player.add_card(card)

    def test_compare_decks_valid(self):
        """
        Tests that the function compares  the decks correctly and returns True when they are holding unique cards
        """
        print('test_compare_decks_valid')
        player = Player('ilay',26)
        self.player.set_hand(self.deck)
        player.set_hand(self.deck)
        self.assertTrue(self.player.compare_decks(player))

    def test_compare_decks_invalid_player_type(self):
        """
        Tests that the function raises TypeError when given an invalid player type
        """
        print('test_compare_decks_invalid_player_type')
        player = [Player('ilay',26)]
        with self.assertRaises(TypeError):
            self.player.compare_decks(player)

    def test_compare_decks_card_in_both_decks(self):
        """
        Tests the function raises ValueError when both decks have at least 1 card that is the same
        """
        print('test_compare_decks_card_in_both_decks')
        player = Player('ilay',26)
        self.player.set_hand(self.deck)
        player.set_hand(self.deck)
        player.cards_deck[5] = self.player.cards_deck[5]
        print(f'Player: {player.cards_deck[5]}')
        print(f'Self Player: {self.player.cards_deck[5]}')
        with self.assertRaises(ValueError):
            self.player.compare_decks(player)