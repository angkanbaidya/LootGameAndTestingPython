########## Angkan Baidya ##########
########## 112309655  #############
########## abaidya #############

from os import P_ALL
import unittest
import loot


class loot_play_test(unittest.TestCase):




    def test_min_max_players(self):
        newGame = loot.Game(loot.Deck.get_instance())
        maxPlayersAllowed = 5
        minPlayersAllowed = 2
        playerNames = ["Joy", "Nan", "Sat","July","Josh","Jake","Adam"] 
        with self.assertRaises(Exception):
            newGame.create_players(playerNames,minPlayersAllowed,maxPlayersAllowed)
    
    def test_cards_after_deal_and_dealer(self):
        othergametwo = loot.Game(loot.Deck.get_instance())
        maxPlayersAllowed = 5
        minPlayersAllowed = 2
        playerNames = ["Joy", "Nan", "Sat"]
        othergametwo.create_players(playerNames,minPlayersAllowed,maxPlayersAllowed)
        dealer = othergametwo.random_player()
        dealer.deal(othergametwo)
        firstplayer = othergametwo.start()
        self.assertEqual(6,len(firstplayer.hand),"Must deal 6 cards!")
        self.assertFalse(firstplayer.dealer,"First Player cannot be dealer!")


   
    
    def test_float_merchant_not_in_hand(self):
        Player1 = loot.Player("John")
        Player2 = loot.Player("Joe")
        shipatsea = loot.MerchantShip(6)
        testship = loot.MerchantShip(7)
        Player1.hand.append(testship)
        self.assertFalse(Player1.float_merchant(shipatsea),"Card must be in hand!")

    
    def test_real_float_merchant(self):
        Player1 = loot.Player("John")
        Player2 = loot.Player("Joe")
        shipatsea = loot.MerchantShip(6)
        testship = loot.MerchantShip(7)
        Player1.hand.append(shipatsea)
        self.assertTrue(Player1.float_merchant(shipatsea),"Card must be in hand!")

    def test_fake_float_merchant(self):
        otherother = loot.Game(loot.Deck.get_instance())
        maxPlayersAllowed = 5
        minPlayersAllowed = 2
        playerNames = ["Joy", "Nan", "Sat"] 
        otherother.create_players(playerNames,minPlayersAllowed,maxPlayersAllowed)
        firstplayer = otherother.random_player()
        fakemerchant = loot.PirateShip("green",3)
        self.assertFalse(firstplayer.float_merchant(fakemerchant),"Card must be a merchant!")

    def test_fake_pirate_not_a_pirate(self):
        fakepirate = loot.MerchantShip(5)
        fakemerchant = loot.MerchantShip(6)
        Player1 = loot.Player("John")
        Player2 = loot.Player("Joe")
        self.assertFalse(Player1.play_pirate(fakepirate,fakemerchant,Player2),"Pirate is not a pirate!")

    def test_pirate_not_in_hand(self):
        Player1 = loot.Player("John")
        Player2 = loot.Player("Joe")
        shipatsea = loot.MerchantShip(6)
        Player1.merchant_ships_at_sea.append(shipatsea)
        pirateforhand = loot.PirateShip("green",3)
        piratetotest = loot.PirateShip("gold",3)
        Player2.hand.append(pirateforhand)
        self.assertFalse(Player2.play_pirate(piratetotest,shipatsea,Player1),"pirate not in hand!")

    def test_merchant_ship_not_in_sea(self):
        Player1 = loot.Player("John")
        Player2 = loot.Player("Joe")
        shipatsea = loot.MerchantShip(6)
        pirateforhand = loot.PirateShip("green",3)
        Player2.hand.append(pirateforhand)
        self.assertFalse(Player2.play_pirate(pirateforhand,shipatsea,Player1),"merchant not at sea")
    

    def test_pirate_played_with_no_previous_color(self):
        Player1 = loot.Player("John")
        Player2 = loot.Player("Joe")
        shipatsea = loot.MerchantShip(6)
        Player1.merchant_ships_at_sea.append(shipatsea)
        pirateforhand = loot.PirateShip("green",3)
        Player2.hand.append(pirateforhand)
        self.assertTrue(Player2.play_pirate(pirateforhand,shipatsea,Player1),"Must play correct pirate card!")

    def test_pirate_played_with_previous_color(self):
        Player1 = loot.Player("John")
        Player2 = loot.Player("Joe")
        shipatsea = loot.MerchantShip(6)
        Player1.merchant_ships_at_sea.append(shipatsea)
        pirateforhand = loot.PirateShip("green",3)
        secondpirateforhand = loot.PirateShip("brown",3)
        Player2.hand.append(pirateforhand)
        Player2.play_pirate(pirateforhand,shipatsea,Player1)
        self.assertFalse(Player2.play_pirate(secondpirateforhand,shipatsea,Player1),"Must be same color when attacking again!")

    
    def test_captain_not_in_hand(self):
        Player1 = loot.Player("John")
        Player2 = loot.Player("Joe")     
        captaincard1 = loot.Captain("brown")
        testcard = loot.PirateShip("green",5)
        merchantotest = loot.MerchantShip(7)
        Player1.merchant_ships_at_sea.append(merchantotest)
        Player2.hand.append(testcard)
        self.assertFalse(Player2.play_captain(captaincard1,merchantotest,Player1),"Captain must be in hand")

    def test_captain_with_diff_color(self):
        Player1 = loot.Player("John")
        Player2 = loot.Player("Joe")
        shipatsea = loot.MerchantShip(6)
        Player1.merchant_ships_at_sea.append(shipatsea)
        pirateforhand = loot.PirateShip("green",3)
        captaincard = loot.Captain("brown")
        Player2.hand.append(pirateforhand)
        Player2.hand.append(captaincard)
        Player2.play_pirate(pirateforhand,shipatsea,Player1)
        self.assertFalse(Player2.play_captain(captaincard,shipatsea,Player1),"Captain card must be same color as previous attack!")

    def test_captain_card_real(self):
        Player1 = loot.Player("John")
        Player2 = loot.Player("Joe")
        shipatsea = loot.MerchantShip(6)
        Player1.merchant_ships_at_sea.append(shipatsea)
        pirateforhand = loot.PirateShip("green",3)
        captaincard = loot.Captain("green")
        Player2.hand.append(pirateforhand)
        Player2.hand.append(captaincard)
        Player2.play_pirate(pirateforhand,shipatsea,Player1)
        self.assertTrue(Player2.play_captain(captaincard,shipatsea,Player1))

    def test_admiral_not_in_hand(self):
        Player1 = loot.Player("John")
        Player2 = loot.Player("Joe")     
        admiral = loot.Admiral.get_instance()
        testcard = loot.PirateShip("green",5)
        testcard2 = loot.MerchantShip(5)
        merchantotest = loot.MerchantShip(7)
        Player1.hand.append(testcard2)
        Player1.merchant_ships_at_sea.append(merchantotest)
        Player2.hand.append(testcard)
        Player2.play_pirate(testcard,merchantotest,Player1)
        self.assertFalse(Player1.play_admiral(admiral,merchantotest),"Admiral must be in hand!")

    def test_admiral_not_defended(self):
        Player1 = loot.Player("John")
        Player2 = loot.Player("Joe")     
        admiral = loot.Admiral.get_instance()
        testcard = loot.PirateShip("green",5)
        testcard2 = loot.MerchantShip(5)
        merchantotest = loot.MerchantShip(7)
        Player1.hand.append(testcard2)
        Player1.hand.append(admiral)
        Player1.merchant_ships_at_sea.append(merchantotest)
        Player2.hand.append(testcard)
        self.assertFalse(Player1.play_admiral(admiral,merchantotest),"Admiral must be defending")

    def test_correct_admiral(self):
        Player1 = loot.Player("John")
        Player2 = loot.Player("Joe")     
        admiral = loot.Admiral.get_instance()
        testcard = loot.PirateShip("green",5)
        testcard2 = loot.MerchantShip(5)
        merchantotest = loot.MerchantShip(7)


        Player1.hand.append(testcard2)
        Player1.hand.append(admiral)
        Player1.merchant_ships_at_sea.append(merchantotest)
        Player2.hand.append(testcard)
        Player2.play_pirate(testcard,merchantotest,Player1)
        self.assertTrue(Player1.play_admiral(admiral,merchantotest))

    def choose_player_out_of_bounds(self):
        otherother = loot.Game(loot.Deck.get_instance())
        maxPlayersAllowed = 5
        minPlayersAllowed = 2
        playerNames = ["Joy", "Nan", "Sat"]
        otherother.create_players(playerNames,minPlayersAllowed,maxPlayersAllowed)
        self.assertIsNone(otherother.choose_player(4),"out of bounds!")

    def choose_player_in_bounds(self):
        otherother = loot.Game(loot.Deck.get_instance())
        player1 = loot.Player("John")
        player2 = loot.Player("Joe")
        player3 = loot.Player("Jake")   
        otherother.players.append(player1)
        otherother.players.append(player2)
        otherother.players.append(player3)
        self.assertEqual(player1,otherother.choose_player(1),"player must be the one selected")

    def test_if_merchant_not_attacked(self):
        otherother = loot.Game(loot.Deck.get_instance())
        Player1 = loot.Player("John")
        Player2 = loot.Player("Joe")     
        testcard = loot.PirateShip("green",5)
        testcard2 = loot.MerchantShip(5)
        merchantotest = loot.MerchantShip(7)
        Player1.hand.append(testcard2)
        Player1.float_merchant(testcard2)
        otherother.players.append(Player1)
        otherother.players.append(Player2)
        otherother.capture_merchant_ships()
        self.assertEqual(testcard2,Player1.merchant_ships_captured[0],"Merchant not attacked!")

    def test_start_picks_right_person_if_edge(self):
        otherother = loot.Game(loot.Deck.get_instance())
        Player1 = loot.Player("John")
        Player2 = loot.Player("Joe")   
        Player3 = loot.Player("John")
        Player1.dealer = True
        otherother.players.append(Player1)
        otherother.players.append(Player2)
        otherother.players.append(Player3)
        self.assertEqual(otherother.players[-1],otherother.start(),"Must wrap around!")

    def test_start_picks_if_in_middle(self):
        otherother = loot.Game(loot.Deck.get_instance())
        Player1 = loot.Player("John")
        Player2 = loot.Player("Joe")   
        Player3 = loot.Player("John")
        Player2.dealer = True
        otherother.players.append(Player1)
        otherother.players.append(Player2)
        otherother.players.append(Player3)
        self.assertEqual(otherother.players[0],otherother.start())

    def test_next_picks_right_person_if_normal(self):
        otherother = loot.Game(loot.Deck.get_instance())
        Player1 = loot.Player("John")
        Player2 = loot.Player("Joe")   
        Player3 = loot.Player("John")
        otherother.players.append(Player1)
        otherother.players.append(Player2)
        otherother.players.append(Player3)
        otherother.current_player =Player1
        self.assertEqual(otherother.players[1],otherother.next())

    def test_next_picks_right_person_if_edge(self):
        otherother = loot.Game(loot.Deck.get_instance())
        Player1 = loot.Player("John")
        Player2 = loot.Player("Joe")   
        Player3 = loot.Player("John")
        otherother.players.append(Player1)
        otherother.players.append(Player2)
        otherother.players.append(Player3)
        otherother.current_player =Player3
        self.assertEqual(otherother.players[0],otherother.next())

    def test_capture_merchant_ships_with_admiral_and_captain(self):
        otherother = loot.Game(loot.Deck.get_instance())
        Player1 = loot.Player("John")
        Player2 = loot.Player("Joe")     
        admiral = loot.Admiral.get_instance()
        testcard = loot.PirateShip("green",5)
        testcard2 = loot.MerchantShip(5)
        merchantotest = loot.MerchantShip(7)
        captaintotest = loot.Captain("green")
        Player1.hand.append(testcard2)
        Player1.hand.append(admiral)
        print(Player1.hand)
        Player1.merchant_ships_at_sea.append(merchantotest)
        print(Player1.merchant_ships_at_sea)
        Player2.hand.append(testcard)
        Player2.hand.append(captaintotest)
        print(Player2.hand)
        otherother.players.append(Player1)
        otherother.players.append(Player2)

        Player2.play_pirate(testcard,merchantotest,Player1)
        Player1.play_admiral(admiral,merchantotest)
        Player2.play_captain(captaintotest,merchantotest,Player1)
        otherother.capture_merchant_ships()
        self.assertEqual(merchantotest,Player2.merchant_ships_captured[0])


    def test_capture_merchant_ships_with_admiral(self):
        otherother = loot.Game(loot.Deck.get_instance())
        Player1 = loot.Player("John")
        Player2 = loot.Player("Joe")     
        admiral = loot.Admiral.get_instance()
        testcard = loot.PirateShip("green",5)
        testcard2 = loot.MerchantShip(5)
        merchantotest = loot.MerchantShip(7)

        Player1.hand.append(testcard2)
        Player1.hand.append(admiral)
        print(Player1.hand)
        Player1.merchant_ships_at_sea.append(merchantotest)
        print(Player1.merchant_ships_at_sea)
        Player2.hand.append(testcard)
        print(Player2.hand)
        otherother.players.append(Player1)
        otherother.players.append(Player2)

        Player2.play_pirate(testcard,merchantotest,Player1)
        Player1.play_admiral(admiral,merchantotest)
        otherother.capture_merchant_ships()
        self.assertEqual(merchantotest,Player1.merchant_ships_captured[0])

    def test_capture_merchant_ships_with_pirates_only_once(self):
        otherother = loot.Game(loot.Deck.get_instance())
        Player1 = loot.Player("John")
        Player2 = loot.Player("Joe") 
        Player3 = loot.Player("Tyler")    
        testcard = loot.PirateShip("green",5)
        testcard2 = loot.MerchantShip(5)
        merchantotest = loot.MerchantShip(7)
        testcard3 = loot.PirateShip("blue",6)
        Player1.hand.append(testcard2)
        Player3.hand.append(testcard3)
        print(Player1.hand)
        Player1.merchant_ships_at_sea.append(merchantotest)
        print(Player1.merchant_ships_at_sea)
        Player2.hand.append(testcard)
        print(Player2.hand)
        otherother.players.append(Player1)
        otherother.players.append(Player2)
        otherother.players.append(Player3)

        Player2.play_pirate(testcard,merchantotest,Player1)
        Player3.play_pirate(testcard3,merchantotest,Player1)
        otherother.capture_merchant_ships()
        self.assertEqual(merchantotest,Player3.merchant_ships_captured[0])

    def test_capture_merchant_ships_with_pirates_multiple(self):
        otherother = loot.Game(loot.Deck.get_instance())
        Player1 = loot.Player("John")
        Player2 = loot.Player("Joe") 
        Player3 = loot.Player("Tyler")    
        testcard = loot.PirateShip("green",5)
        testcard2 = loot.MerchantShip(5)
        merchantotest = loot.MerchantShip(7)
        testcard3 = loot.PirateShip("blue",6)
        testcard4 = loot.PirateShip("green",7)
        Player2.hand.append(testcard4)
        Player1.hand.append(testcard2)
        Player3.hand.append(testcard3)
        print(Player1.hand)
        Player1.merchant_ships_at_sea.append(merchantotest)
        print(Player1.merchant_ships_at_sea)
        Player2.hand.append(testcard)
        print(Player2.hand)
        otherother.players.append(Player1)
        otherother.players.append(Player2)
        otherother.players.append(Player3)

        Player2.play_pirate(testcard,merchantotest,Player1)
        Player3.play_pirate(testcard3,merchantotest,Player1)
        Player2.play_pirate(testcard4,merchantotest,Player1)
        otherother.capture_merchant_ships()
        self.assertEqual(merchantotest,Player2.merchant_ships_captured[0])
        
    def test_equal_value_pirate(self):
        otherother = loot.Game(loot.Deck.get_instance())
        Player1 = loot.Player("John")
        Player2 = loot.Player("Joe")
        Player3 = loot.Player("Tyler")
        shipatsea = loot.MerchantShip(6)
        Player1.merchant_ships_at_sea.append(shipatsea)
        pirateforhand = loot.PirateShip("green",3)
        secondpirateforhand = loot.PirateShip("brown",3)

        Player2.hand.append(pirateforhand)
        Player3.hand.append(secondpirateforhand)
        otherother.players.append(Player1)
        otherother.players.append(Player2)
        otherother.players.append(Player3)

        Player2.play_pirate(pirateforhand,shipatsea,Player1)
        Player3.play_pirate(secondpirateforhand,shipatsea,Player1)
        otherother.capture_merchant_ships()
        self.assertEqual(1,len(Player1.merchant_pirates),"Equal value so no one wins the ship!")

    def test_winners(self):

        otherother = loot.Game(loot.Deck.get_instance())
        Player1 = loot.Player("John")
        Player2 = loot.Player("Joe") 
        Player3 = loot.Player("Tyler")    
        testcard = loot.PirateShip("green",5)
        testcard2 = loot.MerchantShip(5)
        merchantotest = loot.MerchantShip(7)
        testcard3 = loot.PirateShip("blue",6)
        testcard4 = loot.PirateShip("green",7)
        Player2.hand.append(testcard4)
        Player1.hand.append(testcard2)
        Player3.hand.append(testcard3)
        Player1.merchant_ships_at_sea.append(merchantotest)
        Player2.hand.append(testcard)
        otherother.players.append(Player1)
        otherother.players.append(Player2)
        otherother.players.append(Player3)

        Player2.play_pirate(testcard,merchantotest,Player1)
        Player3.play_pirate(testcard3,merchantotest,Player1)
        Player2.play_pirate(testcard4,merchantotest,Player1)
        otherother.capture_merchant_ships()
        listofwinner=[[Player1,0],[Player2,7],[Player3,0]]
        self.assertEqual(listofwinner,otherother.show_winner())
