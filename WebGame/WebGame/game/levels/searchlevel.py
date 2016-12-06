import random
from django.test import TestCase
import time, threading

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
        self.search = SearchLevel(Player("name", 100, 10, ["cl"], 50, ["items"], 1, 20), 10)
        return super().__init__(methodName)
    
    def testSearch(self):
        self.assertEquals("name", self.search.getPlayer().getUserName())
        self.search.startScouting()
        self.assertEquals(["cl", "scouting"], self.search.getPlayer().getCooldowns())
        self.assertEquals(9, self.search.getSeconds())

#Remove after testing, can't seem to fix the import.
class Player(object):

    def __init__(self, username, health, attack, cooldowns, money, items, level, experience):
        self.username = username
        self.health = health
        self.attack = attack
        self.cooldowns = cooldowns
        self.money = money
        self.items = items
        self.level = level
        self.experience = experience

    def getUserName(self):
        return self.username

    def getHealth(self):
        return self.health

    def setHealth(self, health):
        self.health = health

    def getAttackDamage(self):
        return self.attack

    def setAttackDamage(self, damage):
        self.attack = damage
       
    def getCooldowns(self):
        return self.cooldowns

    def removeCooldown(self, cooldown):
        self.cooldowns.remove(cooldown)

    def addCooldown(self, cooldown):
        self.cooldowns.append(cooldown)

    def getMoney(self):
        return self.money

    def setMoney(self, money):
        self.money = money

    def getItems(self):
        return self.items

    def removeItem(self, item):
        self.items.remove(item)

    def addItem(self, item):
        self.items.append(item)     

    def getLevel(self):
        return self.level;

    def increaseLevel(self):
        self.level += 1

    def getExperience(self):
        return self.experience

    def setExperience(self, exp):
        self.experience = exp

    def getRequiredExp(self):
        return self.level * 140

    def checkLevelUp(self):
        if self.experience >= self.getRequiredExp():
            self.increaseLevel()
            self.setExperience(self.getRequiredExp() - self.experience)
            return True
        return False







