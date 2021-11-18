########## Angkan Baidya ##########
########## 112309655 #############
########## abaidya #############

import random
from typing import Type

pirateColors = ["blue", "green", "purple", "gold"]
maxPlayersAllowed = 5
minPlayersAllowed = 2
playerNames = ["Joy", "Nan", "Sat"]


class MerchantShip:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value
        


class PirateShip:
    def __init__(self, color, attack_value):
        self.color = color
        self.attack_value = attack_value

    def get_value(self):
        return self.attack_value

    def get_color(self):
        return self.color


class Captain:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color


class Admiral:
    __instance = None
    def __init__(self):
        if Admiral.__instance != None:
            raise Exception("This is a singleton")
        else:
            Admiral.__instance = self
        
    @staticmethod
    def get_instance():
        if Admiral.__instance == None:
            Admiral()
        return Admiral.__instance
        

class Player:
    def __init__(self, name):
        self.name = name
        self.merchant_ships_at_sea = []
        self.merchant_ships_captured = []
        self.hand = [] 
        self.merchant_pirates = {}
        self.dealer = False

    def deal(self, game_state):
        self.dealer = True
        random.shuffle(game_state.deck.cards)
        for i in game_state.players:
            while len(i.hand) < 6:
                cardtoadd = game_state.deck.cards.pop()
                if cardtoadd not in i.hand:
                    i.hand.append(cardtoadd)
                else:
                    game_state.deck.cards.append(cardtoadd)
                    random.shuffle(game_state.deck.cards)
            
    def see_hand(self):
        return self.hand

    def draw_card(self, game_state):
        card_to_add = game_state.deck.cards.pop()
        self.hand.append(card_to_add)

    def float_merchant(self, card):
        if type(card) != MerchantShip:
            return False
        for i in self.hand:
            if i == card: #find a merchant ship in players hand
                self.merchant_ships_at_sea.append(i)
                self.hand.remove(i)
                return True
        return False

    def play_pirate(self, pirate_card, merchant_card, p1):
        if type(pirate_card) != PirateShip:
            return False
        if type(merchant_card) != MerchantShip:
            return False
        if pirate_card not in self.hand:
            return False
        if merchant_card not in p1.merchant_ships_at_sea:
            return False
        color = pirate_card.get_color()
        if len(p1.merchant_pirates) != 0:
            for i in p1.merchant_pirates.keys():
                if p1.merchant_pirates[i][0][0] == self: #if already attacked
                    if p1.merchant_pirates[i][0][1].get_color() != color:
                        return False
        pairlist = [self,pirate_card] #make the pairlist of the player attacking and the pirate card
        if merchant_card not in p1.merchant_pirates: 
            p1.merchant_pirates[merchant_card] = []
        p1.merchant_pirates[merchant_card].append(pairlist)
        self.hand.remove(pirate_card) #add to the dic of the player w merchant ship, add the pirate attacking it
        return True #return true if all works

        

    def play_captain(self, captain_card, merchant_card, p1):
        if captain_card not in self.hand:
            return False
        if merchant_card not in p1.merchant_ships_at_sea:
            return False
        color = captain_card.get_color()
        if len(p1.merchant_pirates) != 0:
            for i in p1.merchant_pirates.keys():
                if p1.merchant_pirates[i][0][0] == self: #if already attacked
                    if p1.merchant_pirates[i][0][1].get_color() != color:
                        return False
        pairlist = [self,captain_card] #make the pairlist of the player attacking and the pirate card 
        if merchant_card not in p1.merchant_pirates: 
            p1.merchant_pirates[merchant_card] = []
        p1.merchant_pirates[merchant_card].append(pairlist)
        self.hand.remove(captain_card)
        return True

    def play_admiral(self, admiral_card, merchant_card):
        checkformerchant = False
        if admiral_card not in self.hand:
            return False
        if len(self.merchant_pirates) < 1:
            return False
        for i in self.merchant_pirates.keys():
            if i == merchant_card:
                checkformerchant = True
        if checkformerchant == False:
            return False 
        pairlist = [self,admiral_card] #make the pairlist of the player attacking and the pirate card 
        if merchant_card not in self.merchant_pirates:
            self.merchant_pirates[merchant_card] = []
        self.merchant_pirates[merchant_card].append(pairlist)
        self.hand.remove(admiral_card)
        return True

class Deck:
    __instance = None
    def __init__(self):
    
        if Deck.__instance != None:
            raise Exception("This is a singleton")
        else:
            self.cards = []
            Merchant8pts = MerchantShip(8)
            self.cards.append(Merchant8pts)
            Merchant7pts = MerchantShip(7)
            self.cards.append(Merchant7pts)
            for i in range(2):
                Merchant6pts = MerchantShip(6)
                self.cards.append(Merchant6pts)
            for i in range(5):
                Merchant5pts = MerchantShip(5)
                Merchant4pts = MerchantShip(4)
                Merchant2pts = MerchantShip(2)
                self.cards.append(Merchant5pts)
                self.cards.append(Merchant4pts)
                self.cards.append(Merchant2pts)
            for i in range(6):
                Merchant3pts = MerchantShip(3)
                self.cards.append(Merchant3pts)
            AdmiralCard = Admiral.get_instance()
            self.cards.append(AdmiralCard)
            for i in range(2):
                PirateCard1 = PirateShip("blue",1)
                PirateCard4 = PirateShip("blue",4)
                self.cards.append(PirateCard1)
                self.cards.append(PirateCard4)
            for i in range(4):
                PirateCard2 = PirateShip("blue",2)
                PirateCard3 = PirateShip("blue",3)
                self.cards.append(PirateCard2)
                self.cards.append(PirateCard3)
            for i in range(2):
                PirateCard1 = PirateShip("green",1)
                PirateCard4 = PirateShip("green",4)
                self.cards.append(PirateCard1)
                self.cards.append(PirateCard4)
            for i in range(4):
                PirateCard2 = PirateShip("green",2)
                PirateCard3 = PirateShip("green",3)
                self.cards.append(PirateCard2)
                self.cards.append(PirateCard3)
            for i in range(2):
                PirateCard1 = PirateShip("purple",1)
                PirateCard4 = PirateShip("purple",4)
                self.cards.append(PirateCard1)
                self.cards.append(PirateCard4)
            for i in range(4):
                PirateCard2 = PirateShip("purple",2)
                PirateCard3 = PirateShip("purple",3)
                self.cards.append(PirateCard2)
                self.cards.append(PirateCard3)
            for i in range(2):
                PirateCard1 = PirateShip("gold",1)
                PirateCard4 = PirateShip("gold",4)
                self.cards.append(PirateCard1)
                self.cards.append(PirateCard4)
            for i in range(4):
                PirateCard2 = PirateShip("gold",2)
                PirateCard3 = PirateShip("gold",3)
                self.cards.append(PirateCard2)
                self.cards.append(PirateCard3)
            CaptainBlue = Captain("blue")
            CaptainGreen = Captain("green")
            CaptainPurple = Captain("purple")
            CaptainGold = Captain("gold")
            self.cards.append(CaptainBlue)
            self.cards.append(CaptainGreen)
            self.cards.append(CaptainPurple)
            self.cards.append(CaptainGold)
            Deck.__instance = self



    @staticmethod
    def get_instance():
        if Deck.__instance == None:
            Deck()
        return Deck.__instance


class Game:
    def __init__(self, deck):
        self.deck = deck
        self.players = []
        self.current_player = Player


    def create_players(self, names, min_players, max_players):
        playerslist = []
        if (len(names) < min_players) | (len(names) > max_players):
            raise Exception("Players Exception")
        for i  in names:
            playermade = Player(i)
            playerslist.append(playermade)
        self.players = playerslist
        

    def random_player(self):
        return random.choice(self.players)

    def start(self):
        counter = 0 
        dealerindex = 0
        for i in self.players:
            if i.dealer == True:
                dealerindex = counter # gets index
            else:
                counter = counter + 1 
        if dealerindex == 0:
            self.current_player = self.players[-1]
            return self.players[-1] #return last player 
        else:
            self.current_player = self.players[dealerindex -1]
            return self.players[dealerindex -1]

    def next(self):
        counter = 0
        playerindex = 0
        for i in self.players:
            if i == self.current_player:
                playerindex = counter
            else:
                counter = counter + 1
        if playerindex == len(self.players) - 1:
            self.current_player = self.players[0]
            return self.players[0]
        else:
            self.current_player = self.players[playerindex + 1]
            return self.players[playerindex + 1]

        

    def choose_player(self, pos):
        if pos > len(self.players):
            return None
        indextochoose = pos-1
        return self.players[indextochoose]


    def capture_merchant_ships(self):
        highestplayer = None
        highestValue = None
        samescorecheck = True
        for i in self.players: #go through all players
            
            if len(i.merchant_pirates) == 0 and (len(i.merchant_ships_at_sea) > 0):
                for ship in i.merchant_ships_at_sea:
                    samescorecheck = False
                    i.merchant_ships_captured.append(ship)
                    i.merchant_ships_at_sea.remove(ship)
            if len(i.merchant_pirates) == 0: 
                continue #if no merchant ship played go to next player 
            else:
                for x in i.merchant_pirates.keys(): #go thrugh merchant list,
                    playerdict = {}
                    valuedict = {}
                    TypeofAttacker = i.merchant_pirates[x][-1][1]
                    PlayerofAttack = i.merchant_pirates[x][-1][0] 
                    numberofiterations = len(i.merchant_pirates[x]) # number of attacks on each ship 
                    highestValue = 0
                    if (type(TypeofAttacker) == Admiral) | (type(TypeofAttacker) == Captain): #if last card played was captain or admiral
                        PlayerofAttack.merchant_ships_captured.append(x) #append that specific merchant ship 
                        #remove that specific merchant ship 
                        i.merchant_ships_at_sea.remove(x) #remove from at sea 
                        continue #go to next key 
                    for values in range(numberofiterations): #for each attack 
                        currentplayer = i.merchant_pirates[x][values][0] #currentplayer
                        currentCardType = i.merchant_pirates[x][values][1] #currentType
                        currentCardValue = currentCardType.get_value() #current value of the pirate ship 
                        if currentplayer in playerdict:
                            playerdict[currentplayer].append(currentCardValue)
                        else: #new addition to dict
                            playerdict[currentplayer] = []
                            playerdict[currentplayer].append(currentCardValue) #appendvalue of pirate of that specific player
                    for player in playerdict.keys(): # for each player get the total value 
                        currentp = player
                        currentnumber = 0
                        for numbers in playerdict[player]:  #for each value in the list john:[2,3] x is 2 or 3
                            currentnumber = numbers + currentnumber
                        if currentp not in valuedict:
                             valuedict[currentp] = []
                        valuedict[currentp].append(currentnumber)
                    for z in valuedict.keys(): #will product highest player and highest value 
                        current_player = z
                        current_score = valuedict[z]
                        if highestplayer == None:
                            highestplayer = z
                            highestValue = valuedict[z]
                        if current_score < highestValue:
                            samescorecheck = False
                        if current_score > highestValue:
                            highestValue = current_score
                            highestplayer = current_player
                            samescorecheck = False
                    if samescorecheck == True and len(valuedict)>1:
                        continue
                    highestplayer.merchant_ships_captured.append(x) #append the current merchant ship
                    i.merchant_ships_at_sea.remove(x) #remove from at sea 
                if samescorecheck == False:
                    i.merchant_pirates.pop(x)


    def show_winner(self):
        pairlist = []
        valueofgold = 0 
        for i in self.players:
            valueofgold = 0
            for x in i.merchant_ships_captured:
                valueofgold = x.get_value() + valueofgold #value of current merchant ship 
            listtoadd = [i,valueofgold]
            pairlist.append(listtoadd)  
        return pairlist 



otherother = Game(Deck.get_instance())
Player1 = Player("John")
Player2 = Player("Joe")     
testcard = PirateShip("green",5)
testcard2 = MerchantShip(5)
merchantotest = MerchantShip(7)
otherother.players.append(Player1)
otherother.players.append(Player2)
Player1.hand.append(testcard2)
Player1.float_merchant(testcard2)
otherother.capture_merchant_ships()


