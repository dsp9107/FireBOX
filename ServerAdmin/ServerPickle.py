import socket
import time
import pickle

HEADERSIZE = 10

def prep(msg):
    payload = pickle.dumps(msg)
    payload = bytes(str(len(msg)).ljust(HEADERSIZE),"utf-8") + payload
    return payload

msg = "Welcome , Client"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 1237))
s.listen(5)

while True:
    ClientSocket, Address = s.accept()
    print(f"Connection from {Address} has been established")
#    msg = pickle.dumps(d)

    ClientSocket.send(prep(msg))

    while True:
        full_msg = b''
        new_msg = True
        msg = ClientSocket.recv(1024)
        if new_msg:
#            print("RECEIVED")
#            print(f"Message Length : {msg[:HEADERSIZE]}")
            msglen = int(msg[:HEADERSIZE].decode())
            new_msg = False
        full_msg += msg[HEADERSIZE:]
        if(len(full_msg)-HEADERSIZE == msglen):
#            print("Full Message Received")
#            print(full_msg)

            d = "CLIENT : " + pickle.loads(full_msg)
            print(d)

            new_msg = True
            full_msg = b''
