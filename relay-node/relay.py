import socket
HOST = "0.0.0.0"
import struct
MYTCP_PORT = 8080
import multiprocessing as mp
# from connect import internalComms

def relayProcess(dataBuffer, lock):
    while True:
        if not dataBuffer.empty():
            lock.acquire()
            action = dataBuffer.get()
            lock.release()
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((HOST, MYTCP_PORT))
                sock.send(action)
                receivedMsg = sock.recv(2048)
                print(receivedMsg)
                sock.close()
                
def serialize(data):
    serialzedData = b''
    serialzedData += data["playerID"].to_bytes(2, 'little') 
    serialzedData += data["beetleID"].to_bytes(2, 'little')
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
    data = {
        "playerID" : 1,
        "beetleID": 0,
        "payload" : {
            "a1" : 1.0,
            "a2" : 1.0,
            "a3" : 1.0,
            "g1" : 1.0,
            "g2" : 1.0,
            "g3" : 1.0
        }
    }

    data2 = {
        "playerID" : 1,
        "beetleID": 1
    }

    data3 = {
       "playerID" : 2,
        "beetleID": 0,
        "payload" : {
            "a1" : 1.0,
            "a2" : 1.0,
            "a3" : 1.0,
            "g1" : 1.0,
            "g2" : 1.0,
            "g3" : 1.0
        }
    }


    dataBuffer.put(serialize(data))
    dataBuffer.put(serialize(data2))
    dataBuffer.put(serialize(data3))

if __name__ == '__main__':

    dataBuffer = mp.Queue()
    lock = mp.Lock()
    relay = mp.Process(target=relayProcess, args=(dataBuffer, lock))
    init(dataBuffer)
    # internalComms = mp.process(target=internalComms, args=(dataBuffer, lock))
    relay.start()
    # internalComms.start()
    relay.join()
    # internalComms.join()
    