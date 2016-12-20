from game.classes.player import Player
import random
import time, threading

class heist(object):
    """description of class"""
    def __init__(self, player1, player2, player3, player4, seconds):
        self.player1 = player1;
        self.player2 = player2;
        self.player3 = player3;
        self.player4 = player4;
        self.seconds = seconds;

    def startheist(self):
        self.player1.addCooldown("Heist")
        self.player2.addCooldown("Heist")
        self.player3.addCooldown("Heist")
        self.player4.addCooldown("Heist")
        while self.seconds > 0:
            self.seconds -= 1;
            if self.seconds == 0:
                self.player1.removeCooldown("Heist")
                self.player2.removeCooldown("Heist")
                self.player3.removeCooldown("Heist")
                self.player4.removeCooldown("Heist")
                randomNum = random.randint(0, 100)
                if randomNum < 30:
                    #player found weapon
                    pass
                elif randomNum < 50:
                    #player got attacked        
                    pass
                elif randomNum < 80:
                    #enemy encounter
                    pass
                elif randomNum < 85:
                    #player got experience
                    pass
                elif randomNum < 95:
                    #player found money
                    pass
                else:
                    #player found nothing
                    pass
            else:
                 threading.Timer(1, self.startheist).start()     


        


