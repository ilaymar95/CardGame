from game_cards.deck_of_cards import DeckOfCards
from game_cards.card import Card
from random import randint

class Player:
    def __init__(self,name:str,cards_to_deal:int):
        """
        __init__ gets a name(string) and amount of cards to deal(int) and creates a Player with an empty card deck
        """
        if type(name) != str:
            raise TypeError("Name must be a string")
        if len(name)<1:
            raise ValueError("Name cannot be empty")
        if type(cards_to_deal) != int:
            raise TypeError("Cards_to_deal must be an integer")
        if cards_to_deal<10 or cards_to_deal>26:
            cards_to_deal=26
        self.name = name
        self.cards_to_deal=cards_to_deal
        self.cards_deck = []

    def __str__(self):
        """
        Returns string representation of Player object with name and cards
        """
        return f"Player name: {self.name}\nCards: {[card for card in self.cards_deck]}"

    def set_hand(self, card_deck: DeckOfCards):
        """
        The function gets a deck of cards.
        Sets the hand of the player according to the player's cards_to_deal variable
        """
        if type(card_deck) != DeckOfCards:
            raise TypeError("Card deck must be of type DeckOfCards")
        if len(card_deck.card_deck)<self.cards_to_deal:
            for i in range(len(card_deck.card_deck)):
                self.cards_deck.append(card_deck.card_deck.pop())
        else:
            while len(self.cards_deck)<self.cards_to_deal:
                self.cards_deck.append(card_deck.deal_one())

    def get_card(self):
        """
        The function returns a random card from the player's cards_deck
        """
        if len(self.cards_deck)<1:
            raise ValueError("Card deck cannot be empty")
        return self.cards_deck.pop(randint(0,len(self.cards_deck)-1))

    def add_card(self,card:Card):
        """
        The function adds a card to the deck of cards.
        The function will raise an error when the card is not of Card object, or if it's already in the Deck
        """
        if type(card) != Card:
            raise TypeError("Card must be of type Card")
        if card in self.cards_deck:
            raise ValueError("Card already in deck! Not a possible option!!!")
        self.cards_deck.append(card)

    def compare_decks(self,other):
        """
        The function compares the decks between 2 Players and returns True if they're unique, False otherwise
        """
        if type(other) != Player:
            raise TypeError("Player must be of type Player")
        for card in self.cards_deck:
            if card in other.cards_deck:
                raise ValueError("Card already in deck! Not a possible option!!!")
        return True
