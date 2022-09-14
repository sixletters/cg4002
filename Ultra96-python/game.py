import threading
from player import player

class game:
    def __init(self, numberOfPlayers = 1):
        self.numOfPlayers = numberOfPlayers
        self.playerMap = {}
        for i in range(1,numberOfPlayers,1):
            self.playerMap[i] = player()
        self.playerTurn = 1