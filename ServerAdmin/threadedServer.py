import os
import sys
import json
import socket
import threading
import jsontransport as jt
from datetime import datetime

def main():                                                     # INITIALIZATION
    global config, pubKey, s, i, clients, connections
    with open("config.json", "r") as read_file:
        config = json.load(read_file)

    pubKey = "pK-ub-E-li-Yc"
    clients = []
    connections = []
    i = threading.activeCount()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    s.bind((socket.gethostname(), config['port']))
    s.listen(5)
    s.settimeout(12)
    logUpdate(msg=f"SERVER STARTED AT {config['port']}")
    print(f"{socket.gethostname()} Is Listening At {config['port']}")

def logUpdate(ip='', port='', user='', msgtype='', msglen='', msgcontent='', msg=''):
    time = str(datetime.now())
    log = open("log.txt", "a+")
    if msg:
        log.write(f"{time} {msg}\n")
    else:
        log.write(f"{time} {ip} {port} {user} {time} {msgtype} {msglen} {msgcontent}\n")
    log.close()

def acquireID():
    global connections
    mx = config['maxClients']
    if len(connections) != mx :
        for i in range(1,mx+1):
            if i not in connections:
                connections.append(i)
                nxt = i
                break
    else :
        nxt = 0
    return nxt

def revokeID(ID):
    global connections
    status = False
    if ID in connections :
        connections.remove(ID)
        status = True
    return status

def serve(ClientSocket, Address):                               # SERVICE
    clientName = threading.current_thread().name
    logUpdate(msg=f"Client Connected From {Address} As {clientName}")
    print(f"{Address} Has Joined As {clientName}")
    ClientSocket.send(jt.pack(jt.prep("Welcome, Client"), config['headerSize']))

    while True:
        message = jt.unpack(ClientSocket.recv(1024), config['headerSize'])
        logUpdate(ip=Address[0], port=Address[1], user=clientName, msgtype=message['messageType'], msglen=message['messageLength'], msgcontent=message['messageContent'])
        if message['messageType'] == "request" :
            
            if message['messageContent']['terminate'] :
                print(f"{clientName} : <exiting>")
                revokeID(int(clientName[1:]))
                break
            
            elif message['messageContent']['hostname'] :
                print(f"{clientName} : <requesting hostname>")
                ClientSocket.send(jt.pack(jt.prep(socket.gethostname()), config['headerSize']))

            elif message['messageContent']['pubKey'] :
                print(f"{clientName} : <requesting publicKey>")    
                ClientSocket.send(jt.pack(jt.prep(pubKey), config['headerSize']))

        elif message['messageType'] == "message" :
            print(f"{clientName} : {message['messageContent']}")
    logUpdate(msg=f"{clientName} Disconnected From {Address}")
    print(f"{clientName} Has Left")

if __name__ == '__main__' :
    main()
    while i<(threading.activeCount()+config['maxClients']):
        try :
            clientSocket, Address = s.accept()
        except socket.timeout :
            logUpdate(msg=f"SERVER CLOSED DUE TO INACTIVITY\n")
            print("SERVER CLOSED DUE TO INACTIVITY")
            s.close()
            sys.exit()
        else :
            clientID = acquireID()
            if not clientID :
                clientSocket.close()
                continue
            client = threading.Thread(target=serve, name='C'+str(clientID), args=(clientSocket, Address))
            client.start()
            clients.append(client)
            i += 1
    for c in clients:
        print(c)
        c.join()
    logUpdate(msg=f"SERVER CLOSED\n")
    s.close()
    sys.exit()
