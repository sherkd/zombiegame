from game.classes.player import Player

class Groupfight(object):
    """description of class"""
    def __init__(self, player, player2, player3, player4, player5, player6):
        self.player = player
        self.player = player2
        self.player = player3
        self.player = player4
        self.player = player5
        self.player = player6
        self.team1 = [player, player2, player3]
        self.team2 = [player4, player5, player6]


    def startBattle(self):
        self.player.addCooldown("groupfight")
        self.player2.addCooldown("groupfight")
        self.player3.addCooldown("groupfight")
        self.player4.addCooldown("groupfight")
        self.player5.addCooldown("groupfight")
        self.player6.addCooldown("groupfight")
        while len(self.player.getCooldowns()) == 1:
            if self.player.health <= 0 or self.player2.health <= 0 or self.player3.health:
                self.player.removeCooldown("groupfight")
            elif self.player4.health <= 0 or self.player5.health <= 0 or self.player6.health:
                self.player3.removeCooldown("groupfight")
        pass 
     