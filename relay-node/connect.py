from bluepy.btle import Peripheral, DefaultDelegate, BTLEDisconnectError
import struct
import threading
import time
import multiprocessing as mp
import numpy

idOfBeetle1 = 0
macAddressBeetle1 = "C4:BE:84:20:1A:5C"
idOfBeetle2 = 1
macAddressBeetle2 = "C4:BE:84:20:1C:4D"
idOfBeetle3 = 2
macAddressBeetle3 = "B0:B1:13:2D:B5:02"
characteristicToWrite = "0000dfb1-0000-1000-8000-00805f9b34fb"

helloBuffer = [0, 0, 0]
receivingBuffer = ""
allBeetlesConnected = []
nakBuffer = [0, 0, 0]
ackBuffer = [0, 0, 0]


class Delegate(DefaultDelegate):
    def __init__(self, idOfBeetle, dataBuffer, lock):
        DefaultDelegate.__init__(self)
        self.idOfBeetle = idOfBeetle
        self.dataBuffer = dataBuffer
        self.lock = lock
        self.handshake = False
        self.fullPacket = False
        self.packetOneCount = bytearray(0)
        self.packetTwoCount = bytearray(0)

    def doChecksum(self, packetData):
        checksum = 0

        for i in range(19):
            checksum = (checksum ^ packetData[i]) & 0xFF
        
        if checksum == packetData[19]:
            return True
        else:
            return False

    def handleNotification(self, cHandle, data):
        global receivingBuffer
        receivingBuffer += data

        if(len(receivingBuffer) >= 20):
            packet = bytearray(receivingBuffer[0:20])
            receivingBuffer = receivingBuffer[20:]
            packetType = struct.unpack('b', packet[1:2])
            if self.idOfBeetle == 0:
                if self.doChecksum(packet) == True:
                    if self.handshake and packetType == (0,):
                        self.packetOne = packet[3:15]
                        self.packetOneCount = packet[2]
                    elif self.handshake and packetType == (1,):
                        self.packetTwo = packet[3:15]
                        self.packetTwoCount = packet[2]
                        self.fullPacket = True
                    else:
                        pass
                else:
                    print(self.idOfBeetle, " corrupted Packet")
                    pass

                if self.fullPacket and (self.packetOneCount + 1 == self.packetTwoCount):
                    PLAYER_ID = 1
                    serialzedData = b''
                    serialzedData += PLAYER_ID.to_bytes(2, 'little') 
                    serialzedData += self.idOfBeetle.to_bytes(2, 'little')
                    serialzedData +=  self.packetOne + self.packetTwo
                    self.lock.acquire()
                    self.dataBuffer.put(serialzedData)
                    self.lock.release()
                    self.fullPacket = False
                    
            elif self.idOfBeetle == 1:
                if self.doChecksum(packet) == True:
                    if self.handshake:
                        PLAYER_ID = 1
                        serialzedData = b''
                        serialzedData += PLAYER_ID.to_bytes(2, 'little') 
                        serialzedData += self.idOfBeetle.to_bytes(2, 'little')
                        self.lock.acquire()
                        self.dataBuffer.put(serialzedData)
                        self.lock.release()
                        ackBuffer[self.idOfBeetle] = 1
                    else:
                        pass
                else:
                    nakBuffer[self.idOfBeetle] = 1
                    print(self.idOfBeetle, " corrupted packet")
                    pass
            
            elif self.idOfBeetle == 2:
                if self.doChecksum(packet) == True:
                    if self.handshake:
                        PLAYER_ID = 2
                        serialzedData = b''
                        serialzedData += PLAYER_ID.to_bytes(2, 'little') 
                        serialzedData += self.idOfBeetle.to_bytes(2, 'little')
                        self.lock.acquire()
                        self.dataBuffer.put(serialzedData)
                        self.lock.release()
                        ackBuffer[self.idOfBeetle] = 1
                    else:
                        pass
                else:
                    nakBuffer[self.idOfBeetle] = 1
                    print(self.idOfBeetle, " corrupted packet")
                    pass

            else:
                pass
        elif len(receivingBuffer) == 1 and data == str.encode("A"):
            print('ACK SENT')
            self.handshake = True
            helloBuffer[self.idOfBeetle] = 1
            receivingBuffer = ""
        else: 
            print(self.idOfBeetle, " fragmented")
            pass
     
class Communication:
    def __init__(self, idOfBeetle, macAddress, dataBuffer, lock):
        self.idOfBeetle = idOfBeetle
        self.macAddress = macAddress
        self.dev = None
        self.devDelegate = None
        self.dataBuffer = dataBuffer
        self.lock = lock

    def writeToBeetle(self, val):
        characteristics = self.dev.getCharacteristics()
        for characteristic in characteristics:
            if characteristic.uuid == characteristicToWrite:
                print("sending", val, "packet to ", self.idOfBeetle)
                characteristic.write(bytes(val), withResponse=False)

    def connectToBeetle(self):
        while 1:
            try:
                self.dev = Peripheral(self.macAddress)
                print("connected!")
                devDelegate = Delegate(self.idOfBeetle, self.dataBuffer, self.lock)
                self.dev.setDelegate(devDelegate)
                break
            except Exception as e:
                print("Unable to connect: ", e)
                pass
    
    def threeWayHandshake(self):
        handshake = False
        while handshake == False:
            self.dev.waitForNotifications(1.0)
            if len(helloBuffer) != 0 and helloBuffer[self.idOfBeetle] == 1:
                self.writeToBeetle("B")
                handshake = True
                break
            else:
                self.writeToBeetle("A")
        print(self.idOfBeetle, ' handshake completed')
        return handshake

    
    def protocol(self):

        handshake = False
        while True:
            try:
                if handshake:
                    self.dev.waitForNotifications(0.001)
                    if len(ackBuffer) != 0 and ackBuffer[self.idOfBeetle] == 1:
                        self.writeToBeetle("D")
                        ackBuffer[self.idOfBeetle] = 0
                    elif len(nakBuffer) != 0 and nakBuffer[self.idOfBeetle] == 1:
                        self.writeToBeetle("C")
                        nakBuffer[self.idOfBeetle] = 0
                    pass
                else:
                    self.connectToBeetle()
                    handshake = self.threeWayHandshake()
            except KeyboardInterrupt:
                self.dev.disconnect() 
            except (BTLEDisconnectError, AttributeError):
                print(self.idOfBeetle, ' disconnected!')
                handshake = False
                helloBuffer[self.idOfBeetle] = 0

def internalComms(dataBuffer, lock):
    beetle1 = Communication(idOfBeetle1, macAddressBeetle1, dataBuffer, lock)
    thread1 = threading.Thread(target=beetle1.protocol, args=())
    beetle2 = Communication(idOfBeetle2, macAddressBeetle2, dataBuffer, lock)
    thread2 = threading.Thread(target=beetle2.protocol, args=())
    beetle3 = Communication(idOfBeetle3, macAddressBeetle3, dataBuffer, lock)
    thread3 = threading.Thread(target=beetle3.protocol, args=())
    thread1.start()
    thread2.start()
    thread3.start()