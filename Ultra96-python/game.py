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
        for i in range(1,3,1):
            self.players[i] = player(i)
    
    def isSinglePlayer(self):
        return self.singlePlayerMode

    def takeAction(self,getShotMap = {}, **kwargs):
        p1_action = kwargs["1"]
        print(getShotMap)
        print("HERE")
        if self.singlePlayerMode:
            if p1_action == "shoot":
                self.players[1].shoot()
                if getShotMap[2]:
                    self.players[2].getShot()
            elif p1_action == "grenade":
                self.players[1].grenade()
                self.players[2].getGrenade()
            elif p1_action == "reload":
                self.players[1].reload()
            elif p1_action == "shield":
                self.players[1].shield()
            else:
                self.players[1].exit()
        else:
            p2_action = p1_action = kwargs["2"]
            if p1_action == "shield":
                self.players[1].shield()

            if p2_action == "shield":
                self.players[2].shield()

            if p1_action == "shoot" and getShotMap[2]:
                self.players[1].shoot()
                self.players[2].getShot()

            if p2_action == "shoot" and getShotMap[1]:
                self.players[2].shoot()
                self.players[1].getShot()

            if p1_action == "greande":
                self.players[1].grenade()
                self.players[2].getGrenade()

            if p2_action == "grenade":
                self.players[2].grenade()
                self.players[1].getGrenade()
            
            if p1_action == "reload":
                self.players[1].reload()

            if p2_action == "reload":
                self.players[2].reload()

    def synchronise(self, gamestate):
        parsedGameDict = json.loads(gamestate)
        self.players[1].synchronise(**parsedGameDict["p1"])
        if not self.isSinglePlayer:
            self.players[2].synchronise(**parsedGameDict["p2"])

    def toJson(self):
        data = {}
        data["p1"] = self.players[1].__dict__
        data["p2"] = self.players[2].__dict__
        jsonData = json.dumps(data)
        return jsonData


    