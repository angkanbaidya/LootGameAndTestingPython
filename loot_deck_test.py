########## Angkan Baidya ##########
########## 112309655 #############
########## abaidya #############

import unittest
import loot 


class loot_deck_test(unittest.TestCase):

    def test_deck_multiple_instance(self):
        Deck1 = loot.Deck.get_instance()
        with self.assertRaises(Exception):
            Deck2 = loot.Deck()

    def test_total_cards(self):
        Deck1 = loot.Deck.get_instance()
        self.assertEqual(78,len(Deck1.cards),"Not enough cards!")

    def test_total_merchant_cards(self):
        counter = 0
        Deck =  loot.Deck.get_instance()
        for i in Deck.cards:
            if type(i) == loot.MerchantShip:
                counter = counter +1
        self.assertEqual(25,counter,"Not enough Merchant Cards!")

    def test_total_pirate_cards(self):
        counter = 0
        Deck = loot.Deck.get_instance()
        for i in Deck.cards:
            if type(i) == loot.PirateShip:
                counter = counter +1
        self.assertEqual(48,counter,"Not Enough Pirate Ship Cards!")

    def test_total_Admiral_cards(self):
        counter = 0
        Deck = loot.Deck.get_instance()
        for i in Deck.cards:
            if type(i) == loot.Admiral:
                counter = counter +1
        self.assertEqual(1,counter,"Too many Admiral Cards")

    def test_total_pirate_captain_cards(self):
        counter = 0
        Deck = loot.Deck.get_instance()
        for i in Deck.cards:
            if type(i) == loot.Captain:
                counter = counter +1
        self.assertEqual(4,counter,"too many Admiral Cards")

    def test_pirate_captain_color(self):
        correctcolor = False
        Deck = loot.Deck.get_instance()
        for i in Deck.cards:
            if type(i) == loot.Captain:
                if (i.get_color() == "blue") or (i.get_color() == "green") or (i.get_color() == "purple") or (i.get_color() == "gold"):
                    correctcolor = True
                else:
                    correctcolor = False
        self.assertTrue(correctcolor,"not correct colors!")

    def test_merchant_numbers(self):
        correctnumbers = False
        Deck = loot.Deck.get_instance()
        for i in Deck.cards:
            if type(i) == loot.MerchantShip:
                if (i.get_value() == 2) or (i.get_value() == 3) or (i.get_value() == 4) or (i.get_value() == 5) or (i.get_value() == 6) or (i.get_value() == 7)or (i.get_value() == 8):
                    correctnumbers = True
                else:
                    correctnumbers = False 
        self.assertTrue(correctnumbers,"not correct colors!")
    
    def test_pirate_color(self):
        correctcolor = False
        Deck = loot.Deck.get_instance()
        for i in Deck.cards:
            if type(i) == loot.PirateShip:
                if (i.get_color() == "blue") or (i.get_color() == "green") or (i.get_color() == "purple") or (i.get_color() == "gold"):
                    correctcolor = True
                else:
                    correctcolor = False
        self.assertTrue(correctcolor,"not correct colors!")
    
    def test_merchant_each_gold_value(self):
        twocounter = 0
        threecounter = 0
        fourcounter = 0
        fivecounter = 0
        sixcounter =0
        sevencounter = 0
        eightcounter = 0
        Deck = loot.Deck.get_instance()
        for i in Deck.cards:
            if type(i) == loot.MerchantShip:
                if i.get_value() == 2:
                    twocounter = twocounter +1
                if i.get_value() == 3:
                    threecounter = threecounter +1
                if i.get_value() == 4:
                    fourcounter = fourcounter +1
                if i.get_value() == 5:
                    fivecounter = fivecounter +1
                if i.get_value() == 6:
                    sixcounter = sixcounter +1
                if i.get_value() == 7:
                    sevencounter = sevencounter +1
                if i.get_value() == 8:
                    eightcounter = eightcounter +1
        self.assertEqual(5,twocounter,"Not correct amount of 2 cards")
        self.assertEqual(6,threecounter,"Not correct amount of 3 cards")
        self.assertEqual(5,fourcounter,"Not correct amount of 4 cards")
        self.assertEqual(5,fivecounter,"Not correct amount of 5 cards")
        self.assertEqual(2,sixcounter,"Not correct amount of 6 cards")
        self.assertEqual(1,sevencounter,"Not correct amount of 7 cards")
        self.assertEqual(1,eightcounter,"Not correct amount of 8 cards")
 
    def test_pirate_each_attack_value(self):
        onecounter = 0
        twocounter = 0
        threecounter = 0
        fourcounter = 0
        Deck = loot.Deck.get_instance()
        for i in Deck.cards:
            if type(i) == loot.PirateShip:
                if i.get_value() == 1:
                    onecounter = onecounter +1
                if i.get_value() == 2:
                    twocounter = twocounter +1
                if i.get_value() == 3:
                    threecounter = threecounter +1
                if i.get_value() == 4:
                    fourcounter = fourcounter +1
        self.assertEqual(8,onecounter,"Not correct amount of 1 attack strength")
        self.assertEqual(16,twocounter,"Not correct amount of 2 attack strength")
        self.assertEqual(16,threecounter,"Not correct amount of 3 attack strength")
        self.assertEqual(8,fourcounter,"Not correct amount of 4 attack strength")
        








