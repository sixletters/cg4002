import socket
HOST = "0.0.0.0"
import struct
MYTCP_PORT = 8080
import multiprocessing as mp
from connect import internalComms
import struct

def serialize(data):
    serialzedData = b''
    serialzedData += data["playerID"].to_bytes(1, 'little') 
    serialzedData += data["beetleID"].to_bytes(1, 'little')
    if data["beetleID"] == 0:
        a1 = struct.pack('<f', data["payload"]["a1"])
        a2 = struct.pack('<f', data["payload"]["a2"])
        a3 = struct.pack('<f', data["payload"]["a3"])
        g1 = struct.pack('<f', data["payload"]["g1"])
        g2 = struct.pack('<f', data["payload"]["g2"])
        g3 = struct.pack('<f', data["payload"]["g3"]) 
        serialzedData += a1 + a2 + a3 + g1 + g2 + g3
    return serialzedData
    

def init(dataBuffer):

    data2 = {
        "playerID" : 1,
        "beetleID": 1
    }

    data3 = {
       "playerID" : 2,
        "beetleID": 2,
    }


    dataBuffer.put(serialize(data2))
    dataBuffer.put(serialize(data3))
# def serialize(data):
#     serialzedData = b''
#     serialzedData += data["playerID"].to_bytes(2, 'little') 
#     serialzedData += data["beetleID"].to_bytes(2, 'little')
#     if data["beetleID"] == 0:   
#         serialzedData += data["packetOne"] + data["packetTwo"]

def relayProcess(dataBuffer, lock):
    while True:
        if not dataBuffer.empty():
            lock.acquire()
            action = dataBuffer.get()
            lock.release()
            serializedData = serialize(action)
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((HOST, MYTCP_PORT))
                sock.send(action)
                receivedMsg = sock.recv(2048)
                print(receivedMsg)
                sock.close()
                

if __name__ == '__main__':
    dataBuffer = mp.Queue()
    lock = mp.Lock()
    relay = mp.Process(target=relayProcess, args=(dataBuffer, lock))
    # internalCommsProcess = mp.process(target=internalComms, args=(dataBuffer, lock))
    init(dataBuffer)
    relay.start()
    # internalCommsProcess.start()
    relay.join()
    # internalCommsProcess.join()
    