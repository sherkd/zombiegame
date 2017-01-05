
class Bank(object):
    """description of bank."""

    def __init__(self, player):
        self.player = player

    def getPlayer(self):
        return self.player

    def withdrawMoney(self, input):
        if self.player.getBalance() > input:
            self.player.setBalance(self.player.getBalance() - input)
            self.player.setMoney(self.player.getMoney() + input)
        else:
            print("Not enough balance")

    def depositMoney(self, input):
        if self.player.getMoney() >= input:
            output = (self.player.getBalance() + input)
            self.player.setBalance(output)
            self.player.setMoney(self.player.getMoney() - input)
        else:
            print("Not enough money")

