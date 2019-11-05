import json

def prep(msg, typ="message"):
    package = {
	"messageType": str(typ),
	"messageLength": len(msg),
	"messageContent": msg
    }
    return package

def pack(msg, HEADERSIZE = 10, ENCODING = 'utf-8'):
    payload = json.dumps(msg)
    payload = bytes(str(len(payload)).ljust(HEADERSIZE) + payload , ENCODING)
    return payload

def unpack(payload, HEADERSIZE = 10, ENCODING = 'utf-8'):
    msg = ""
    if payload[0] == 91 :
        payload = payload.decode()
        payload = payload.replace("\n","")
        payload = json.loads(payload)
        for i in payload:
            msg += chr(i)
    else :
        msg = payload.decode()
    msg = msg[HEADERSIZE:]
    msg = json.loads(msg)
    return msg
