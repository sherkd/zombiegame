from game.classes.player import Player
from django.test import TestCase
from game.classes.enemy import Enemy
from game.classes.weapon import Weapon
import time, threading


class Tournament(object):
    """description of class"""
    def __init__(self, player, enemy, counter):
        self.player = player
        self.enemy = enemy
        self.counter = counter

    def attack(self):
        self.enemy.setHealth(self.enemy.getHealth() - self.player.attack)
        self.player.setHealth(self.player.getHealth() - self.enemy.weapon.damage)

    def fight1(self):
        self.enemy = Enemy("drakenslachter010", 13, 240, Weapon("waterpistool", 20, 300), None)

    def startTournament(self):
        self.player.addCooldown("Tournament")
        if len(self.player.getCooldowns()) == 1:
            self.player.addCooldown("Tournament")
            if self.player.getHealth() <= 0:
               self.player.removeCooldown("Tournament")
            elif self.enemy.getHealth() <= 0:
               self.counter -= 1
               self.player.removeCooldown("Tournament")
               if self.counter == 3:
                   self.enemy = Enemy("swaggerboy111", 7, 180, Weapon("minigun", 30, 400), None)
               elif self.counter == 2:
                   self.enemy = Enemy("drakenslachter010", 13, 240, Weapon("waterpistool", 20, 300), None)
                   self.player.removeCooldown("Tournament")
                   threading.Timer(1, self.startTournament()).start() 
               elif self.counter == 1:
                   self.enemy = Enemy("oreobakker12", 5, 160, Weapon("botermes", 10, 70), None)
               else:  
                   # give reward
                   self.player.removeCooldown("Tournament")
                   pass  

                   
            else:
                self.attack()
                self.player.removeCooldown("Tournament")
                self.player.removeCooldown("Tournament")
                threading.Timer(1, self.startTournament()).start() 
                

