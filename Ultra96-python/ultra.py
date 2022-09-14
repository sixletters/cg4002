import multiprocessing as mp
from os import readlink
import socket
from player import player
import json
from Cryptodome.Cipher import AES
import base64
from Cryptodome.Random import get_random_bytes
from Crypto.Util.Padding import pad

MYTCP_PORT = 8080
tempDataMap = {
    1: "shield",
    2: "reload",
    3:"activate",
    4:"shoot",
    5:"exit"
}
playerdict = { 'p1' : {'hp': 4, 
            'action': None ,
            'bullets': 3,
            'grenades': 17, 
            'shield_time': 3,
            'shield_health': 1,
            'num_deaths': 22, 
            'num_shield': 12
            }, 
          'p2' : {'hp': 4, 
            'action': None ,
            'bullets': 3,
            'grenades': 17, 
            'shield_time': 3,
            'shield_health': 1,
            'num_deaths': 22, 
            'num_shield': 12
            }
}
key = "connecttoevalkey".encode("utf-8")
iv = get_random_bytes(AES.block_size)

def predict(data):
    return tempDataMap[data]

def jsonDataParser(predictedData):
    
    return json.dumps(predictedData)

def initialize(numOfPlayers, players):
    for i in range(numOfPlayers):
        players[i] = player()
    print(players)

def receiverProcess(dataBuffer, lock):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((str(socket.INADDR_ANY),MYTCP_PORT))
        sock.listen()
        while True:
            conn, addr = sock.accept()
            with conn:
                print(f"connected with {addr}")
                data = conn.recv(1024)
                lock.acquire()
                dataBuffer.put(data.decode("utf-8"))
                lock.release()
                conn.sendall("Data Received".encode("utf-8"))
                conn.close()
                
def senderProcess(dataBuffer, lock):
    p1 = False
    p2 = False
    toggle = 0
    EVAL_HOST = "127.0.0.1"  # The server's hostname or IP address
    EVAL_PORT = 5001 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((EVAL_HOST, EVAL_PORT))
        while True:
            if not dataBuffer.empty():
                if toggle == 0:
                    ## Player 1
                    lock.acquire()
                    rawData = int(dataBuffer.get())
                    lock.release()
                    playerdict['p1']['action'] = predict(rawData)
                    toggle = 1
                    p1 = True
                else:
                    ## Player 2
                    lock.acquire()
                    rawData = int(dataBuffer.get())
                    lock.release()
                    playerdict['p2']['action'] = predict(rawData)
                    toggle = 0
                    p2 = True
                
                if p1 and p2:
                    cipher = AES.new(key, AES.MODE_CBC, iv)
                    data = pad(json.dumps(playerdict).encode("utf-8"), AES.block_size)
                    encoded = base64.b64encode(iv + cipher.encrypt(data))
                    prefix = (str(len(encoded)) + "_").encode("utf-8")
                    encoded = prefix + encoded
                    sock.sendall(encoded)
                    receivedMsg = sock.recv(2048)
                    print(receivedMsg)
                    p1 = False
                    p2 = False

if __name__ == '__main__':
    num_of_players = input("Number of players:")
    players = {}
    # initialize(int(num_of_players), players)
    dataBuffer = mp.Queue()
    lock = mp.Lock()
    # sem = mp.Semaphore()
    receiver = mp.Process(target=receiverProcess, args=(dataBuffer,lock))
    sender = mp.Process(target=senderProcess, args=(dataBuffer, lock))
    sender.start()
    receiver.start()
    sender.join()
    receiver.join()