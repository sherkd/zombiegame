from django.test import TestCase

class shoplevel(object):

    def __init__(self, weapons, prices):
        self.weaponnames = weapons
        self.weaponprices = prices

    def addweapon(self, weaponname, price):
        self.weaponnames.append(weaponname)
        self.weaponprices.append(price)

    def getweaponnames(self):
        return self.weaponnames

    def getweaponprice(self):
        return self.weaponprices

    def getweaponnameandprice(self):
        return self.weaponnames[0] + str(self.weaponprices[0])

            
            
        



class TestShop(TestCase):

    def testShop(self):
        shop = shoplevel(["lasergun"], [100])
        self.assertEquals(["lasergun"], shop.getweaponnames())
        self.assertEquals([100], shop.getweaponprice())
        shop.addweapon("machinegun", 200)
        self.assertEquals(["lasergun", "machinegun"], shop.getweaponnames())
        self.assertEquals([100, 200], shop.getweaponprice())
        shop.addweapon("balistic knife", 150)
        self.assertEquals("lasergun"+"100", shop.getweaponnameandprice())
        
