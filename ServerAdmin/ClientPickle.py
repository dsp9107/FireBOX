import socket
import time
import pickle

HEADERSIZE = 10
ENCODING = "utf-8"
reqexit = {'terminate': 1}
reqhn = {'hostname': 1}
reqpubkey = {'pubKey': 1}

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

host = 'localhost'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, 1237))

print(f"\nConnection With {host} Has Been Established")

message = unpack(s.recv(1024))
print("SERVER ~ " + message)
while True:
    mess = str(input("SERVER : "))
    if mess == "<reqhn>" :
        mess = str(reqhn)
        s.send(pack(mess))
        hn = s.recv(1024)
        print("SERVER ~ " + unpack(hn))
    elif mess == "<reqpubkey>" :
        mess = str(reqpubkey)
        s.send(pack(mess))
        hn = s.recv(1024)
        print("SERVER ~ " + unpack(hn))
    elif mess == "<reqexit>" :
        mess = str(reqexit)
        s.send(pack(mess))
        break
    else :
        s.send(pack(mess))
            
print(f"Connection With {host} Has Been Terminated")
