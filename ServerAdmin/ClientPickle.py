import sys
import json
import socket
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
    s.connect((host, config['port']))

except ConnectionRefusedError :
    print("Server's Offline")

else :
    print(f"\nConnection With {host} Has Been Established")

    message = jt.unpack(s.recv(1024), config['headerSize'])['messageContent']
    print("SERVER ~ " + message)

    while True:
        mess = str(input("SERVER : "))

        if mess == "<reqhn>" :
            mess = config['reqtype']
            mess['hostname']=1
            s.send(jt.pack(jt.prep(mess, "request"), config['headerSize']))
            hn = s.recv(1024)
            print("SERVER ~ " + jt.unpack(hn, config['headerSize'])['messageContent'])

        elif mess == "<reqpk>" :
            mess = config['reqtype']
            mess['pubKey']=1
            s.send(jt.pack(jt.prep(mess, "request"), config['headerSize']))
            hn = s.recv(1024)
            print("SERVER ~ " + jt.unpack(hn, config['headerSize'])['messageContent'])

        elif mess == "<exit>" :
            mess = config['reqtype']
            mess['terminate']=1
            s.send(jt.pack(jt.prep(mess, "request"), config['headerSize']))
            break

        else :
            s.send(jt.pack(jt.prep(mess), config['headerSize']))

        config['reqtype'] = {i : 0 for i in config['reqtype']}
            
    print(f"Connection With {host} Has Been Terminated")

sys.exit()
