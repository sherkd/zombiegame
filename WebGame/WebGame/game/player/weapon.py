class Weapon(object):

    def __init__(self, name, damage, value):
        self.name = name
        self.damage = damage
        self.value = value

    def getName(self):
        return self.name

    def getDamage(self):
        return self.damage

    def getValue(self):
        return self.value
    