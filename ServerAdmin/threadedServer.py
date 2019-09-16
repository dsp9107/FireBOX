import os
import json
import socket
import threading
import jsontransport as jt
from datetime import datetime

def main():                                                     # INITIALIZATION
    global config, pubKey, s, i, clients
    with open("config.json", "r") as read_file:
        config = json.load(read_file)

    pubKey = "pK-ub-E-li-Yc"
    clients = []

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), config['port']))
    s.listen(5)
    logUpdate(msg=f"SERVER STARTED AT {config['port']}")

def logUpdate(ip='', port='', user='', msgtype='', msglen='', msgcontent='', msg='', time=str(datetime.now())):
    log = open("log.txt", "a+")
    if msg:
        log.write(f"{time} {msg}\n")
    else:
        log.write(f"{time} {ip} {port} {user} {time} {msgtype} {msglen} {msgcontent}\n")
    log.close()

def serve(ClientSocket, Address):                               # SERVICE
    clientName = threading.current_thread().name
    ClientSocket.send(jt.pack(jt.prep("Welcome, Client"), config['headerSize']))

    while True:
        message = jt.unpack(ClientSocket.recv(1024), config['headerSize'])
        logUpdate(ip=Address[0], port=Address[1], user=clientName, msgtype=message['messageType'], msglen=message['messageLength'], msgcontent=message['messageContent'])
        if message['messageType'] == "request" :
            
            if message['messageContent']['terminate'] :
                print(f"{clientName} : <exiting>")
                break
            
            elif message['messageContent']['hostname'] :
                print(f"{clientName} : <requesting hostname>")
                ClientSocket.send(jt.pack(jt.prep(socket.gethostname()), config['headerSize']))

            elif message['messageContent']['pubKey'] :
                print(f"{clientName} : <requesting publicKey>")    
                ClientSocket.send(jt.pack(jt.prep(pubKey), config['headerSize']))

        elif message['messageType'] == "message" :
            print(f"{clientName} : {message['messageContent']}")
            
    print(f"{clientName} Has Left")

if __name__ == '__main__' :
    main()
    print(f"MAIN THREAD : {os.getpid()}")
    i = 0
    while i<config['maxClients']:
        clientSocket, Address = s.accept()
        logUpdate(msg=f"Client Connected From {Address} As C{i}")
        print(f"{Address} Has Joined As C{i}")
        client = threading.Thread(target=serve, name=f"C{i}", args=(clientSocket, Address))
        client.start()
        clients.append(client)
        i += 1
    for c in clients:
        c.join()
    logUpdate(msg=f"SERVER CLOSED\n")
    s.close()
