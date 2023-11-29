from card import Card
import random

class Deck:

    def __init__(self):
        self.deck = []
        for i in range(1, 5):
            for j in range(1, 14):
                self.deck.append(Card(i, j).get_card())

    # -- Modifier Methods -- #
    def drawCard(self):
        return self.deck[random.randrange(len(self.deck))]

    # -- Accessor Methods -- #
    def getCards(self):
        name = ""
        for card in self.deck:
            name += str(card) + ", "
        return name[:len(name)-2]
