import multiprocessing as mp
from os import readlink
from queue import Queue
import socket

from numpy import False_
from player import player
from game import Game
import json
from Cryptodome.Cipher import AES
import base64
from Cryptodome.Random import get_random_bytes
from Crypto.Util.Padding import pad
import threading
import time
import struct
import action
import util as util

MYTCP_PORT = 8080
EVAL_HOST = "127.0.0.1"  # The server's hostname or IP address
EVAL_PORT = 8090
BUFFER_LENGTH = 10

## Encryption intiliazation
key = "connecttoevalkey".encode("utf-8")
iv = get_random_bytes(AES.block_size)
BUFFER_INDEX = 0
THRESHOLD = 0.5

## Process that receives the data and puts it into the buffer
## Has a lock for critical section when accessing data buffer
def receiverProcess(dataBuffer, lock):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((str(socket.INADDR_ANY),MYTCP_PORT))
        sock.listen()
        while True:
            conn, addr = sock.accept()
            with conn:
                print(f"connected with {addr}")
                data = util.deserialize(conn.recv(1024))
                lock.acquire()
                dataBuffer.put(data)
                lock.release()
                conn.sendall("Data Received".encode("utf-8"))
                conn.close()


## Process that takes data from databuffer and sends it to the evaluation server
def senderProcess(dataBuffer, lock, currGame):

    ## Flag to dictate which player's action has been set
    playerFlags = {
        1: False,
        2: False
    }

    ## Buffer to store a player's action
    playerActionBuffer = {
        "1" : None,
        "2" : None
    }

    ## thread pool to put action calculations
    threadPool = []

    ## Buffer to store if a player has been shot 
    playerShotMap = {
        1 : False,
        2 : False
    }
    timerCount = 5
    IMU_DATA_BUFFER = []
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((EVAL_HOST, EVAL_PORT))
        while True:
            ## We only want to check when there is data in the buffer
            if not dataBuffer.empty():

                ## Critical Section, use lock to gain ownership of dataBuffer
                lock.acquire()
                Data = dataBuffer.get()
                lock.release()
                ## Single Player Mode -> Predict and then send
                if currGame.isSinglePlayer():
                    currPlayer = Data['playerID']
                    print(Data)
                    if Data["beetleID"] == 2 and not playerShotMap[Data["playerID"]]:
                        playerShotMap[Data["playerID"]] = True
                        continue

                    util.payloadParser(Data, playerActionBuffer, IMU_DATA_BUFFER)
                    currGame.takeAction(**playerActionBuffer)
                    encoded = util.formatData(currGame.toJson(),key,iv)
                    sock.sendall(encoded)
                    expectedGameState = sock.recv(2048)
                    for i in playerShotMap:
                        playerShotMap[i] = False
                    # print(expectedGameState)
                    # print("BREAK")
                    # print(expectedGameState[4:])
                    # currGame.synchronise(expectedGameState[4:])

                else:
                    ## Check playerID of the data
                    currPlayer = Data['playerID']

                    ## If player has already taken an action and if the data packet isnt a "get shot" packet, we can discard it
                    if playerFlags[currPlayer] and Data["beetleID"] != 2:
                        continue
                    
                    ## If it is a getshot packet, we can just set the getshot buffer as true as an input into take action
                    ## We then proceed on
                    if Data["beetleID"] == 2 and not playerShotMap[Data["playerID"]]:
                        playerShotMap[Data["playerID"]] = Data["payload"]
                        continue
                    
                    if Data["beetleID"] == 0:
                        if len(IMU_DATA_BUFFER) == BUFFER_LENGTH: 
                            IMU_DATA_BUFFER[BUFFER_INDEX] = Data
                        else:
                            IMU_DATA_BUFFER.append(Data)

                        BUFFER_INDEX += 1
                        if BUFFER_INDEX == BUFFER_LENGTH:
                            BUFFER_INDEX = 0
                    
                        if len(IMU_DATA_BUFFER) != BUFFER_LENGTH:
                            continue
                    
                    
                    ## If it is not a "get shot" packet, we set the action to true and then launch a worker thread to 
                    ## compute action based on data payload
                    playerFlags[currPlayer] = True
                    workerThread = threading.Thread(target=util.payloadParser, args=(Data, playerActionBuffer, IMU_DATA_BUFFER))
                    workerThread.start()
                    threadPool.append(workerThread)


            ## if both player 1 and player 2 has taken an action
            if playerFlags[1] and playerFlags[2]:
                for thread in threadPool:
                    thread.join()
                
                continueFlag = False
                for i in playerActionBuffer:
                    if playerActionBuffer[i] == "idle":
                        playerFlags[int(i)] = False
                        continueFlag = True

                if continueFlag:
                    continue

                IMU_DATA_BUFFER = []
                ## we wait for the threads to finish computation
                for thread in threadPool:
                    thread.join()

                ## We want to give a buffer time of 0.25 second to see if player has been shot
                if timerCount != 0:
                    time.sleep(0.05)
                    timerCount -= 1
                    continue
                else:
                    timerCount = 5

                ## we input the playerShotMap and action buffer into the take action function of currgame to update state
                currGame.takeAction(getShotMap=playerShotMap.copy(), **playerActionBuffer)

                ## get the currentgame state in json
                encoded = util.formatData(currGame.toJson(),key,iv)

                ## send
                sock.sendall(encoded)
                expectedGameState= sock.recv(2048)
                currGame.synchronise(expectedGameState[4:])
                for player in playerFlags:
                    playerFlags[player] = False

                for i in playerShotMap:
                        playerShotMap[i] = False


if __name__ == '__main__':
    num_of_players = int(input("Number of players:"))
    while num_of_players != 1 and num_of_players != 2:
        print("INVALID NUMBER OF PLAYERS, PLEASE INPUT AGAIN:")
        num_of_players = int(input("Number of players:"))

    dataBuffer = mp.Queue()
    lock = mp.Lock()
    currGame = Game(numberOfPlayers=num_of_players)
    receiver = mp.Process(target=receiverProcess, args=(dataBuffer,lock))
    sender = mp.Process(target=senderProcess, args=(dataBuffer, lock, currGame))
    sender.start()
    receiver.start()
    sender.join()
    receiver.join()