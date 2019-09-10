# To Be Run Before ServerClient.py

from jsonsocket import Server

host = '0.0.0.0'
port = 8080

server = Server(host, port)

while True:
    server.accept()
    data = server.recv()
    server.send({"response":data})

server.close()
