import random
from django.test import TestCase
import time, threading
from game.classes.player import Player
from game.classes.weapon import Weapon

class SearchLevel(object):
    
    def __init__(self, player, seconds):
        self.player = player
        self.seconds = seconds
        self.message = ""

    def startScouting(self):
        self.player.addCooldown("scouting")
        self.startRunnable()
        pass

    def getPlayer(self):
        return self.player

    def getSeconds(self):
        return self.seconds

    def getMessage(self):
        return self.message 

    def startRunnable(self):
        self.seconds -= 1  
        print(self.seconds)     
        if self.seconds == 0:
            self.player.removeCooldown("scouting")
            randomNum = random.randint(0, 100)
            if randomNum < 30:
                self.player.addWeapon(Weapon.getRandomWeapon(self.player.getLevel()))    
                self.message = "You found a weapon."            
            elif randomNum < 50:
                healthLost = random.randint(3, 15)
                self.player.setHealth(self.player.getHealth() - healthLost)
                self.message = "You got attacked and you lost " + healthLost + " health."
            elif randomNum < 80:
                self.message = "You entered a battle!"
                """ ToDo: start battle """
            elif randomNum < 85:
                self.player.setExperience(self.player.getExperience() + 20 * self.player.getLevel());
                self.message = "You got experience."
            elif randomNum < 95:
                self.player.setMoney(self.player.getMoney() + 20)
                self.message = "You found money."
            else:
                self.message = "You found nothing at all."
        else:
             threading.Timer(1, self.startRunnable).start()   
             
    
             
class TestSearch(TestCase):

    def testSearch(self):
        search = SearchLevel(Player("name", 100, 10, ["cl"], 50, ["items"], 1, 20, 0, 0), 2)
        self.assertEquals("name", search.getPlayer().getUserName())
        search.startScouting()
        self.assertEquals(["cl", "scouting"], search.getPlayer().getCooldowns())
        self.assertEquals(1, search.getSeconds())