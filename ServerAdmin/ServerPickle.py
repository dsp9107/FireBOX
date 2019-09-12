import socket
import time
import pickle

HEADERSIZE = 10
d = {1: "Hello", 2: "World"}
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1236))
s.listen(5)

while True:
    ClientSocket, Address = s.accept()
    print(f"Connection from {Address} has been established")
    msg = pickle.dumps(d)
    #msg = bytes(f'{len(msg):<{HEADERSIZE}}', "utf-8") + msg
    msg = bytes(str(len(msg)).ljust(HEADERSIZE),"utf-8") + msg

    ClientSocket.send(msg)
