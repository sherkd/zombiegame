import random

class SearchLevel(object):
    
    def __init__(self, player, seconds):
        self.player = player
        self.seconds = seconds

    def startScouting(self):
        player.addCooldown("scouting")
        self.startRunnable()
        pass

    def startRunnable(self):
        self.seconds -= 1       
        if seconds == 0:
            player.removeCooldown("scouting")
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
            pass
            #TODO: start a runnable






