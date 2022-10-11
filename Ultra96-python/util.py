
import struct
from Cryptodome.Cipher import AES
import base64
from Cryptodome.Random import get_random_bytes
from Crypto.Util.Padding import pad

INT_TO_ACTION_ARR = ["shield", "grenade","reload","exit"]

## Predict function to be implemented
def predict(data):
    return "shield"

## Deserialization of bytestream into a python dictionary
def deserialize(bytestream):
    playerID = int.from_bytes(bytestream[0:2], "little")
    beetleID = int.from_bytes(bytestream[2:4], "little")
    deserializedData = {
        "playerID" : playerID,
        "beetleID" : beetleID,
    }
    if beetleID == 0:
        a1 = struct.unpack('<f', bytestream[4:8])[0]
        a2 =  struct.unpack('<f', bytestream[8:12])[0]
        a3 =  struct.unpack('<f', bytestream[12:16])[0]
        g1 = struct.unpack('<f', bytestream[16:20])[0]
        g2 = struct.unpack('<f', bytestream[20:24])[0]
        g3 = struct.unpack('<f', bytestream[24:])[0]
        deserializedData['payload'] = [a1,a2,a3,g1,g2,g3]
    return deserializedData

def idleChecker(data, IMU_PREV_DATA, THRESH):
    curr_payload = data["payload"]
    prev_payload = ["payload"]
    diffSum = abs(curr_payload[0] - prev_payload[0]) + abs(curr_payload[1] - prev_payload[1]) + abs(curr_payload[2] - prev_payload[2])
    if diffSum < THRESH:
        return True
    return False
## Parses the payload of the data to an action

def payloadParser(data, playerActionBuffer):
    if data["beetleID"] == 0:
        playerActionBuffer[str(data["playerID"])] = INT_TO_ACTION_ARR[predict(data["payload"])]
    elif data["beetleID"] == 1:
        playerActionBuffer[str(data["playerID"])] = "shoot"
    

## Input game state in Json, output encoded data to be sent
def formatData(gameState, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    gameStateData = pad(gameState.encode("utf-8"), AES.block_size)
    encoded = base64.b64encode(iv + cipher.encrypt(gameStateData ))
    prefix = (str(len(encoded)) + "_").encode("utf-8")
    encoded = prefix + encoded
    return encoded