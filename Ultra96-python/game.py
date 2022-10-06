from asyncio import shield
import threading
from player import player
import json
from action import actions

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
        p1_action = kwargs[1]
        if self.singlePlayerMode:
            if p1_action == actions.shoot:
                self.players[1].shoot()
            elif p1_action == actions.grenade:
                self.players[1].grenade()
            elif p1_action == actions.reload:
                self.players[1].reload()
            elif p1_action == actions.shield:
                self.players[1].shield()
            else:
                self.players[1].exit()
        else:
            p2_action = p1_action = kwargs[2]
            if p1_action == actions.shield:
                self.players[1].shield()

            if p2_action == actions.shield:
                self.players[2].shield()

            if p1_action == actions.shoot and getShotMap[2]:
                self.players[1].shoot()
                self.players[2].getShot()

            if p2_action == actions.shoot and getShotMap[1]:
                self.players[2].shoot()
                self.players[1].getShot()

            if p1_action == actions.grenade:
                self.players[1].grenade()
                self.players[2].getGrenade()

            if p2_action == actions.grenade:
                self.players[2].grenade()
                self.players[1].getGrenade()
            
            if p1_action == actions.reload:
                self.players[1].reload()

            if p2_action == actions.reload:
                self.players[2].reload()

    def synchronise(self, gamestate):
        parsedGameDict = json.loads(gamestate)
        self.player[1].synchronise(parsedGameDict["p1"])
        if not self.isSinglePlayer:
            self.player[2].synchronise(parsedGameDict["p2"])

    def toJson(self):
        data = {}
        data["p1"] = self.players[1].__dict__
        if self.numOfPlayers > 1:
            data["p2"] = self.players[2].__dict__
        jsonData = json.dumps(data)
        return jsonData


    