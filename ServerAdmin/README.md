# How To Communicate With Server

### Usage

First, Prepare The Message `text` By Calling `prep(text)` -
```
prep(string text, string typ="message"):
    package = {
        "messageType": str(typ),
    	"messageLength": len(text),
    	"messageContent": text
    }
    return package
```
Then, You Need To Pack The `package` In A Proper Format Using `pack()` -
```
pack(dictionary package, integer HEADERSIZE, string ENCODING = 'utf-8'):
    payload = json.dumps(package)
    payload = bytes(str(len(payload)).ljust(HEADERSIZE), ENCODING) + pickle.dumps(payload)
    return payload
```
The `payload` Can Then Be Sent Using [`socket.send()`](https://docs.python.org/3/library/socket.html#socket.socket.send)

Similarly, The `payload` Recieved Via [`socket.recv()`](https://docs.python.org/3/library/socket.html#socket.socket.recv) Can Be Opened Up Using `unpack()` -
```
unpack(payload, integer HEADERSIZE, string ENCODING = 'utf-8'):
    msg = pickle.loads(payload[HEADERSIZE:])
    msg = json.loads(msg)
    return msg
```

#### To Send Message

Client
```
text = "HELLO"
package = jt.prep(text, "message")
payload = jt.pack(package, config['headerSize'])
ServerSocket.send(payload)
```

Server
```
payload = ClientSocket.recv(1024)
message = jt.unpack(payload, config['headerSize'])
```

Elements

- `message['messageType']` : Message
- `message['messageContent']` : Content of Message

#### To Send Request - Disconnect 

Client
```
request = {
  "terminate": 1
}
package = jt.prep(request, "request")
payload = jt.pack(package, config['headerSize'])
ServerSocket.send(payload)
```

Server
```
payload = ClientSocket.recv(1024)
message = jt.unpack(payload, config['headerSize'])
if message['messageContent']['terminate'] :
    # Disconnect User
```

Elements

- `message['messageType']` : Request
- `message['messageContent']` : Content of Request
- `message['messageContent']['terminate']` : Termination Status

#### To Send Request - Login 

Client
```
request = {
    "uname": "user123",
    "pwd": hash("pass123")
}
package = jt.prep(request, "login")
payload = jt.pack(package, config['headerSize'])
ServerSocket.send(payload)
```

Server
```
payload = ClientSocket.recv(1024)
message = jt.unpack(payload, config['headerSize'])
if message['messageType'] == "login" :
    # Check If User Exists
    # Authenticate
```

Elements

- `message['messageType']` : Login Request
- `message['messageContent']` : Content of Request
- `message['messageContent']['uname']` : Username
- `message['messageContent']['pwd']` : Password

#### To Send Request - Register 

Client
```
request = {
    "uname": "user123",
    "pwd": hash("pass123")
}
package = jt.prep(request, "register")
payload = jt.pack(package, config['headerSize'])
ServerSocket.send(payload)
```

Server
```
payload = ClientSocket.recv(1024)
message = jt.unpack(payload, config['headerSize'])
if message['messageType'] == "register" :
    user = {"uname": "", "pwd": ""}
    user['uname'] = message['messageContent']['uname']
    user['pwd'] = hash(message['messageContent']['pwd'])
    # Update Database
    # Authorise
```

Elements

- `message['messageType']` : Registration Request
- `message['messageContent']` : Content of Request
- `message['messageContent']['uname']` : Username
- `message['messageContent']['pwd']` : Password
