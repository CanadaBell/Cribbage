class Card:
    '''
    Card in Deck of Cards
    '''
    suits = {
        1: "Diamonds",
        2: "Clubs",
        3: "Hearts",
        4: "Spades"
    }

    values = {
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "10",
        11: "J",
        12: "Q",
        13: "K"
    }

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"<card.Card object at {Card.values[self.value]} of {Card.suits[self.suit]}>"

    # Accessor Methods
    def __str__(self):
        return f"{Card.values[self.value]}{Card.suits[self.suit]}"
    
    def get_card(self):
        return f"{Card.values[self.value]}-{Card.suits[self.suit]}"

    def getValue(self):
        return self.value