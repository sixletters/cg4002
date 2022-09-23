import socket

from Ultra96-python.ultra import receiverProcess
HOST = "0.0.0.0"
MYTCP_PORT = 8080
import multiprocessing as mp

# tempDataMap = {
#     "shield": "1",
#     "reload": "2",
#     "activate": "3",
#     "shoot": "4",
#     "exit": "5",
#     "grenade": "6"
# }
def relayProcess(dataBuffer, lock):
    while True:
        if not dataBuffer.empty():
            action = dataBuffer.get()
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((HOST, MYTCP_PORT))
                encodedAction = action.serialise()
                sock.send(encodedAction)
                receivedMsg = sock.recv(2048)
                print(receivedMsg)
                sock.close()
                
def internalComms(dataBuffer,lock):
    while True:
        ## INTERNAL COMMS SHUD BE PUTTING THE STRUCTURES INTO THE DATABUFFER
        print("INTERNAL COMMS STUFF")
        
if __name__ == '__main__':
    dataBuffer = mp.Queue()
    lock = mp.Lock()
    relay = mp.Process(target=receiverProcess, args=(dataBuffer, lock))
    internalComms = mp.process(target=internalComms, args=(dataBuffer, lock))
    relay.start()
    internalComms.start()
    relay.join
    internalComms.join