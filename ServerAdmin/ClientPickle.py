import sys
import json
import socket
import hashlib
import getpass
import jsontransport as jt

def main():
    global config, host, s

    with open("config.json", "r") as read_file:
        config = json.load(read_file)

    config['reqtype'] = {i : 0 for i in config['reqtype']}
    host = socket.gethostname()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if __name__ == '__main__' :
    main()

try :
    # Try Connecting With Server
    s.connect((host, config['port']))

except ConnectionRefusedError :
    # If Connection Refused
    print("Server's Offline")

else :
    while True:
        op = str(input("[l]ogin or [r]egister ? "))

        # Authentication
        if op == 'l':
            uname = str(input("Username: "))
            secret = getpass.getpass()
            password = hashlib.sha3_512(bytes(str(secret), "utf-8")).hexdigest()

            # Build Message
            mess = config['sensitive']['credentials']
            mess['uname'] = uname
            mess['pwd'] = password
            s.send(jt.pack(jt.prep(mess, "login"), config['headerSize']))
            hn = s.recv(1024)

            # Decision Making
            if jt.unpack(hn, config['headerSize'])['messageContent'] == "Invalid User Details" :
                print("INVALID USER DETAILS")
                continue
            else :
                print(f"\nConnection With {host} Has Been Established")
                print("SERVER ~ " + jt.unpack(hn, config['headerSize'])['messageContent'])
                break

        # Registration
        elif op == 'r':
            uname = str(input("Username: "))
            secret = getpass.getpass()
            password = hashlib.sha3_512(bytes(str(secret), "utf-8")).hexdigest()

            # Build Message
            mess = config['sensitive']['credentials']
            mess['uname'] = uname
            mess['pwd'] = password
            s.send(jt.pack(jt.prep(mess, "register"), config['headerSize']))
            hn = s.recv(1024)

            # Decision Making
            if jt.unpack(hn, config['headerSize'])['messageContent'] == "Registration Successful" :
                print("Registered Successfully")
                print("Application Will Now Exit")
            else :
                print("Could Not Register")
            sys.exit()

    while True:
        mess = str(input("SERVER : "))
        ty = "request"

        # Disconnection Request
        if mess == "<exit>" :
            mess = {"terminate": 1}
            s.send(jt.pack(jt.prep(mess, "request"), config['headerSize']))
            break

        # Other Requests
        else :
            # Request Curious Chigfy To Start
            if mess == "<chigfy-start>" :
                mess = {"curiosity": 1}

            # Request Curious Chigfy To Stop
            elif mess == "<chigfy-stop>" :
                mess = {"curiosity": 0}

            # If Just A Message
            else :
                ty = "message"

            s.send(jt.pack(jt.prep(mess, ty), config['headerSize']))
            
    print(f"Connection With {host} Has Been Terminated")

sys.exit()
