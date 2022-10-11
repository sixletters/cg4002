import socket
HOST = "0.0.0.0"
import struct
MYTCP_PORT = 8080
import multiprocessing as mp
from connect import internalComms

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
                

if __name__ == '__main__':
    dataBuffer = mp.Queue()
    lock = mp.Lock()
    relay = mp.Process(target=relayProcess, args=(dataBuffer, lock))
    internalCommsProcess = mp.process(target=internalComms, args=(dataBuffer, lock))
    relay.start()
    internalCommsProcess.start()
    relay.join()
    internalCommsProcess.join()
    