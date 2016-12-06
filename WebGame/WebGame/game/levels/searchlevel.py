import random
from django.test import TestCase
import time, threading
from game.classes.player import Player

class SearchLevel(object):
    
    def __init__(self, player, seconds):
        self.player = player
        self.seconds = seconds

    def startScouting(self):
        self.player.addCooldown("scouting")
        self.startRunnable()
        pass

    def getPlayer(self):
        return self.player

    def getSeconds(self):
        return self.seconds

    def startRunnable(self):
        self.seconds -= 1  
        print(self.seconds)     
        if self.seconds == 0:
            self.player.removeCooldown("scouting")
            randomNum = random.randint(0, 100)
            if randomNum < 30:
                #player found weapon
                pass
            elif randomNum < 50:
                #player got attacked
                pass
            elif randomNum < 80:
                #enemy encounter
                pass
            elif randomNum < 85:
                #player got experience
                pass
            elif randomNum < 95:
                #player found money
                pass
            else:
                #player found nothing
                pass
        else:
             threading.Timer(1, self.startRunnable).start()     
             
class TestSearch(TestCase):

    def __init__(self, methodName = 'runTest'):
        self.search = SearchLevel(Player("name", 100, 10, ["cl"], 50, ["items"], 1, 20, 0), 10)
        return super().__init__(methodName)
    
    def testSearch(self):
        self.assertEquals("name", self.search.getPlayer().getUserName())
        self.search.startScouting()
        self.assertEquals(["cl", "scouting"], self.search.getPlayer().getCooldowns())
        self.assertEquals(9, self.search.getSeconds())