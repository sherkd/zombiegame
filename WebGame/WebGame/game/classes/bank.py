from django.test import TestCase
import player

class Bank(object):
    """description of bank."""

    def __init__(self, player):
        self.player = player

    def getPlayer(self):
        return self.player

    def withdrawMoney(self, input):
        if self.player.getBalance() > input:
            self.player.setBalance(self.player.getBalance() - input)
            self.player.setMoney(self.player.getMoney() + input)
        else:
            print("Not enough balance")

    def depositMoney(self, input):
        if self.player.getMoney() >= input:
            output = (self.player.getBalance() + input)
            self.player.setBalance(output)
            self.player.setMoney(self.player.getMoney() - input)
        else:
            print("Not enough money")

class TestBank(TestCase):

    def testBank(self):
        bank = Bank(Player("name", 100, 10, ["cl"], 50, ["items"], 1, 20, 0))      
        
        self.assertEquals(0, bank.player.getBalance())
        bank.depositMoney(10)
        self.assertEquals(40, bank.player.getMoney())

class Player(object):

    def __init__(self, username, health, attack, cooldowns, money, items, level, experience, balance):
        self.username = username
        self.health = health
        self.attack = attack
        self.cooldowns = cooldowns
        self.money = money
        self.items = items
        self.level = level
        self.experience = experience
        self.balance = balance

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

    def getBalance(self):
        return self.balance

    def setBalance(self, balance):
        self.balance = balance

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