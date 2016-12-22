from django.test import TestCase
from game.classes.weapon import Weapon

class Enemy(object):
    
    def __init__(self, name, level, health, weapon, rewardItem):
        self.name = name
        self.level = level
        self.health = health
        self.weapon = weapon    
        self.rewardItem = rewardItem
        
    def getName(self):
        return self.name

    def getLevel(self):
        return self.level

    def getHealth(self):
        return self.health

    def setHealth(self, health):
        self.health = health

    def getWeapon(self):
        return self.weapon

    def getRewardMoney(self):
        return self.level * 2.2

    def getRewardExp(self):
        return self.level * 4.3

    def getRewardItem(self):
        return self.rewardItem

    def getRandomEnemy(player):
        """TODO: generate a random enemy depending on your level."""
        pass

class TestEnemy(TestCase):

    def testEnemy(self):
        en = Enemy("Henk", 3, 100, Weapon("Henk weapon", 5, 100), None)
        self.assertEquals("Henk", en.getName())
        self.assertEquals(3, en.getLevel())
        self.assertEquals(100, en.getHealth())
        self.assertEquals(None, en.getRewardItem())
        self.assertEquals(en.getLevel() * 2.2, en.getRewardMoney())
        self.assertEquals(en.getLevel() * 4.3, en.getRewardExp())

       

