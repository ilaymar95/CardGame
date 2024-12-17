from unittest import TestCase
from game_cards.player import Player
from game_cards.deck_of_cards import DeckOfCards
from game_cards.card import Card
from unittest import mock


class TestPlayer(TestCase):
    def setUp(self):
        print('This is setUp')
        self.deck = DeckOfCards()
        self.player = Player('ilay', 26)

    def tearDown(self):
        print('This is tearDown')
        self.player = None

    def test_init_valid(self):
        """
        Creates a valid Player object
        """
        self.assertEqual(self.player.name, 'ilay')
        self.assertEqual(self.player.cards_to_deal, 26)

    def test_init_invalid_name_type(self):
        """
        Tests that the function raises TypeError when given invalid player name type
        """
        with self.assertRaises(TypeError):
            player = Player(['ilay'], 25)

    def test_invalid_name_empty(self):
        """
        Tests that the function raises ValueError when given empty player name
        """
        with self.assertRaises(ValueError):
            player = Player('', 26)

    def test_valid_name_length_1(self):
        """
        Tests that the function makes a player with name length of 1 which is valid for the game
        """
        player = Player('i', 26)
        self.assertEqual(player.name, 'i')

    def test_valid_cards_to_deal_0(self):
        """
        Tests the player init that cards_to_deal is set to 26
        """
        player = Player('ilay', 0)
        self.assertTrue(player.cards_to_deal == 26)

    def test_valid_cards_to_deal_default(self):
        player = Player('ilay', )
        self.assertTrue(player.cards_to_deal == 26)

    def test_valid_cards_to_deal_10_26(self):
        """
        Tests the player init that cards_to_deal is set to 26 or 10 (edge values)
        """
        player = Player('ilay', 10)
        player2 = Player('david', 26)
        self.assertTrue(player.cards_to_deal == 10)
        self.assertTrue(player2.cards_to_deal == 26)

    def test_valid_cards_to_deal_26_27(self):
        print('test_valid_cards_to_deal_26_27')
        player = Player('ilay', 26)
        player2 = Player('david', 27)
        self.assertTrue(player.cards_to_deal == 26)
        self.assertTrue(player2.cards_to_deal == player.cards_to_deal)

    def test_invalid_cards_to_deal_type(self):
        """
        Tests that the function raises TypeError when given invalid cards_to_deal type
        """

        with self.assertRaises(TypeError):
            player = Player('ilay', '26')


    def test_set_hand_valid(self):
        """
        Tests that set_hand function sets the player's hand correctly
        """
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


    @mock.patch('game_cards.deck_of_cards.DeckOfCards.deal_one', return_value=Card(1, 1))
    def test_set_hand_mocked(self, mocked_card):
        self.player.set_hand(self.deck)
        self.assertTrue(len(self.player.cards_deck) == 26)
        for card in self.player.cards_deck:
            self.assertTrue(card.value == 1)
            self.assertTrue(card.suit == 1)


    def test_set_hand_deck_length_lower(self):
        """
        Tests what happens when the deck's length is less than the amount of cards to deal.
        In this case, the function should set the cards in the player's deck according to the deck's length
        """
        for i in range(self.player.cards_to_deal + 1):  # cards_to_deal == 26 so running 27 times to make deck length 25
            self.deck.card_deck.pop()
        self.assertTrue(len(self.deck.card_deck) < self.player.cards_to_deal)
        length = len(self.deck.card_deck)
        self.player.set_hand(self.deck)
        self.assertTrue(self.player.cards_to_deal == length)


    def test_get_card_deck_full(self):
        """
        Tests that the function returns a card correctly, the card is unique and not in the Deck.
        Deck length changes
        """
        self.player.set_hand(self.deck)
        card = self.player.get_card()
        self.assertTrue(len(self.player.cards_deck) < self.player.cards_to_deal)
        self.assertTrue(isinstance(card, Card))


    def test_get_card_deck_empty(self):
        """
        Tests the function ValueError raise when player's deck is empty
        """
        self.player.set_hand(self.deck)
        for i in range(len(self.deck.card_deck)):
            self.player.get_card()
        self.assertEqual(None,self.player.get_card())


    def test_add_card_valid_card(self):
        """
        Tests the function adding the card correctly and making sure it's of Card object
        """
        self.player.set_hand(self.deck)
        card = self.deck.deal_one()
        self.player.add_card(card)
        self.assertIn(card, self.player.cards_deck)
        self.assertTrue(isinstance(card, Card))

    def test_add_card_invalid_card_type(self):
        """
        Tests the function raises TypeError when given an invalid card type
        """
        self.player.set_hand(self.deck)
        with self.assertRaises(TypeError):
            self.player.add_card(1)

    def test_add_card_already_exists(self):
        """
        Tests the function raises ValueError when given an already existing card
        """
        card = self.deck.deal_one()
        self.player.add_card(card)
        with self.assertRaises(ValueError):
            self.player.add_card(card)