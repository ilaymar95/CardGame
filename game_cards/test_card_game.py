from unittest import TestCase
from game_cards.card_game import CardGame
from game_cards.card import Card
from game_cards.player import Player
from game_cards.deck_of_cards import DeckOfCards


class TestCardGame(TestCase):
    def setUp(self):
        print('This is a setUp')
        player1 = Player('ilay', 26)
        player2 = Player('david', 26)
        self.game = CardGame(player1.name, player2.name, 26)

    def tearDown(self):
        print('This is a tearDown')
        self.game = None

    def test_init_valid(self):
        """
        Tests that the function creates a new game correctly and sets the player hands
        """
        self.assertTrue(type(self.game.player1) == Player)
        self.assertTrue(type(self.game.player2) == Player)
        self.assertTrue(len(self.game.player1.cards_deck) == len(self.game.player2.cards_deck))
        self.assertTrue(len(self.game.player1.cards_deck) == 26)
        self.assertTrue(type(self.game.card_deck) == DeckOfCards)

    def test_init_invalid_player_name_type(self):
        """
        Tests that the function raises TypeError when given invalid player name type(not string)
        """
        with self.assertRaises(TypeError):
            self.game = CardGame(self.game.player1, 'ilay', 26)

    def test_init_invalid_player_name_length(self):
        """
        Tests that the function raises ValueError when given invalid player name length(less than 1) for either players
        """
        with self.assertRaises(ValueError):
            self.game = CardGame('il', '', 26)

    def test_init_invalid_amount_type(self):
        """
        Tests that the function raises TypeError when given invalid type for amount of cards (not integer)
        """
        with self.assertRaises(TypeError):
            self.game = CardGame('ilay', 'david', '26')

    def test_init_amount_over_26(self):
        """
        Tests that the init uses Player object correctly, and because Player already makes sure the amount
        is 10-26, as long as an Integer will be sent, it should create with the default 26 cards per player
        """
        self.game = CardGame('ilay', 'david', 100)
        self.assertTrue(len(self.game.player1.cards_deck) == 26)
        self.assertTrue(len(self.game.player1.cards_deck) == len(self.game.player2.cards_deck))

    def test_get_winner_first_winner(self):
        self.game.player1.add_card(self.game.player2.get_card())
        self.assertTrue(self.game.player1, self.game.get_winner())

    def test_get_winner_second_winner(self):
        self.game.player2.add_card(self.game.player1.get_card())
        self.assertTrue(self.game.player2,self.game.get_winner())

    def test_get_winner_tie(self):
        self.assertEqual(None, self.game.get_winner())
