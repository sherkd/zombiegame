from django.test import TestCase

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


    
class ClassTest(TestCase):  
    
    def testPlayer(self):      
        player = Player("P", 100, 10, ["cooldown1", "cooldown2"], 100, ["item1", "item2"], 10, 20, 0)
        self.assertEquals("P", player.getUserName())

        self.assertEquals(100, player.getHealth())
        player.setHealth(50)
        self.assertEquals(50, player.getHealth())       

        self.assertEquals(10, player.getAttackDamage())
        player.setAttackDamage(12)
        self.assertEquals(12, player.getAttackDamage())

        self.assertEquals(["cooldown1", "cooldown2"], player.getCooldowns())
        player.addCooldown("cooldown3")
        self.assertEquals(["cooldown1", "cooldown2", "cooldown3"],  player.getCooldowns())
        player.removeCooldown("cooldown2")
        self.assertEquals(["cooldown1", "cooldown3"],  player.getCooldowns())

        self.assertEquals(100, player.getMoney()) 
        player.setMoney(50)
        self.assertEquals(50, player.getMoney()) 

        self.assertEquals(["item1", "item2"], player.getItems())
        player.addItem("item3")
        self.assertEquals(["item1", "item2", "item3"], player.getItems())
        player.removeItem("item3") 
        self.assertEquals(["item1", "item2"], player.getItems())

        self.assertEquals(10, player.getLevel())
        player.increaseLevel()
        self.assertEquals(11, player.getLevel())

        self.assertEquals(20, player.getExperience())
        player.setExperience(player.getRequiredExp() + 10)
        self.assertEquals(player.getRequiredExp() + 10, player.getExperience())
        self.assertEquals(True, player.checkLevelUp())
        self.assertEquals(12, player.getLevel())
        self.assertEquals(130, player.getExperience())

        self.assertEquals(0, player.getBalance())
        player.setBalance(10)
        self.assertEquals(10, player.getBalance())

     

        


