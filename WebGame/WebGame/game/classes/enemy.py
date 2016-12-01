class Enemy(object):
    
    def __init__(self, name, level, health, weapon):
        self.name = name
        self.level = level
        self.health = health
        self.weapon = weapon     

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

    def getWeapon(self):
        return self.weapon

    def getRewardMoney(self):
        return self.level * 2.2

    def getRewardExp(self):
        return self.level * 4.3

    def getRewardItem(self):
        return self.rewardItem

