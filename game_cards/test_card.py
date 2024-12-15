from unittest import TestCase
from game_cards.card import Card


class TestCard(TestCase):
    def setUp(self):
        print('This is setUp')
        self.card = Card(1, 1)

    def tearDown(self):
        print('This is tearDown')
        self.card = None

    def test_init_valid(self):
        print('This is test_init_valid')
        self.assertTrue(type(self.card) == Card)

    def test_init_valid_suit_all_suits(self):
        """
        Tests to check all the valid suits(1-4) for a Card object
        """
        print('test_init_valid_suit_all_suits')
        for suit in range(1, 5):
            card = Card(suit, 1)
            self.assertTrue(type(card) == Card)
            print('True')

    def test_init_invalid_suit_0(self):
        """
        Tests the bottom invalid number for a suit (0) and checks that it raises ValueError
        """
        print('test_init_invalid_suit_0')
        with self.assertRaises(ValueError):
            card = Card(0, 1)

    def test_init_invalid_suit_5(self):
        """
        Tests the top invalid number for a suit (5) and checks that it raises ValueError
        """
        print('test_init_invalid_suit_5')
        with self.assertRaises(ValueError):
            card = Card(5, 1)

    def test_init_invalid_suit_type(self):
        """
        Tests the invalid type for a suit (not a number) and checks that it raises TypeError
        """
        print('test_init_invalid_suit_type')
        with self.assertRaises(TypeError):
            card = Card('10', 1)

    def test_init_invalid_value_14(self):
        """
        Tests the invalid value for a card value (14) and checks that it raises ValueError
        """
        print('test_init_invalid_value_14')
        with self.assertRaises(ValueError):
            card = Card(1, 14)

    def test_init_invalid_value_0(self):
        """
        Tests the invalid value for a card value (0) and checks that it raises ValueError
        """
        print('test_init_invalid_value_0')
        with self.assertRaises(ValueError):
            card = Card(1, 0)

    def test_init_invalid_value_type(self):
        """
        Tests the invalid type for a card value and raises TypeError
        """
        print('test_init_invalid_value_type')
        with self.assertRaises(TypeError):
            card = Card(1, [1])

    def test__gt__valid_equal_suit(self):
        """
        Tests the valid __gt__ method showing the difference with Ace, King and 5
        :return:
        """
        print('test__gt__valid_equal_suit')
        card = Card(1, 13)
        card2 = Card(1, 5)
        self.assertTrue(self.card > card)
        self.assertTrue(card > card2)

    def test__gt__valid_equal_value(self):
        """
        Tests the valid __gt__ method showing the difference with equal value but different suits
        """
        print('test__gt__valid_equal_value')
        card = Card(2, 10)
        card2 = Card(1, 10)
        self.assertTrue(card2 > card)

    def test__gt__valid_different_cards(self):
        card1 = Card(1, 10)
        card2 = Card(4, 12)
        self.assertTrue(card2 > card1)

    def test__gt__other_ace(self):
        card1 = Card(1, 1)
        card2 = Card(2, 10)
        self.assertFalse(card2 > card1)

    def test__gt__invalid_type(self):
        card = "Card"
        with self.assertRaises(TypeError):
            self.assertTrue(self.card > card)

    def test__eq__valid_True_and_False(self):
        """
        Tests the __eq__ method
        """
        print('test__eq__valid_True_and_False')
        card = Card(1, 1)
        self.assertTrue(self.card == card)
        card2 = Card(2, 1)
        self.assertFalse(card == card2)

    def test__eq_invalid_type(self):
        """
        Tests the __eq__ method invalid type of other
        """
        print('test__eq_invalid_type')
        card = "Card"
        with self.assertRaises(TypeError):
            self.assertTrue(self.card == card)
