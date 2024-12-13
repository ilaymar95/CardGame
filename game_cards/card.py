class Card:
    def __init__(self, suit:int, value:int):
        """
        receives values for suit(int 1-4) and value(int 1-13) and creates a Card
        """
        if type(suit) != int:
            raise TypeError("Suit must be an integer")
        if type(value) != int:
            raise TypeError("Value must be an integer")
        if suit>4 or suit<1:
            raise ValueError(f"Suit must be 1 - 4!")
        if value>13 or value<1:
            raise ValueError(f"Value must be 1 - 13!")
        self.suit = suit
        self.value = value

    def __repr__(self):
        """
        returns a string representation of the card
        """
        suits = ['Diamonds','Spades','Hearts','Clubs']
        values = [None, "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        return f'[{values[self.value]} of {suits[self.suit-1]}]'

    def __gt__(self, other):
        """
        returns True if current Card beats other Card, False otherwise
        """
        if type(other) != Card:
            raise TypeError(f'{other} is not a Card')
        #Case to check Ace(Lowest value but strongest Card)
        if self.value == 1:
            return other.value!=1 or self.suit<other.suit
        if other.value == 1:
            return False
        #If the suits are the same, compare by value
        if self.suit == other.suit:
            return self.value > other.value
        if self.value == other.value:
            return self.suit < other.suit
        return self.value > other.value

    def __eq__(self,other):
        """
        returns True of self == other, False otherwise
        """
        if type(other) != Card:
            raise TypeError(f'{other} is not a Card')
        return self.suit == other.suit and self.value == other.value

