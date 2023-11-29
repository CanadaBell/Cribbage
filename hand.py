class Hand:
    
    def __init__(self, given_cards:list = []):
        self.hand = given_cards
        self.hand_points = 0

    def __str__(self): 
        return (f"given hand = {self.hand}, hand points = {self.hand_points}")    
    
    def addCards(self, cards:list):
        self.hand = cards


    def calculate_points(self):
        of_a_kind = []
        pairs_add_15 = []


        for card1 in self.hand:
            for card2 in self.hand:
                if card1 == card2: continue

                if card1[:1] == card2[:1]:
                    of_a_kind.append((card1, card2))

        
        for pair1 in of_a_kind:
            for pair2 in of_a_kind:
                if pair1 == pair2: continue

                if pair1[0] in pair2 and pair1[1] in pair2:
                    of_a_kind.remove(pair2)

        for card1 in self.hand:
            for card2 in self.hand:
                card_1 = card1[:card1.index('-')]
                try: card_1 = int(card_1)
                except ValueError: card_1 = 10

                card_2 = card2[:card2.index('-')]
                try: card_2 = int(card_2)
                except ValueError: card_2 = 10

                if card_1 + card_2 == 15:
                    pairs_add_15.append((card1, card2))
                
        for pair1 in pairs_add_15:
            for pair2 in pairs_add_15:
                if pair1 == pair2: continue

                if pair1[0] in pair2 and pair1[1] in pair2:
                    pairs_add_15.remove(pair2)     

        for same in of_a_kind:
            if len(same) == 2: self.hand_points += 2; print (f'added 2 because pair {same}')
            if len(same) == 3: self.hand_points += 6; print (f'added 6 {same}')
            if len(same) == 4: self.hand_points += 12; print (f'added 12 {same}')

        for pair in pairs_add_15:
            self.hand_points += 2; print (f'added 2 because 15 {pair}')

    def get_points(self):
        return self.hand_points
    
    def get_hand(self):
        return self.hand