from game.classes.player import Player

class tournament(object):
    """description of class"""
    def __init__(self, player, enemy, counter):
        self.player = player
        self.enemy = enemy
        self.counter = counter

    def getPlayer(self):
        return self.player

    def getEnemy(self):
        return self.enemy

    def getCounter(self):
        return self.counter

    def startTournament(self):
        self.player.addCooldown("Tournament")
        while len(self.player.getCooldowns()) == 1:
            if self.player.health <= 0:
                self.player.removeCooldown("Tournament")
            elif self.enemy.health <= 0:
                self.player.removeCooldown("Tournament")
                self.counter -= 1
                if self.counter == 0:
                    pass
                else:    
                    startTournament(self)

                


                     
