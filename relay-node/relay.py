import socket
HOST = "0.0.0.0"
import struct
MYTCP_PORT = 8080
import multiprocessing as mp
import concurrent.futures
import json
import util
import threading
import math
from connect import internalComms
import struct  
WINDOW_LEN = 20
THRESHOLD = 0.0

def init(dataBuffer):
    dataBuffer.put({'playerID':1,'beetleID': 0, "payload":{'a1': 1.0, 'a2': 2.0 , 'a3': 1.0, "g1": 1.0, "g2":1.0, "g3": 1.0}})
    dataBuffer.put({'playerID':1,'beetleID': 1})
    dataBuffer.put({'playerID':1,'beetleID': 0, "payload":{'a1': 1.1, 'a2': 2.0 , 'a3': 1.0, "g1": 1.0, "g2":1.0, "g3": 1.0}})
    dataBuffer.put({'playerID':1,'beetleID': 0, "payload":{'a1': 1.2, 'a2': 2.0 , 'a3': 1.0, "g1": 1.0, "g2":1.0, "g3": 1.0}})
    dataBuffer.put({'playerID':1,'beetleID': 0, "payload":{'a1': 1.3, 'a2': 2.0 , 'a3': 1.0, "g1": 1.0, "g2":1.0, "g3": 1.0}})
    dataBuffer.put({'playerID':1,'beetleID': 0, "payload":{'a1': 1.2, 'a2': 2.1 , 'a3': 1.4, "g1": 1.5, "g2":1.6, "g3": 1.8}})
    dataBuffer.put({'playerID':1,'beetleID': 0, "payload":{'a1': 1.0, 'a2': 2.0 , 'a3': 1.0, "g1": 1.0, "g2":1.0, "g3": 1.0}})
    dataBuffer.put({'playerID':1,'beetleID': 0, "payload":{'a1': 1.0, 'a2': 2.0 , 'a3': 1.0, "g1": 1.0, "g2":1.0, "g3": 1.0}})
    dataBuffer.put({'playerID':1,'beetleID': 0, "payload":{'a1': 1.0, 'a2': 2.0 , 'a3': 1.0, "g1": 1.0, "g2":1.0, "g3": 1.0}})
    dataBuffer.put({'playerID':1,'beetleID': 0, "payload":{'a1': 1.0, 'a2': 2.0 , 'a3': 1.0, "g1": 1.0, "g2":1.0, "g3": 1.0}})
    dataBuffer.put({'playerID':1,'beetleID': 0, "payload":{'a1': 1.0, 'a2': 2.0 , 'a3': 1.0, "g1": 1.0, "g2":1.0, "g3": 1.0}})
    dataBuffer.put({'playerID':1,'beetleID': 0, "payload":{'a1': 1.0, 'a2': 2.0 , 'a3': 1.0, "g1": 1.0, "g2":1.0, "g3": 1.0}})
    dataBuffer.put({'playerID':1,'beetleID': 0, "payload":{'a1': 1.0, 'a2': 2.0 , 'a3': 1.0, "g1": 1.0, "g2":1.0, "g3": 1.0}})
    dataBuffer.put({'playerID':1,'beetleID': 0, "payload":{'a1': 1.0, 'a2': 2.0 , 'a3': 1.0, "g1": 1.0, "g2":1.0, "g3": 1.0}})
    dataBuffer.put({'playerID':1,'beetleID': 0, "payload":{'a1': 1.0, 'a2': 2.0 , 'a3': 1.0, "g1": 1.0, "g2":1.0, "g3": 1.0}})
    dataBuffer.put({'playerID':1,'beetleID': 0, "payload":{'a1': 1.0, 'a2': 2.0 , 'a3': 1.0, "g1": 1.0, "g2":1.0, "g3": 1.0}})
    dataBuffer.put({'playerID':1,'beetleID': 0, "payload":{'a1': 1.0, 'a2': 2.0 , 'a3': 1.0, "g1": 1.0, "g2":1.0, "g3": 1.0}})
    dataBuffer.put({'playerID':1,'beetleID': 0, "payload":{'a1': 1.0, 'a2': 2.0 , 'a3': 1.0, "g1": 1.0, "g2":1.0, "g3": 1.0}})
    dataBuffer.put({'playerID':1,'beetleID': 0, "payload":{'a1': 1.0, 'a2': 2.0 , 'a3': 1.0, "g1": 1.0, "g2":1.0, "g3": 1.0}})
    dataBuffer.put({'playerID':1,'beetleID': 0, "payload":{'a1': 1.0, 'a2': 2.0 , 'a3': 1.0, "g1": 1.0, "g2":1.0, "g3": 1.0}})
    dataBuffer.put({'playerID':1,'beetleID': 0, "payload":{'a1': 1.0, 'a2': 2.0 , 'a3': 1.0, "g1": 1.0, "g2":1.0, "g3": 1.0}})


def serialize(data):
    serialzedData = b''
    serialzedData += data["playerID"].to_bytes(2, 'little') 
    serialzedData += data["beetleID"].to_bytes(2, 'little')
    if data["beetleID"] == 0:   
        serialzedData += data["packetOne"] + data["packetTwo"]
    return serialzedData
    
def dataTransformation(IMU_DATA_BUFFER):
    parsedPacket = {
        "playerID": IMU_DATA_BUFFER[0]["playerID"],
        "beetleID": 0,
        "payload": {
        }
    }  
    a1 = []
    a2 = []
    a3 = []
    g1 = []
    g2 = []
    g3 = []
    for data in IMU_DATA_BUFFER:
        a1.append(data["payload"]["a1"])
        a2.append(data["payload"]["a2"])
        a3.append(data["payload"]["a3"])
        g1.append(data["payload"]["g1"])
        g2.append(data["payload"]["g2"])
        g3.append(data["payload"]["g3"])

    threadpool = []
    dataMap = {}
    threadpool.append(threading.Thread(target=util.dataParser, args=(util.normalize(a1),dataMap, "a1")))
    threadpool.append(threading.Thread(target=util.dataParser, args=(util.normalize(a2),dataMap, "a2")))
    threadpool.append(threading.Thread(target=util.dataParser, args=(util.normalize(a3),dataMap, "a3")))
    threadpool.append(threading.Thread(target=util.dataParser, args=(util.normalize(g1),dataMap, "g1")))
    threadpool.append(threading.Thread(target=util.dataParser, args=(util.normalize(g2),dataMap, "g2")))
    threadpool.append(threading.Thread(target=util.dataParser, args=(util.normalize(g3),dataMap, "g3")))
    for thread in threadpool:
        thread.start()
    for thread in threadpool:
        thread.join()

    parsedPacket["payload"] = dataMap
    return parsedPacket

def sendToUltra96(data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, MYTCP_PORT))
        sock.send(data)
        receivedMsg = sock.recv(2048)
        print(receivedMsg)
        sock.close()

def idle(data, threshold):
    avg = math.sqrt(data["payload"]["a1"][3] ** 2 + data["payload"]["a2"][3] ** 2 + data["payload"]["a3"][3] ** 2 )
    print(avg)
    if avg < threshold:
        return True
    else:
        return False


def relayProcess(dataBuffer, lock):
    P1_IMU_DATA_BUFFER = []  
    P2_IMU_DATA_BUFFER = []  
    while True:
        if not dataBuffer.empty():
            lock.acquire()
            data = dataBuffer.get()
            lock.release()
            
            if data["beetleID"] != 0:
                sendToUltra96(json.dumps(data).encode("utf-8"))
                continue

            if data["playerID"] == 1:
                P1_IMU_DATA_BUFFER.append(data)
                if len(P1_IMU_DATA_BUFFER) >= WINDOW_LEN:
                    parsed_data = dataTransformation(P1_IMU_DATA_BUFFER)
                    encodeddata = json.dumps(parsed_data).encode("utf-8")
                    if not idle(parsed_data, THRESHOLD):
                        print("SENDING")
                        sendToUltra96(encodeddata)
                    P1_IMU_DATA_BUFFER = []

            if data["playerID"] == 2:
                P2_IMU_DATA_BUFFER.append(data)
                if len(P2_IMU_DATA_BUFFER) >= WINDOW_LEN:
                    parsed_data = dataTransformation(P2_IMU_DATA_BUFFER)
                    if not idle(parsed_data, THRESHOLD):
                        print("SENDING")
                        sendToUltra96(parsed_data)
                    P2_IMU_DATA_BUFFER = []

                
                

if __name__ == '__main__':
    dataBuffer = mp.Queue()
    lock = mp.Lock()
    relay = mp.Process(target=relayProcess, args=(dataBuffer, lock))
    internalCommsProcess = mp.process(target=internalComms, args=(dataBuffer, lock))
    # init(dataBuffer)
    relay.start()
    internalCommsProcess.start()
    relay.join()
    internalCommsProcess.join()
    