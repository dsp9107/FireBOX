import socket
import time
import pickle

HEADERSIZE = 10
ENCODING = "utf-8"

def pack(msg):
    payload = pickle.dumps(msg)
    payload = bytes(str(len(msg)).ljust(HEADERSIZE), ENCODING) + payload
    return payload

def unpack(message):
    msglen = int(message[:HEADERSIZE].decode())
    full_msg = message[HEADERSIZE:]
    if(len(full_msg)-HEADERSIZE == msglen):
        msg = pickle.loads(full_msg)
    return msg

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 1237))
s.listen(5)

while True:
    ClientSocket, Address = s.accept()
    print(f"\nConnection From {Address} Has Been Established")
    ClientSocket.send(pack("Welcome, Client"))

    while True:
        msg = ClientSocket.recv(1024)
        if msg:
            message = unpack(msg)
        if message == "<exit>" :
            print("CLIENT : <exiting>")
            break
        elif message == "{'request': [{'hostname': 1}]}" :
            print("CLIENT : <requesting hostname>")
            ClientSocket.send(pack(socket.gethostname()))
        else :
            d = "CLIENT : " + message
            print(d)
    print(f"Connection From {Address} Has Been Lost")
