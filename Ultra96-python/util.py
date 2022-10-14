
import struct
from Cryptodome.Cipher import AES
import base64
from Cryptodome.Random import get_random_bytes
from Crypto.Util.Padding import pad
# from predict import predicts
import socket
import threading
# from pynq import Overlay
import json
# import pynq.lib.dma
INT_TO_ACTION_ARR = ["shield", "grenade","reload","exit", "idle"]

## Predict function to be implemented

# overlay = Overlay('/home/xilinx/cg4002/Ultra96-python/fourthProtoModel/design_3_wrapper.bit')
# dma = overlay.axi_dma_0

## Deserialization of bytestream into a python dictionary
def deserialize(datastream):
    return json.loads(datastream)

def payloadParser(data, playerActionBuffer):
    if data["beetleID"] == 0:
        prediction_inputs = []
        for i in data["payload"]:
            prediction_inputs.append(data["payload"][i])
        # playerActionBuffer[str(data["playerID"])] = INT_TO_ACTION_ARR[predicts(prediction_inputs,dma)]
        playerActionBuffer[str(data["playerID"])] = "grenade"
    if data["beetleID"] == 1:
        playerActionBuffer[str(data["playerID"])] = "shoot"
    

## Input game state in Json, output encoded data to be sent
def formatData(gameState, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    gameStateData = pad(gameState.encode("utf-8"), AES.block_size)
    encoded = base64.b64encode(iv + cipher.encrypt(gameStateData ))
    prefix = (str(len(encoded)) + "_").encode("utf-8")
    encoded = prefix + encoded
    return encoded

def receiveGameState(sock):
    length = b''
    i = sock.recv(1)
    length += i
    while i.decode("utf-8") != '_':
        i = sock.recv(1)
        if i.decode("utf-8") != '_':
            length += i                            
    length = int(length.decode("utf-8"))
    expectedgamestate = sock.recv(length)
    return expectedgamestate