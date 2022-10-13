import json
import threading
import time
import action
    
class player:
    def __init__(self, id):
        self.id = id
        self.hp = 100
        self.bullets = 6
        self.grenades = 2
        self.shield_time = 0
        self.shield_health = 0
        self.num_deaths = 0
        self.num_shield = 3
        self.action = None
        self.activated_shield = False

    def grenade(self):
        self.action = "grenade"
        if self.grenade:
            self.grenade -= 1

    
    def shield_health_counter(self):
        self.shield_time = 10
        while self.shield_time > 0:
            time.sleep(1)
            self.shield_time -= 1
        self.activate_shield = False


    def shield(self):
        self.action = "shield"
        if self.num_shield > 0 and not self.activated_shield:
            self.activated_shield = True
            t1 = threading.Thread(target=self.shield_health_counter, args=())
            self.shield_health = 30
            self.num_shield -= 1
            t1.start()
 
    def reload(self):
        self.action = "reload"
        if self.bullets == 0:
            self.bullets = 6

    def shoot(self):
        if self.bullets > 0:
            self.bullets -= 1
            self.action = "shoot"

    def getDamaged(self, damage):
        if self.activated_shield:
            if self.shield_health > damage:
                self.shield_health -= damage
            else:
                damage -= self.shield_health
                self.shield_health = 0
                self.hp -= damage
        else:
            self.hp -= damage

        if self.hp <= 0:
            self.num_shield = 3
            self.grenades = 2
            self.bullets = 6
            self.num_deaths += 1
            self.hp = 100

    def getGrenade(self):
        self.getDamaged(30)

    def getShot(self):
        self.getDamaged(10)
    
    def exit(self):
        print()
    
    def synchronise(self,**kwargs):
        for key,value in kwargs.items():
            setattr(self,key,value)