from game.classes.player import Player

class tournament(object):
    """description of class"""
    def __init__(self, player, enemy, counter):
        self.player = player
        self.enemy = enemy
        self.counter = counter

    def flee(self):
        self.player.removeCooldown("Tournament")

    def Attack(self):
        if self.player.addCooldown("Tournament"):
            self.enemy.health - (self.player.attack + self.player.currentweapon.getDamage())

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

                


                     
