import random

class Weapon:   

    def __init__(self, name, damage, value, level, cl):
        self.name = name
        self.damage = damage
        self.value = value    
        self.description = ""   
        self.level = level
        self.cl = cl

    def getName(self):
        return self.name

    def getDamage(self):
        return self.damage

    def getValue(self):
        return self.value

    def getDescription(self):       
        return self.description

    def setDescription(self, desc):
        self.description = desc
        
    def getLevel(self):
        return self.level

    def setLevel(self, level):
        self.level = level

    def getClass(self):
        return self.cl

    def getRandomWeapon(damage):
        randomNum = random.randint(0, 4)
        if (randomNum == 0):
            return Weapon("Sniper", damage, random.randint(70, 100))
        elif (randomNum == 1):
             return Weapon("SMG", damage, random.randint(70, 100))
        elif (randomNum == 2):
             return Weapon("Assault rifle", damage, random.randint(70, 100))
        elif (randomNum == 3):
            return Weapon("Knife", damage/2, random.randint(20, 60))
        elif (randomNum == 4):
            return Weapon("RPG", damage * 1.2, random.randint(90, 100))





    