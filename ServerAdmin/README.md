# How To Communicate With Server

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

### :star: Example :star:

To Send
```
text = "HELLO"
package = jt.prep(text)
payload = jt.pack(package, config['headerSize'])
ServerSocket.send(payload)
```
To Receive
```
payload = ClientSocket.recv(1024)
message = jt.unpack(payload, config['headerSize'])
```
To Open

- `message['messageType']` : Type of Message
- `message['messageContent']` : Content of Message
