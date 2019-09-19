import json
import socket
import jsontransport as jt

def main():
    global config, pubKey, s
    with open("config.json", "r") as read_file:
        config = json.load(read_file)

    pubKey = "pK-ub-E-li-Yc"

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if __name__ == '__main__' :
    main()

s.bind(('localhost', 1237))
s.listen(5)

while True:
    ClientSocket, Address = s.accept()
    print(f"\nConnection From {Address} Has Been Established")
    ClientSocket.send(jt.pack(jt.prep("Welcome, Client"), config['HEADERSIZE']))

    while True:
        message = jt.unpack(ClientSocket.recv(1024), config['HEADERSIZE'])
        
        if message['messageType'] == "request" :
            
            if message['messageContent']['terminate'] :
                print("CLIENT : <exiting>")
                break
            
            elif message['messageContent']['hostname'] :
                print("CLIENT : <requesting hostname>")
                ClientSocket.send(jt.pack(jt.prep(socket.gethostname()), config['HEADERSIZE']))

            elif message['messageContent']['pubKey'] :
                print("CLIENT : <requesting publicKey>")    
                ClientSocket.send(jt.pack(jt.prep(pubKey), config['HEADERSIZE']))

        elif message['messageType'] == "message" :
            print("CLIENT : " + message['messageContent'])
            
    print(f"Connection From {Address} Has Been Lost")
