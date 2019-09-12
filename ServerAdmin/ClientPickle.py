import socket
import time
import pickle

HEADERSIZE = 10

def prep(msg):
    payload = pickle.dumps(msg)
    payload = bytes(str(len(msg)).ljust(HEADERSIZE),"utf-8") + payload
    return payload


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1237))

while True:
    print("CONNECTED")
    full_msg = b''
    new_msg = True
    while True:
        msg = s.recv(1024)
        if new_msg:
#            print("RECEIVED")
#            print(f"Message Length : {msg[:HEADERSIZE]}")
            msglen = int(msg[:HEADERSIZE].decode())
            new_msg = False
        full_msg += msg[HEADERSIZE:]
        if(len(full_msg)-HEADERSIZE == msglen):
#           print("Full Message Received")
#           print(full_msg[HEADERSIZE:])

           d = pickle.loads(full_msg)
           print(d)
           
           new_msg = True
           full_msg = b''
           print()
        while True:
            mess = str(input("SERVER : "))
            s.send(prep(mess))
#            print("SENT")
