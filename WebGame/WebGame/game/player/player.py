class Player():  
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

    def getUserName():
        return username

    def getHealth():
        return health

    def setHealth(health):
        self.health = health

    def getAttackDamage():
        return attackDamage

    def setAttackDamage(damage):
        self.attackDamage = damage
        
    def getCooldowns():
        return cooldowns

    def removeCooldown(cooldown):
        del self.cooldown[cooldown]

    def getMoney():
        return money

    def setMoney(money):
        self.money = money

    def getItems():
        return items

    def removeItem(item):
        self.items.remove(item)

    def addItem(item):
        self.items.append(item)     

    def getLevel():
        return self.level;

    def increaseLevel():
        self.level += 1

    def getExperience():
        return self.experience

    def setExperience(exp):
        self.experience = exp

    def getRequiredExp():
        return self.level * 140

    def checkLevelUp():
        if self.experience >= getRequiredExp:
            increaseLevel()
            setExperience(getRequiredExp - self.experience)
            return True
        return False

        


