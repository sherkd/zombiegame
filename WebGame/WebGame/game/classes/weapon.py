from django.test import TestCase

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

class TestWeapon(TestCase):

    def testWeapon(self):
        wep = Weapon("Wep", 10, 100)
        self.assertEquals("Wep", wep.getName())
        self.assertEquals(10, wep.getDamage())
        self.assertEquals(100, wep.getValue())
        self.assertEquals("", wep.getDescription())


    