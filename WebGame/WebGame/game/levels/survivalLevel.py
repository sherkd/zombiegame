from django.test import TestCase
from game.classes.player import Player
from game.classes.enemy import Enemy
import random

class Survival(object):
    """description of bank."""

    def __init__(self, player, wavecounter, damage):
        self.player = player
        self.wavecounter = wavecounter
        self.damage = damage

    def getPlayer(self):
        return self.player

    def getWaveCounter(self):
        return self.wavecounter

    def setWaveCounter(self, wavecounter):
        self.wavecounter = wavecounter

    def getDamage(self):
        return self.damage

    def setDamage(self, damage):
        self.damage = damage

    def getEnemy(self):
        return self.enemy

    def startOneWave(self):
        if self.player.health > 0:
            self.player.setHealth(self.player.getHealth() - self.damage)
            self.setWaveCounter(self.getWaveCounter() + 1)
            self.setDamage(self.getDamage() + 10)
            #randint(1,10)
        else:
            print("You are dead")

    def startWaves(self):
        damage = 10
        while startWaves():
            if self.player.health > 0 and self.player.health > damage:
                self.player.setHealth(self.player.getHealth() - damage)
                self.setWaveCounter(self.getWaveCounter() + 1)
                damage = damage + 10     
            else:
                break

    def startSurvival(self):
        self.player.addCooldown("Survival")
        while len(self.player.getCooldowns()) == 1:
            if self.player.health <= 0:
                self.player.removeCooldown("Survival")
            elif self.player.health > 0 and self.player.health > damage:
                self.player.setHealth(self.player.getHealth() - damage)
                self.setWaveCounter(self.getWaveCounter() + 1)
                damage = damage + 10
                #startWaves()
                

class TestSurvival(TestCase):

    def testSurvival(self):
        #Player(username, health, attack, cooldowns, money, items, weapons, level, experience, balance)
        surv = Survival(Player("name", 100, 10, ["cl"], 50, ["items"], 1, 20, 0, 0), 1, 10)

        #Enemy(name, level, health, weapon, rewardItem)
        #en = Enemy("Henk", 3, 100, Weapon("Henk weapon", 5, 100), None)

        self.assertEquals(100, surv.player.getHealth())

        self.assertEquals(1, surv.getWaveCounter())

        surv.startOneWave()

        self.assertEquals(2, surv.getWaveCounter())
        self.assertEquals(90, surv.player.getHealth())

        surv.startOneWave()

        self.assertEquals(3, surv.getWaveCounter())
        self.assertEquals(70, surv.player.getHealth())

        surv.startOneWave()

        self.assertEquals(4, surv.getWaveCounter())
        self.assertEquals(40, surv.player.getHealth())

        surv.startOneWave()

        self.assertEquals(5, surv.getWaveCounter())
        self.assertEquals(0, surv.player.getHealth())

