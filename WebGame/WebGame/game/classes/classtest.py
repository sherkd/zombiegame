from django.test import TestCase
from player import *

class ClassTest(TestCase):  
    
    def testPlayer(self):
        #username, health, attack, defence, cooldowns, money, items, level, experience
        player = Player("P", 100, 10, ["cooldown1", "cooldown2"], 100, "items", 10, 20)
        print(player.getUserName())
        self.assertAlmostEquals("P", player.getUserName())
        self.assertAlmostEquals(100, player.getHealth())
        self.assertAlmostEquals(10, player.getAttackDamage())
        self.assertAlmostEquals( ["cooldown1", "cooldown2"], ["cooldown1", "cooldown2"])
        self.assertAlmostEquals(100, player.getMoney()) 
        self.assertAlmostEquals("items", player.getItems())
        self.assertAlmostEquals(10, player.getLevel())
        self.assertAlmostEquals(20, player.getExperience())
     



