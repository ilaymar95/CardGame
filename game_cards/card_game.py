from game_cards.player import Player
from game_cards.card import Card
from game_cards.deck_of_cards import DeckOfCards


class CardGame:
    def __init__(self, player1_name: str, player2_name: str, amount: int):
        """
        The __init__ starts the game and creates a CardGame object
        The object receives names of 2 players
        """
        if type(player1_name) != str or type(player2_name) != str:
            raise TypeError('Player names must be strings!!!')
        if len(player1_name) < 1 or len(player2_name) < 1:
            raise ValueError('Player names must have at least 1 character!!!')
        if type(amount) != int:
            raise TypeError('Amounts to deal must be integers!!!')
        if amount < 10 or amount > 26:
            amount = 26
        self.player1 = Player(player1_name, amount)
        self.player2 = Player(player2_name, amount)
        self.card_deck = DeckOfCards()
        self._initialized_ = True
        self.new_game()
        self._initialized_ = False

    def new_game(self):
        """
        An inside method of CardGame object.
        Starts a new game, initialized from the __init__ method and cannot be used
        """
        if not self._initialized_:
           print("new_game() is private and cannot be accessed!!!")
        else:
            self.card_deck.cards_shuffle()
            self.player1.set_hand(self.card_deck)
            self.player2.set_hand(self.card_deck)

    def get_winner(self):
        if len(self.player1.cards_deck) > len(self.player2.cards_deck):
            return self.player1
        if len(self.player2.cards_deck) > len(self.player1.cards_deck):
            return self.player2
        return None
