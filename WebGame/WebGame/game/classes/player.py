class Player(object):

    def __init__(self, username, health, attack, defence, cooldowns, money, items, level, experience):
        self.username = username
        self.health = health
        self.attack = attack
        self.defence = defence
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
        return self.attackDamage

    def setAttackDamage(self, damage):
        self.attackDamage = damage
        
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
        if self.experience >= getRequiredExp():
            self.increaseLevel()
            self.setExperience(self.getRequiredExp() - self.experience)
            return True
        return False

        


