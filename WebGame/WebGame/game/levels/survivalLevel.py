from django.test import TestCase
from game.classes.player import Player
from game.classes.player import Enemy

class Survival(object):
    """description of bank."""

    def __init__(self, player, wavecounter):
        self.player = player
        self.wavecounter = wavecounter
        self.enemy = enemy

    def getPlayer(self):
        return self.player

    def getWaveCounter(self):
        return self.wavecounter

    def getEnemy(self):
        return self.enemy

    def startWaves(self):
        self.wavecounter = 1
        damage = 10
        while startWaves():
            if self.player.getHealth > 0 and self.player.getHealth - damage != 0:
                self.wavecounter = self.wavecounter + 1
                damage = damage + 10
            else:
                break

    def startSurvival(self):
        self.player.addCooldown("Survival")
        while len(self.player.getCooldowns()) == 1:
            if self.player.health <= 0:
                self.player.removeCooldown("Survival")
            else:
                startWaves()
                break


class TestSurvival(TestCase):

    def testSurvival(self):
        #Player(username, health, attack, cooldowns, money, items, weapons, level, experience, balance)
        surv = Survival(Player("name", 100, 10, ["cl"], 50, ["items"], 1, 20, 0, 0))
        #Enemy(name, level, health, weapon, rewardItem)
        en = Enemy("Henk", 3, 100, Weapon("Henk weapon", 5, 100), None)
