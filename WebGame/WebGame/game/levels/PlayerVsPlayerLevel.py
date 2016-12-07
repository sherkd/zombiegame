class PlayerVsPlayerLevel(object):
    """description of class"""
    def __init__(self, player, player2):
        self.player = player
        self.player2 = player2

    def getPlayer(self):
        return self.player

    def startBattle(self):
        self.player.addCooldown("Battle")
        self.player2.addCooldown("Battle")
        pass



