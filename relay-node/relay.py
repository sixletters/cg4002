import socket
HOST = "0.0.0.0"
import struct
MYTCP_PORT = 8080
import multiprocessing as mp
# from connect import internalComms
import struct

# def serialize(data):
#     serialzedData = b''
#     serialzedData += data["playerID"].to_bytes(1, 'little')
#     serialzedData += data["beetleID"].to_bytes(1, 'little')
#     if data["beetleID"] == 0:
#         a1 = struct.pack('<f', data["payload"]["a1"])
#         a2 = struct.pack('<f', data["payload"]["a2"])
#         a3 = struct.pack('<f', data["payload"]["a3"])
#         g1 = struct.pack('<f', data["payload"]["g1"])
#         g2 = struct.pack('<f', data["payload"]["g2"])
#         g3 = struct.pack('<f', data["payload"]["g3"]) 
#         serialzedData += a1 + a2 + a3 + g1 + g2 + g3
        
#     return serialzedData
    

def init(dataBuffer):
    ##grenade
    # dataBuffer.put({'playerID':1, 'beetleID': 0, 'packetOne': bytearray(b'\x00\xc0u?\x00\x00m\xbe\x00\x80\x9a\xbe'), 'packetTwo': bytearray(b'5w\xc1\xbf\xb0\xe2$\xc1ZF\xf4\xbf')})
    # dataBuffer.put({'playerID':1, 'beetleID': 0, 'packetOne': bytearray(b'\x00\xc0u?\x00\x00m\xbe\x00\x80\x9a\xbe'), 'packetTwo': bytearray(b'5w\xc1\xbf\xb0\xe2$\xc1ZF\xf4\xbf')})
    # dataBuffer.put({'playerID':1, 'beetleID': 0, 'packetOne': bytearray(b'\x00\xc0u?\x00\x00m\xbe\x00\x80\x9a\xbe'), 'packetTwo': bytearray(b'5w\xc1\xbf\xb0\xe2$\xc1ZF\xf4\xbf')})
    # dataBuffer.put({'playerID':1, 'beetleID': 0, 'packetOne': bytearray(b'\x00\xc0u?\x00\x00m\xbe\x00\x80\x9a\xbe'), 'packetTwo': bytearray(b'5w\xc1\xbf\xb0\xe2$\xc1ZF\xf4\xbf')})
    # dataBuffer.put({'playerID':1, 'beetleID': 0, 'packetOne': bytearray(b'\x00\xc0u?\x00\x00m\xbe\x00\x80\x9a\xbe'), 'packetTwo': bytearray(b'5w\xc1\xbf\xb0\xe2$\xc1ZF\xf4\xbf')})
    # dataBuffer.put({'playerID':1, 'beetleID': 0, 'packetOne': bytearray(b'\x00\xc0u?\x00\x00m\xbe\x00\x80\x9a\xbe'), 'packetTwo': bytearray(b'5w\xc1\xbf\xb0\xe2$\xc1ZF\xf4\xbf')})
    # dataBuffer.put({'playerID':1, 'beetleID': 0, 'packetOne': bytearray(b'\x00\xc0u?\x00\x00m\xbe\x00\x80\x9a\xbe'), 'packetTwo': bytearray(b'5w\xc1\xbf\xb0\xe2$\xc1ZF\xf4\xbf')})
    # dataBuffer.put({'playerID':1, 'beetleID': 0, 'packetOne': bytearray(b'\x00\xc0u?\x00\x00m\xbe\x00\x80\x9a\xbe'), 'packetTwo': bytearray(b'5w\xc1\xbf\xb0\xe2$\xc1ZF\xf4\xbf')})
    # dataBuffer.put({'playerID':1, 'beetleID': 0, 'packetOne': bytearray(b'\x00\xc0u?\x00\x00m\xbe\x00\x80\x9a\xbe'), 'packetTwo': bytearray(b'5w\xc1\xbf\xb0\xe2$\xc1ZF\xf4\xbf')})
    # dataBuffer.put({'playerID':1, 'beetleID': 0, 'packetOne': bytearray(b'\x00\xc0u?\x00\x00m\xbe\x00\x80\x9a\xbe'), 'packetTwo': bytearray(b'5w\xc1\xbf\xb0\xe2$\xc1ZF\xf4\xbf')})
    # dataBuffer.put({'playerID':1, 'beetleID': 0, 'packetOne': bytearray(b'\x00\xc0u?\x00\x00m\xbe\x00\x80\x9a\xbe'), 'packetTwo': bytearray(b'5w\xc1\xbf\xb0\xe2$\xc1ZF\xf4\xbf')})

    # #shield
    # dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x00\xc0}?\x00\x00\xf7\xbd\x00\x00k\xbe'), 'packetTwo': bytearray(b'do\x1d\xc1\x9c\x90\xb2\xc0/\xf8+?')})
    # dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x00\xd0\x7f?\x00\xc0\n\xbe\x00@j\xbe'), 'packetTwo': bytearray(b'\x93gY\xc1\xf4\x01\xd5\xc0{kC\xbe')})
    # dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x00\xd0\x7f?\x00\xc0\n\xbe\x00@j\xbe'), 'packetTwo': bytearray(b'\x93gY\xc1\xf4\x01\xd5\xc0{kC\xbe')})
    # dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x00\xc0}?\x00\x00\xf7\xbd\x00\x00k\xbe'), 'packetTwo': bytearray(b'do\x1d\xc1\x9c\x90\xb2\xc0/\xf8+?')})
    # dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x00\xc0}?\x00\x00\xf7\xbd\x00\x00k\xbe'), 'packetTwo': bytearray(b'do\x1d\xc1\x9c\x90\xb2\xc0/\xf8+?')})
    # dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x00\xc0}?\x00\x00\xf7\xbd\x00\x00k\xbe'), 'packetTwo': bytearray(b'do\x1d\xc1\x9c\x90\xb2\xc0/\xf8+?')})
    # dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x00\xc0}?\x00\x00\xf7\xbd\x00\x00k\xbe'), 'packetTwo': bytearray(b'do\x1d\xc1\x9c\x90\xb2\xc0/\xf8+?')})
    # dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x00\xc0}?\x00\x00\xf7\xbd\x00\x00k\xbe'), 'packetTwo': bytearray(b'do\x1d\xc1\x9c\x90\xb2\xc0/\xf8+?')})
    # dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x00\xc0}?\x00\x00\xf7\xbd\x00\x00k\xbe'), 'packetTwo': bytearray(b'do\x1d\xc1\x9c\x90\xb2\xc0/\xf8+?')})
    # dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x00\xc0}?\x00\x00\xf7\xbd\x00\x00k\xbe'), 'packetTwo': bytearray(b'do\x1d\xc1\x9c\x90\xb2\xc0/\xf8+?')})

    # #idle
    # dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x00\x90\x83?\x00\x00\xb9\xbd\x00\x80I\xbe'), 'packetTwo': bytearray(b'3\xa2\x8fB\x9a\xbb\xa0\xc1\x83\xbf\x1aA')})
    # dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x00\x90\x83?\x00\x00\xb9\xbd\x00\x80I\xbe'), 'packetTwo': bytearray(b'3\xa2\x8fB\x9a\xbb\xa0\xc1\x83\xbf\x1aA')})
    # dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x00\x90\x83?\x00\x00\xb9\xbd\x00\x80I\xbe'), 'packetTwo': bytearray(b'3\xa2\x8fB\x9a\xbb\xa0\xc1\x83\xbf\x1aA')})
    # dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x00\x90\x83?\x00\x00\xb9\xbd\x00\x80I\xbe'), 'packetTwo': bytearray(b'3\xa2\x8fB\x9a\xbb\xa0\xc1\x83\xbf\x1aA')})
    # dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x00\x90\x83?\x00\x00\xb9\xbd\x00\x80I\xbe'), 'packetTwo': bytearray(b'3\xa2\x8fB\x9a\xbb\xa0\xc1\x83\xbf\x1aA')})
    # dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x00\x90\x83?\x00\x00\xb9\xbd\x00\x80I\xbe'), 'packetTwo': bytearray(b'3\xa2\x8fB\x9a\xbb\xa0\xc1\x83\xbf\x1aA')})
    # dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x00\x90\x83?\x00\x00\xb9\xbd\x00\x80I\xbe'), 'packetTwo': bytearray(b'3\xa2\x8fB\x9a\xbb\xa0\xc1\x83\xbf\x1aA')})
    # dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x00\x90\x83?\x00\x00\xb9\xbd\x00\x80I\xbe'), 'packetTwo': bytearray(b'3\xa2\x8fB\x9a\xbb\xa0\xc1\x83\xbf\x1aA')})
    # dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x00\x90\x83?\x00\x00\xb9\xbd\x00\x80I\xbe'), 'packetTwo': bytearray(b'3\xa2\x8fB\x9a\xbb\xa0\xc1\x83\xbf\x1aA')})
    # dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x00\x90\x83?\x00\x00\xb9\xbd\x00\x80I\xbe'), 'packetTwo': bytearray(b'3\xa2\x8fB\x9a\xbb\xa0\xc1\x83\xbf\x1aA')})
    # dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x00\x90\x83?\x00\x00\xb9\xbd\x00\x80I\xbe'), 'packetTwo': bytearray(b'3\xa2\x8fB\x9a\xbb\xa0\xc1\x83\xbf\x1aA')})

    #relay
    # dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x00\xc0u?\x00\x00m\xbe\x00\x80\x9a\xbe'), 'packetTwo': bytearray(b'5w\xc1\xbf\xb0\xe2$\xc1ZF\xf4\xbf')})
    # dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x00\x90x?\x00\x00X\xbe\x00 \x93\xbe'), 'packetTwo': bytearray(b'\xe5Y\x86\xc0J\x9e\xa5\xc0\xb6a\x9a\xbf')})
    # dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x00\x00v?\x00\xc0V\xbe\x00\x80\x97\xbe'), 'packetTwo': bytearray(b'\xc7\xde\xda\xbf\xd9[\x1b\xc1)y\x16\xc0')})
    # dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x00pu?\x00\x00c\xbe\x00\x80\x95\xbe'), 'packetTwo': bytearray(b'`\xc5\xe9\xc0\xdd\x05\xcf\xc1u\xec\x95A')})
    # dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x00P\x86?\x00\xa0\x0f\xbf\x00\xa0\xd4\xbe'), 'packetTwo': bytearray(b'\xe1\xaf\xca\xc1?\xa0\xb2\xc2\x1d{9C')})
    # dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x00\x80c?\x00p\xc4\xbf\x00\x10S\xbf'), 'packetTwo': bytearray(b'ZF\xeaB\x89>\xc0\xc29!zC')})
    # dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x00\x90\n?\x00\x009\xbf\x00@\xa2\xbe'), 'packetTwo': bytearray(b'9!zC\xc7\xde\xcaB9!zC')})
    # dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x00\x00\xb8\xbc\x00\xe0\xbf>\x00\x00\t\xbf'), 'packetTwo': bytearray(b'\\\x1b0C\xfa\x80>C!%\x04C')})
    # dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x00\xa0\xec\xbe\x00 7?\x00\xb8\xf6\xbf'), 'packetTwo': bytearray(b'?\xa0\xa0\xc2-#z\xc3\x12}\xcc\xc2')})
    # dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x00\x00\xe0=\x00\x00A=\x00\x80\x94\xbf'), 'packetTwo': bytearray(b'1\xcd\x05B-#z\xc3+N\xd8\xc2')})
    # dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x00H\xc1?\x00\x00\x16\xbe\x00\x88\x98?'), 'packetTwo': bytearray(b'F\xf4\x89\xc1\x9c\x90\xfa\xc1\x91\x92+B')})
    # dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x00`\xe9>\x00\x00\xac\xbc\x00`\xfa>'), 'packetTwo': bytearray(b'\xee\x82\xd3\xc2H\xc9@\xc3\xfa\x80\x94B')})
    # dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x00`a?\x00\x00Z\xbe\x00@<>'), 'packetTwo': bytearray(b'\xc9\xb3\xe6\xc2\x81\xea%\xc3\x02\xd5\x89\xc1')})
    # dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x00(\xa3?\x00\xc0\x9b\xbe\x00 \xb7\xbe'), 'packetTwo': bytearray(b'J\x9eM\xc3\x1b\xa6\x1d\xc2\x89>\xf4\xc2')})
    # dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x00\xa0\xc7?\x00\x80c\xbe\x00\xb0\x02\xbf'), 'packetTwo': bytearray(b'\xb4\x8c\x0f\xc3\xa8\x8e\x95\xc2\xaaco\xc1')})
    # dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x00 \x93?\x00\xc0~\xbe\x00\x80\x17\xbe'), 'packetTwo': bytearray(b'\xa0:\x12Bdo\rB\xe7.\xf6B')})
    # dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x00\xe8\x91?\x00\x00\xac\xbc\x00@\x9f\xbe'), 'packetTwo': bytearray(b'^\xf0\xefA\x0c\xfe\xca\xc1\x87i\x13C')})
    # dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x00\x10\x82?\x00@\x87\xbe\x00\x80\x90\xbe'), 'packetTwo': bytearray(b"\x15\'2\xc3\xfcU\xda\xc2\xf8\xab1C")})
    # dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x00 \xe8>\x00 \x05\xbf\x00\xd0+\xbf'), 'packetTwo': bytearray(b'-#z\xc3\x10\xa8\x0e\xbfb\x9a\xa3B')})
    # dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x00\x00\x86>\x00\x80k\xbe\x00`k\xbf'), 'packetTwo': bytearray(b'\xdb0E\xc2T\xc7\x06Bm\x98f@')})
    # dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x00\x00\xd3>\x00@\x10\xbe\x00\xd0]\xbf'), 'packetTwo': bytearray(b'\xee\x82??\xae\r\x9bA\x14RB\xc1')})
    # dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x00 \x17?\x00\x80\x11\xbe\x00\xf0_\xbf'), 'packetTwo': bytearray(b'\xcf2\xa2\xc0\x1b\xa6\t\xc1\xa4\xe4\x19@')})
    # dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x00@\x08?\x00\x00\xac\xbd\x00\xc0L\xbf'), 'packetTwo': bytearray(b'\xa6\xb9\x83\xc1NH\xc9\xbf5w1A')})
    # dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x00\xe0\x0c?\x00\xc0\n\xbe\x00@E\xbf'), 'packetTwo': bytearray(b'k\xc3\xec\xc1\xcf2\xa2\xbfLs\x17\xc0')})
    #reload    
    dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x00pk?\x00\xc0\xc3\xbe\x00\x80|\xbe'), 'packetTwo': bytearray(b'\x96\x11\xfd\xc0do\xcd\xc0\xb0\xe2\x04\xbf')})
    dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x000p?\x00`\xc7\xbe\x00\x80y\xbe'), 'packetTwo': bytearray(b'\xf4\x01\x05\xc1\x1b\xa6\xb9\xc0\xac8\xa1\xbf')})
    dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x00\xf0k?\x00 \xb5\xbe\x00@q\xbe'), 'packetTwo': bytearray(b'b\x9a\xfb\xc0Xq\xa2\xc0\xee\x82\xbf\xc0')})
    dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x00\xa0r?\x00\xe0\xab\xbe\x00\x80O\xbe'), 'packetTwo': bytearray(b'\xf0W1\xc0D\x1f\xd0\xbf\x02\xd5Q\xc1')})
    dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x00pr?\x00\x80\xb7\xbe\x00@z\xbe'), 'packetTwo': bytearray(b'%\xcfR\xc1!%\xdf\xc1\xd1\x07DA')})
    dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x00\x90Y?\x000"\xbf\x00\x90\x1c\xbf'), 'packetTwo': bytearray(b'\x85\x94\xd6\xc2R\xf2T\xc3J\x9e\x14C')})
    dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x00\xb0\x0e?\x00\x00\xe7\xbe\x00\xb8\x87\xbf'), 'packetTwo': bytearray(b'\xac8\xc1\xc2\x8d\xe89\xc3\xcd]\x8aB')})
    dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x00\x00\x84\xbd\x00\x00}\xbe\x00P-\xbf'), 'packetTwo': bytearray(b'\xb0\xe2\xc2\xc2NH\xb9\xc1\xae\r\xebA')})
    dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x00@(\xbe\x00\xc00\xbe\x00\x10V\xbf'), 'packetTwo': bytearray(b'\x14RFB\xec\xad\x8fB\xa0:\xb6\xc1')})
    dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x00\x00\x88\xbb\x00\xe0\xdf\xbe\x00@k\xbf'), 'packetTwo': bytearray(b'=\xcbpB\x1b\xa6\xffB\xae\r\x93\xc2')})
    dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x00\xa0\r?\x00@\xd0\xbe\x00PZ\xbf'), 'packetTwo': bytearray(b'\x1b\xa6%Bh\x19\xe5B\xa0:\xe2\xc2')})
    dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x00\x10e?\x00\x00\xe9\xbe\x00P\x1b\xbf'), 'packetTwo': bytearray(b'\xf8\xab\xa8\xc1\xc7\xdeJA@u4\xc2')})
    dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x000g?\x00\xe0\x94\xbe\x00\xc0\xbc\xbe'), 'packetTwo': bytearray(b'\x17\xfc\x87B\xee\x82\x7f@\xd3\xdc5\xc2')})
    dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x00 \x80?\x00\x80;\xbe\x00 \xab\xbe'), 'packetTwo': bytearray(b'\xf0W\x89\xc1\x9ee\x04\xc1\x87i\x1eA')})
    dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x00P~?\x00\x00\xe2\xbc\x00\xc0\xa2\xbe'), 'packetTwo': bytearray(b'\xf0W\x0b\xc3\xf6\xd6\xde\xc1\x89>\xa8B')})
    dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x00\xc0O?\x00\x00\xa1\xbe\x00@\xdb\xbe'), 'packetTwo': bytearray(b'\x8b\x13\xd4\xc2)y\x06\xc1\xaacsB')})
    dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x000P?\x00@\xa7\xbe\x00\xc0\x1f\xbf'), 'packetTwo': bytearray(b'H\xc93\xc2\x06\x7f]\xc2T\xc7\xfeA')})
    dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x000d?\x00@\n\xbe\x00\xb0u\xbf'), 'packetTwo': bytearray(b'\xcd]\xc4\xc2\x1b\xa6\xbbB\xb2\xb7\x1aB')})
    dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x00\x80(?\x00\x00\xd0\xbb\x00`G\xbf'), 'packetTwo': bytearray(b'\xfa\x80\x02\xc2@u,A\xcb\x88\x8eA')})
    dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x0000?\x00\x00X\xbd\x00\x80K\xbf'), 'packetTwo': bytearray(b'\xa4\xe4Y\xc2\xbe\xb5!\xc1qBjA')})
    dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x00\xd0M?\x00\x00\xda\xbc\x00P6\xbf'), 'packetTwo': bytearray(b'\xfa\x80\x80Bj\xee\xba\xc1\xdb0\r\xc2')})
    dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x00\xf0<?\x00\x00\x85\xbd\x00\x00N\xbf'), 'packetTwo': bytearray(b'qB\x1aALs\x97\xc0\x06\x7f\x15\xc0')})
    dataBuffer.put({'playerID':1,'beetleID': 0, 'packetOne': bytearray(b'\x00\xa07?\x00\x00h<\x00@Z\xbf'), 'packetTwo': bytearray(b'Xq\x82\xc0\xac8\xa1?\xe5Y\xc6?')})

def serialize(data):
    serialzedData = b''
    serialzedData += data["playerID"].to_bytes(2, 'little') 
    serialzedData += data["beetleID"].to_bytes(2, 'little')
    if data["beetleID"] == 0:   
        serialzedData += data["packetOne"] + data["packetTwo"]
    return serialzedData

def relayProcess(dataBuffer, lock):
    while True:
        if not dataBuffer.empty():
            lock.acquire()
            action = dataBuffer.get()
            lock.release()
            serializedData = serialize(action)
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((HOST, MYTCP_PORT))
                sock.send(serializedData)
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
    