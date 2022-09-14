# echo-client.py
import pandas as pd
import socket
import json
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import io

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 5001  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        mydict = { 'p1' : {'hp': 4, 
            'action': None ,
            'bullets': 3,
            'grenades': 17, 
            'shield_time': 3,
            'shield_health': 1,
            'num_deaths': 22, 
            'num_shield': 12
            }, 'p2' : {'hp': 4, 
            'action': None ,
            'bullets': 3,
            'grenades': 17, 
            'shield_time': 3,
            'shield_health': 1,
            'num_deaths': 22, 
            'num_shield': 12
            }
            }
        key = "connecttoevalkey".encode("utf-8")
        iv = get_random_bytes(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        data = pad(json.dumps(mydict).encode("utf-8"), AES.block_size)
        encoded = base64.b64encode(iv + cipher.encrypt(data))
        sock.connect((HOST, PORT))
        prefix = (str(len(encoded)) + "_").encode("utf-8")
        while True:
            sock.sendall(prefix + encoded) 
            receivedMsg = sock.recv(2048)
            print(receivedMsg)