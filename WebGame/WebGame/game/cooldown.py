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

  


