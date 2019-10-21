import os
import sys
import json
import socket
import jsontransport as jt
import threeHash as th
from datetime import datetime

def main():
    global config, pubKey, s, failed
    with open("config.json", "r") as read_file:
        config = json.load(read_file)

    #pubKey = "pK-ub-E-li-Yc"
    failed = 0

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

if __name__ == '__main__' :
    main()

while True:
    # Check For Failed Attempts At Login
    if failed > 2 :
        logUpdate(msg="SERVER CLOSED DUE TO MULTIPLE FAILED LOGIN ATTEMPTS\n")
        print("SERVER CLOSED DUE TO MULTIPLE FAILED LOGIN ATTEMPTS")
        sys.exit()

    try :
        # Try Accepting Client's Connection Request
        ClientSocket, Address = s.accept()
        
    except socket.timeout :
        # If Socket Times Out
        logUpdate(msg="SERVER CLOSED DUE TO INACTIVITY\n")
        print("SERVER CLOSED DUE TO INACTIVITY")
        ClientSocket.close()
        sys.exit()
        
    else :
        # When Connected
        message = jt.unpack(ClientSocket.recv(1024), config['headerSize'])

        # If Message Is Login Request
        if message['messageType'] == "login" :
            user = {"uname": "", "pwd": ""}
            user['uname'] = message['messageContent']['uname']
            user['pwd'] = th.threeHash(message['messageContent']['pwd'])
            # Load DB
            with open("users.json", "r") as read_file :
                users = json.load(read_file)
            # If User Registered
            if user['uname'] in users :
                # If Passwords Match
                if user['pwd'] == users[user['uname']] :
                    # Acknowledge
                    ClientSocket.send(jt.pack(jt.prep(f"Welcome, {user['uname']}"), config['headerSize']))
                    print(f"\nConnection From {Address} Has Been Established")
                else :
                    ClientSocket.send(jt.pack(jt.prep("Invalid User Details"), config['headerSize']))
                    failed += 1
                    print(f"Failed Attempt : {failed}")
                    logUpdate(msg=f"{user['uname']} : Failed Login Attempt")
                    ClientSocket.close()
                    continue
            else :
                ClientSocket.send(jt.pack(jt.prep("Invalid User Details"), config['headerSize']))
                continue

        # If Message Is Registration Request
        elif message['messageType'] == "register" :
            user = {"uname": "", "pwd": ""}
            user['uname'] = message['messageContent']['uname']
            user['pwd'] = th.threeHash(message['messageContent']['pwd'])
            # Load DB
            with open("users.json", "r") as read_file :
                users = json.load(read_file)
            users[user['uname']] = user['pwd']
            # Update DB
            with open("users.json", "w") as write_file :
                json.dump(users, write_file)
            # Acknowledge
            ClientSocket.send(jt.pack(jt.prep("Registration Successful"), config['headerSize']))
            logUpdate(msg=f"{user['uname']} Has Been Registered")
            print(f"{user['uname']} Has Registered")
            ClientSocket.close()
            continue

        # If First Message Is Anything Else, Drop Connection
        else :
            ClientSocket.close()
            continue

        # Serve
        while True:
            # Receive Message
            message = jt.unpack(ClientSocket.recv(1024), config['headerSize'])

            # Log Message
            logUpdate(ip=Address[0], port=Address[1], user=user['uname'], msgtype=message['messageType'], msglen=message['messageLength'], msgcontent=message['messageContent'])

            # If Client Sends A Request
            if message['messageType'] == "request" :
                # If Client Requests To Disconnect
                if message['messageContent']['terminate'] :
                    print(f"{user['uname']} : <exiting>")
                    break

                # If Client Requests Public Key
                elif message['messageContent']['pubKey'] :
                    print(f"{user['uname']} : <requesting publicKey>")
                    # Send Public Key
                    ClientSocket.send(jt.pack(jt.prep(pubKey), config['headerSize']))

            # If Client Sends A Message
            elif message['messageType'] == "message" :
                print(f"{user['uname']} : " + message['messageContent'])

        logUpdate(msg=f"{user['uname']} Disconnected From {Address}")
        print(f"{user['uname']} Has Left")
