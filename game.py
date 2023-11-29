from deck import Deck
from player import Player
from hand import Hand
from sys import exit
import random
import os
import time

# class Game:

#     

#     # -- Accessor Methods -- #
#     def intro(self):
#         print("War is ridiculous in real life and as a card game!")

#     # -- Modifier Methods -- #

class Game:

    def __init__(self):
        self.deck = Deck()
        self.player = []
        self.inPlay = []
        self.roundNumber = 0
        self.crib = Hand()

    def setup(self):
        self.player.append(Player(input("Player Name: ")))
        self.player.append(Player(input("Computer Name: ")))


    def computer_round(self):
        for user in self.player:
            player_hand = []
            player_hand = [self.deck.drawCard() for card in range(6)]
            user.addHand(player_hand)
        if self.player[0].getScore() >= 121:
            print(f"{self.player[1].getName()} wins!")
            exit()
        elif self.player[1].getScore() >= 121:
            print(f"{self.player[0].getName()} wins!")
            exit()
        else:
            # Adding cards to crib
            crib_hand = []

            # Removing cards from computers hand
            crib_hand.append(self.player[1].drawCard(random.randint(0, 5)))
            crib_hand.append(self.player[1].drawCard(random.randint(0, 4)))

            # Removing cards from players hand
            player_hand = self.player[0].library.get_hand() # Player's current hand

            print (player_hand)

            card1 = input("First card to discard?: ")
            while True: 
                if card1 in player_hand: 
                    card1 = self.player[0].library.hand.index(card1)
                    break
                try: 
                    card1 = (int(card1) - 1)
                    if card1 < 0 or card1 > 5:
                        card1 = input('Please input a valid card > ')
                        continue
                    break
                except ValueError:
                    card1 = input('Please choose a card > ')
            
     

            card2 = input("Second card to discard?: ")
            while True: 
                if card2 == card1:
                    card2 = input('Card2 same as card1, pick new card > ')
                if card2 in player_hand: 
                    card2 = self.player[0].library.hand.index(card2)
                    break
                try: 
                    card2 = (int(card2) - 1)
                    if card2 < 0 or card2 > 5:
                        card2 = input('Please input a valid card > ')
                        continue
                    break
                except ValueError:
                    card2 = input('Please choose a card > ')

            crib_hand.append(self.player[0].drawCard(card1))
            crib_hand.append(self.player[0].drawCard(card2 - 1))

            self.crib.addCards(crib_hand)
            self.crib.calculate_points()

            # Getting score of player/computer hands
            self.player[0].library.calculate_points()
            self.player[1].library.calculate_points()


            # Playing
            player = self.player[0]
            computer = self.player[1]
            cards_on_table = []
            card_total = 0
            c_skip_turn = False
            p_skip_turn = False

            while card_total < 31:
                if c_skip_turn == True and p_skip_turn == True: break
                c_playable_cards = []
                
                for card in computer.library.get_hand():

                    card_v = card[:card.index('-')]
                    try: card_v = int(card_v)
                    except ValueError: card_v = 10

                    if card_v + card_total <= 31: 
                        c_playable_cards.append(card)
                
                print (c_playable_cards)
                if len(c_playable_cards) == 0:
                    print ("Skipping Computer's turn")
                    c_skip_turn = True
                    time.sleep(2)
                else:
                    card_drawn = computer.drawCard(random.randint(0, (len(c_playable_cards)  - 1)))

                    card_v = card_drawn[:card_drawn.index('-')]
                    try: card_v = int(card_v)
                    except ValueError: card_v = 10

                    card_total += card_v
                    
                    cards_on_table.append(card_drawn)

                    if card_total == 15 or card_total == 31: computer.addScore(2)
                
                os.system('cls' if os.name =='nt' else 'clear')

                p_playable_cards = []
                for card in player.library.get_hand():

                    card_v = card[:card.index('-')]
                    try: card_v = int(card_v)
                    except ValueError: card_v = 10

                    if card_v + card_total <= 31: 
                        p_playable_cards.append(card)

                print (p_playable_cards)
                print (f"Table Value: {card_total}")
                if len(p_playable_cards) == 0:
                    print ("Skipping Player's turn")
                    p_skip_turn = True
                    time.sleep(2)
                else:
                    card_drawn = input("What card do you want to draw?: ")
                    while True: 
                        if card_drawn in p_playable_cards:
                            card_drawn = player.library.hand.index(card_drawn)
                            break
                        try: 
                            card_drawn = (int(card_drawn) - 1)
                            if card_drawn < 0 or card_drawn > (len(p_playable_cards) - 1):
                                card_drawn = input('Please input a card > ')
                                continue
                            break
                        except ValueError:
                            card_drawn = input('Please choose valid card > ')
                    card_drawn = player.drawCard(card_drawn)
                
                    card_v = card_drawn[:card_drawn.index('-')]
                    try: card_v = int(card_v)
                    except ValueError: card_v = 10

                    card_total += card_v

                    if card_total == 15 or card_total == 31: computer.addScore(2)   

                    cards_on_table.append(card_drawn)

            player.addScore(player.library.get_points())
            computer.addScore(computer.library.get_points())
            computer.addScore(self.crib.get_points())

    def player_round(self):
        for user in self.player:
            player_hand = []
            player_hand = [self.deck.drawCard() for card in range(6)]
            user.addHand(player_hand)
        if self.player[0].getScore() >= 121:
            print(f"{self.player[1].getName()} wins!")
            exit()
        elif self.player[1].getScore() >= 121:
            print(f"{self.player[0].getName()} wins!")
            exit()
        else:
            # Adding cards to crib
            crib_hand = []

            # Removing cards from computers hand
            crib_hand.append(self.player[1].drawCard(random.randint(0, 5)))
            crib_hand.append(self.player[1].drawCard(random.randint(0, 4)))

            # Removing cards from players hand
            player_hand = self.player[0].library.get_hand() # Player's current hand

            print (player_hand)

            card1 = input("First card to discard?: ")
            while True: 
                if card1 in player_hand: 
                    card1 = self.player[0].library.hand.index(card1)
                    break
                try: 
                    card1 = (int(card1) - 1)
                    if card1 < 0 or card1 > 5:
                        card1 = input('Please input a valid card > ')
                        continue
                    break
                except ValueError:
                    card1 = input('Please choose a card > ')
            
     

            card2 = input("Second card to discard?: ")
            while True: 
                if card2 == card1:
                    card2 = input('Card2 same as card1, pick new card > ')
                if card2 in player_hand: 
                    card2 = self.player[0].library.hand.index(card2)
                    break
                try: 
                    card2 = (int(card2) - 1)
                    if card2 < 0 or card2 > 5:
                        card2 = input('Please input a valid card > ')
                        continue
                    break
                except ValueError:
                    card2 = input('Please choose a card > ')

            crib_hand.append(self.player[0].drawCard(card1))
            crib_hand.append(self.player[0].drawCard(card2 - 1))

            self.crib.addCards(crib_hand)
            self.crib.calculate_points()

            # Getting score of player/computer hands
            self.player[0].library.calculate_points()
            self.player[1].library.calculate_points()


            # Playing
            player = self.player[0]
            computer = self.player[1]
            cards_on_table = []
            card_total = 0
            c_skip_turn = False
            p_skip_turn = False

            while card_total < 31:
                if c_skip_turn == True and p_skip_turn == True: break

                p_playable_cards = []
                for card in player.library.get_hand():

                    card_v = card[:card.index('-')]
                    try: card_v = int(card_v)
                    except ValueError: card_v = 10

                    if card_v + card_total <= 31: 
                        p_playable_cards.append(card)

                print (p_playable_cards)
                print (f"Table Value: {card_total}")
                if len(p_playable_cards) == 0:
                    print ("Skipping Player's turn")
                    p_skip_turn = True
                    time.sleep(2)
                else:
                    card_drawn = input("What card do you want to draw?: ")
                    while True: 
                        if card_drawn in p_playable_cards:
                            card_drawn = player.library.hand.index(card_drawn)
                            break
                        try: 
                            card_drawn = (int(card_drawn) - 1)
                            if card_drawn < 0 or card_drawn > (len(p_playable_cards) - 1):
                                card_drawn = input('Please input a card > ')
                                continue
                            break
                        except ValueError:
                            card_drawn = input('Please choose valid card > ')
                    card_drawn = player.drawCard(card_drawn)
                
                    card_v = card_drawn[:card_drawn.index('-')]
                    try: card_v = int(card_v)
                    except ValueError: card_v = 10

                    card_total += card_v

                    if card_total == 15 or card_total == 31: computer.addScore(2)   

                    cards_on_table.append(card_drawn)

                    c_playable_cards = []
                
                for card in computer.library.get_hand():

                    card_v = card[:card.index('-')]
                    try: card_v = int(card_v)
                    except ValueError: card_v = 10

                    if card_v + card_total <= 31: 
                        c_playable_cards.append(card)

                os.system('cls' if os.name =='nt' else 'clear')
                
                print (c_playable_cards)
                if len(c_playable_cards) == 0:
                    print ("Skipping Computer's turn")
                    c_skip_turn = True
                    time.sleep(2)
                else:
                    card_drawn = computer.drawCard(random.randint(0, (len(c_playable_cards)  - 1)))

                    card_v = card_drawn[:card_drawn.index('-')]
                    try: card_v = int(card_v)
                    except ValueError: card_v = 10

                    card_total += card_v
                    
                    cards_on_table.append(card_drawn)

                    if card_total == 15 or card_total == 31: computer.addScore(2)
                

            player.addScore(player.library.get_points())
            computer.addScore(computer.library.get_points())
            player.addScore(self.crib.get_points())
            
    def run(self):
        self.setup()
        while True:
            if self.roundNumber % 2 == 0:
                self.computer_round()
                os.system('cls' if os.name =='nt' else 'clear')
            else:
                self.player_round()
                os.system('cls' if os.name =='nt' else 'clear')
            self.roundNumber += 1 

Game().run() 