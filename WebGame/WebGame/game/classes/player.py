
"""
database = Postgres()
print(database.getConnection())
database.insertAccount()
database.insertTestPlayer()
print(database.getAccount())
print(database.getTestPlayer())
"""

class Player(object):

    def __init__(self, id, username, health, attack, cooldowns, money, items, weapons, level, experience, balance, equipedWeapon):
        self.id = id
        self.username = username
        self.health = health
        self.attack = attack
        self.cooldowns = cooldowns
        self.money = money
        self.items = items
        self.weapons = weapons; 
        self.level = level
        self.experience = experience
        self.balance = balance
        self.equipedWeapon = equipedWeapon

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

    def getWeapons(self):
        return self.weapons

    def removeWeapon(self, weapon):
        for wep in self.getWeapons():
            if wep.getName() == weapon.getName() and wep.getValue() == weapon.getValue() and wep.getDamage() == weapon.getDamage():
                self.weapons.remove(wep)
                break

    def addWeapon(self, weapon):
        self.weapons.append(weapon)

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

    def getEquipedWeapon(self):
        return self.equipedWeapon

    def setEquipedWeapon(self, weapon):
        self.addWeapon(self.getEquipedWeapon())
        self.equipedWeapon = weapon
        self.removeWeapon(weapon)

    def checkLevelUp(self):
        if self.experience >= self.getRequiredExp():
            self.increaseLevel()
            self.setExperience(self.getRequiredExp() - self.experience)
            return True
        return False

    
