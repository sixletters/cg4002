import threading
from player import player
import json

class Game:
    def __init__(self, numberOfPlayers = 1):
        self.numOfPlayers = numberOfPlayers
        self.singlePlayerMode = (numberOfPlayers == 1)
        self.players = {}
        for i in range(self.numOfPlayers):
            self.players[i+1] = player(i+1)
    
    def isSinglePlayer(self):
        return self.singlePlayerMode

    def takeAction(self,getShotMap = {}, **kwargs):
        p1_action = kwargs["1"]
        if self.numOfPlayers > 1:
            p2_action = kwargs["2"]

        
        ## FURTHER GAME LOGIC
        
    def toJson(self):
        data = {}
        data["p1"] = self.players[1].__dict__
        if self.numOfPlayers > 1:
            data["p2"] = self.players[2].__dict__
        jsonData = json.dumps(data)
        return jsonData


    