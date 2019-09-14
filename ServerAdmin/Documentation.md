## Requests To Be Made And Responses To Be Expected

### `<` *Whatever Inside* `>` Is Processed By The Server

- `<exit>` - terminates connection
```
Request = {
  "uname": "USERNAME",
  "terminate": 1
}
```

- `<reqhn>` - requests hostname
```
Request = {
  "uname": " USERNAME",
  "hostname": 1
}
```
```
Response = {
  "hostname": "HOSTNAME"
}
```

- `<reqpubkey>` - requests public key
```
Request = {
  "uname": "USERNAME",
  "pubKey": 1
}
```
```
Response = {
  "pubKey": "PUBLICKEY"
}
```

### :star: Request/Response Operations Are Carried Out In JSON Format