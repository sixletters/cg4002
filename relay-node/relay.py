import socket
HOST = "0.0.0.0"
MYTCP_PORT = 8080
import multiprocessing as mp
from connect import internalComms

def relayProcess(dataBuffer, lock):
    while True:
        if not dataBuffer.empty():
            action = dataBuffer.get()
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
    internalComms = mp.process(target=internalComms, args=(dataBuffer, lock))
    relay.start()
    internalComms.start()
    relay.join()
    internalComms.join()