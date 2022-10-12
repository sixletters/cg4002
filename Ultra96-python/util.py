
import struct
from Cryptodome.Cipher import AES
import base64
from Cryptodome.Random import get_random_bytes
from Crypto.Util.Padding import pad
# import predict

INT_TO_ACTION_ARR = ["shield", "grenade","reload","exit", "idle"]

## Predict function to be implemented

## Deserialization of bytestream into a python dictionary
def deserialize(bytestream):
    playerID = bytestream[0] - 48
    beetleID = bytestream[1] - 48
    deserializedData = {
        "playerID" : playerID,
        "beetleID" : beetleID,
    }
    print(deserializedData)
    if beetleID == 0:
        a1 = struct.unpack('<f', bytestream[2:6])[0]
        a2 =  struct.unpack('<f', bytestream[6:10])[0]
        a3 =  struct.unpack('<f', bytestream[10:14])[0]
        g1 = struct.unpack('<f', bytestream[14:18])[0]
        g2 = struct.unpack('<f', bytestream[18:22])[0]
        g3 = struct.unpack('<f', bytestream[22:])[0]
        deserializedData['payload'] = [a1,a2,a3,g1,g2,g3]
    return deserializedData


def payloadParser(data, playerActionBuffer, IMU_DATA_BUFFER):
    predictionInputs = []
    for data in IMU_DATA_BUFFER:
        predictionInputs += data["payload"]
    # if data["beetleID"] == 0:
    #     playerActionBuffer[str(data["playerID"])] = INT_TO_ACTION_ARR[predict(predictionInputs)]
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

def serialize(data):
    serialzedData = b''
    serialzedData += data["playerID"].to_bytes(2, 'little') 
    serialzedData += data["beetleID"].to_bytes(2, 'little')
    if data["beetleID"] == 0:   
        serialzedData += data["packetOne"] + data["packetTwo"]