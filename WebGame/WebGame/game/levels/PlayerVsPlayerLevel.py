from game.classes.player import Player


class PlayerVsPlayerLevel(object):
    """description of class"""
    def __init__(self, player, player2):
        self.player = player
        self.player2 = player2


    def startBattle(self):
        self.player.addCooldown("Battle")
        while len(self.player.getCooldowns()) == 1:
            if self.player.health <= 0 or self.player2.health <= 0:
                self.player.removeCooldown("Battle")
        pass



