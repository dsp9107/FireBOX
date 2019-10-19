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
    # Authentication
    uname = str(input("Username: "))
    secret = getpass.getpass()
    password = hashlib.sha3_512(bytes(str(secret), "utf-8")).hexdigest()

    # Build Message
    mess = config['sensitive']['login']
    mess['uname'] = uname
    mess['pwd'] = password
    s.send(jt.pack(jt.prep(mess, "sensitive"), config['headerSize']))
    hn = s.recv(1024)
    if jt.unpack(hn, config['headerSize'])['messageContent'] == "Invalid User Details" :
        print("INVALID USER DETAILS")
        sys.exit()
    else :
        print(f"\nConnection With {host} Has Been Established")
        print("SERVER ~ " + jt.unpack(hn, config['headerSize'])['messageContent'])

    while True:
        mess = str(input("SERVER : "))

        # Request To Disconnect
        if mess == "<exit>" :
            mess = config['reqtype']
            mess['terminate'] = 1
            s.send(jt.pack(jt.prep(mess, "request"), config['headerSize']))
            break

        # Request Server's Public Key
        elif mess == "<reqpk>" :
            mess = config['reqtype']
            mess['pubKey'] = 1
            s.send(jt.pack(jt.prep(mess, "request"), config['headerSize']))
            # Wait For Server To Respond
            hn = s.recv(1024)
            s_pubkey = jt.unpack(hn, config['headerSize'])['messageContent']
            print("SERVER ~ " + s_pubkey)

        # Else, Send Message To Server
        else :
            s.send(jt.pack(jt.prep(mess), config['headerSize']))

        # Reset Request Flags
        config['reqtype'] = {i : 0 for i in config['reqtype']}
            
    print(f"Connection With {host} Has Been Terminated")

sys.exit()
