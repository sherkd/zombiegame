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
                

class TestTournament(TestCase):
    
    def testTournament(self):
        enemy1 = Enemy("drakenslachter010", 13, 240, Weapon("waterpistool", 20, 300), None)
        enemy2 = Enemy("oreobakker12", 5, 160, Weapon("botermes", 10, 70), None)
        enemy3 = Enemy("swaggerboy111", 7, 180, Weapon("minigun", 30, 400), None)
        player1 = Player("bamboeknul69", 300, 70, [], 100, ["legendarische steekmes"], 10, 9000, 0, 0)

        tournament = Tournament(player1, enemy3, 3)
        self.assertEquals(3, tournament.counter)   #ivm recursieve functie is vanaf hier ***
        tournament.startTournament()
       
        self.assertEquals("swaggerboy111", tournament.enemy.getName())
        self.assertEquals(270, tournament.player.getHealth())
        self.assertEquals(tournament.enemy.health, 110)
       
        tournament.attack()
       
        self.assertEquals(tournament.enemy.health, 40)
        self.assertEquals(tournament.player.getHealth(), 240) 
        self.assertEquals(player1.getCooldowns(), ["Tournament", "Tournament", "Tournament"]) 
        self.assertEquals(tournament.counter, 3) 
        tournament.attack()  
        self.assertEquals(tournament.enemy.health, -30)   #t/m hier voor counter == 3

       # self.assertEquals(3, tournament.counter)   #ivm recursieve functie is vanaf hier ***
       # tournament.startTournament()
       #
       # self.assertEquals("drakenslachter010", tournament.enemy.getName())
       # self.assertEquals(210, tournament.player.getHealth())
       # self.assertEquals(tournament.enemy.health, 240)
       #
       # tournament.attack()
       #
       # self.assertEquals(tournament.enemy.health, 170)
       # self.assertEquals(tournament.player.getHealth(), 190) # laatste attack van enemy1 voor zijn dood + eerste attack van enemy2 = 20+30
       # self.assertEquals(player1.getCooldowns(), ["Tournament"]) 
       # self.assertEquals(tournament.counter, 2) 
       # tournament.attack()  
       # tournament.attack()
       # tournament.attack()
       # self.assertEquals(tournament.enemy.health, -40)  
       # self.assertEquals(tournament.player.health, 130) #t/m hier voor counter == 2 
        

                     
