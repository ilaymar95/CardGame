from game_cards.card import Card
from random import randint, random, shuffle


class DeckOfCards:
    def __init__(self):
        """
        Creates a deck of 52 unique cards in random order
        """
        self.card_deck = []
        while len(self.card_deck) < 52:
            card = Card(randint(1,4),randint(1,13))
            if card not in self.card_deck:
                self.card_deck.append(card)

    def __repr__(self):
        return f"Card deck: {self.card_deck}"

    def cards_shuffle(self):
        """
        Shuffles the deck of cards using Python's shuffle() method
        """
        if len(self.card_deck) <1:
            raise ValueError("Deck of cards cannot be empty")
        else:
            shuffle(self.card_deck)

    def deal_one(self):
        """
        removes and returns 1 random card from the deck
        """
        if len(self.card_deck) == 0:
            return None
        return self.card_deck.pop(randint(0,len(self.card_deck)-1))



