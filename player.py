from hand import Hand

class Player:

    def __init__(self, firstName):
        self.name = firstName
        self.library = Hand()
        self.score = 0

    # -- Modifier Methods -- #
    def addHand(self, cards):
        self.library.addCards(cards)

    def drawCard(self, card):
        return self.library.hand.pop(card)
    
    def addScore(self, score_to_add):
        self.score += score_to_add


    # -- Accessor Methods -- #

    def getName(self):
        return self.name
    
    def getScore(self):
        return self.score
