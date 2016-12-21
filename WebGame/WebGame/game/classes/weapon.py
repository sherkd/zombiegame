from django.test import TestCase
import random

class Weapon(object):

    def __init__(self, name, damage, value, description):
        self.name = name
        self.damage = damage
        self.value = value
        self.description = description

    def __init__(self, name, damage, value):
        self.name = name
        self.damage = damage
        self.value = value    
        self.description = ""   

    def getName(self):
        return self.name

    def getDamage(self):
        return self.damage

    def getValue(self):
        return self.value

    def getDescription(self):       
        return self.description

    def getRandomWeapon(damage):
        randomNum = random.randint(0, 4)
        if (level == 0):
            return Weapon("Sniper", damage, random.randint(70, 100))
        elif (level == 1):
             return Weapon("SMG", damage, random.randint(70, 100))
        elif (level == 2):
             return Weapon("Assault rifle", damage, random.randint(70, 100))
        elif (level == 3):
            return Weapon("Knife", damage/2, random.randint(20, 60))
        elif (level == 4):
            return Weapon("RPG", damage * 1.2, random.randint(90, 100))


class TestWeapon(TestCase):

    def testWeapon(self):
        wep = Weapon("Wep", 10, 100)
        self.assertEquals("Wep", wep.getName())
        self.assertEquals(10, wep.getDamage())
        self.assertEquals(100, wep.getValue())
        self.assertEquals("", wep.getDescription())


    