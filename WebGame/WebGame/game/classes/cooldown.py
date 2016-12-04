from django.test import TestCase

class Cooldown(object):

    def __init__(self, cooldownType, seconds):
        self.cooldownType = cooldownType
        self.seconds = seconds

    def getCooldownType(self):
        return self.cooldownType

    def getSeconds(self):
        return self.seconds

    def lowerSeconds(self):
        self.seconds -= 1

    def setSeconds(self, sec):
        self.seconds = sec


class TestCooldown(TestCase):
    
    def testCooldown(self):
        cl = Cooldown("search", 12)
        self.assertEquals("search", cl.getCooldownType())
        self.assertEquals(12, cl.getSeconds())
        cl.lowerSeconds()
        self.assertEquals(11, cl.getSeconds())
        cl.setSeconds(12) 
        self.assertEquals(12, cl.getSeconds())





  


