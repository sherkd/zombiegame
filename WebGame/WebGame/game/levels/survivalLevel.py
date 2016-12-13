from django.test import TestCase
from game.classes.player import Player
from game.classes.player import Enemy

class Survival(object):
    """description of bank."""

    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def getPlayer(self):
        return self.player

    def getEnemy(self):
        return self.enemy



class TestSurvival(TestCase):

    def testSurvival(self):
        #Player(username, health, attack, cooldowns, money, items, weapons, level, experience, balance)
        bank = Survival(Player("name", 100, 10, ["cl"], 50, ["items"], 1, 20, 0, 0))
        #Enemy(name, level, health, weapon, rewardItem)
        en = Enemy("Henk", 3, 100, Weapon("Henk weapon", 5, 100), None)
