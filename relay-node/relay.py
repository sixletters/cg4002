import socket
HOST = "0.0.0.0"
MYTCP_PORT = 8080
tempDataMap = {
    "shield": "1",
    "reload": "2",
    "activate": "3",
    "shoot": "4",
    "exit": "5"
}

if __name__ == '__main__':
    while True:
        action = input("Enter the action")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((HOST, MYTCP_PORT))
            encodedAction = tempDataMap[action].encode("utf-8")
            sock.send(encodedAction)
            receivedMsg = sock.recv(2048)
            print(receivedMsg)
            sock.close()