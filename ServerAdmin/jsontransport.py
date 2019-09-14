import json
import pickle

def prep(msg, typ="message"):
    package = {
	"messageType": str(typ),
	"messageLength": len(msg),
	"messageContent": msg
    }
    return package

def pack(msg, HEADERSIZE, ENCODING = 'utf-8'):
    payload = json.dumps(msg)
    payload = bytes(str(len(payload)).ljust(HEADERSIZE), ENCODING) + pickle.dumps(payload)
    return payload

def unpack(payload, HEADERSIZE, ENCODING = 'utf-8'):
    msg = pickle.loads(payload[HEADERSIZE:])
    msg = json.loads(msg)
    return msg
