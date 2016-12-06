from django.test import TestCase
import player

class Bank(object):
    """description of bank"""

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

    def depositMoney(self, input, money, balance):
        if self.player.getMoney() >= input:
            self.player.setBalance(self.player.getBalance() + input)
            self.player.setMoney(self.player.getMoney() - input)
        else:
            print("Not enough money")

class BankLevel(object):

    def __init__(self, player, money, balance):
        self.player = player
        self.money = money
        self.balance = balance

    def getPlayer(self):
        return self.player

class TestBank(TestCase):

    def testBank(self):
        search = Bank(Player("name", 100, 10, ["cl"], 50, ["items"], 1, 20), 10)
        self.assertEquals("name", search.getPlayer().getUserName())
        search.startScouting()
        self.assertEquals(["cl", "scouting"], search.getPlayer().getCooldowns())
        self.assertEquals(9, search.getSeconds())