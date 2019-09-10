# To Be Run After ServerSide.py

from jsonsocket import Client
import time

host = '192.168.1.3'
port = 8080

i=0
while True:
    client = Client()
    client.connect(host, port).send({'test':++i})
    response = client.recv()
    print(response)
    client.close()
    time.sleep(1)
 
