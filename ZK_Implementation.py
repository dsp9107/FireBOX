import hashlib
import base64

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

# FireBOX

wifi_ssid = 'default'
wifi_pwd = 'default'

def update(ssid,p1):
    global wifi_ssid, wifi_pwd
    wifi_ssid = ssid
    wifi_pwd = p1

def connect(ssid,p1):
    global wifi_pwd
    connect = True if (p1 == wifi_pwd) else False
    return connect

# FireBOX App

wifi_ssid = 'default'
wifi_p1 = 'default'

def gen_key(p2):
    salt = wifi_ssid.encode()
    kdf = PBKDF2HMAC(
        algorithm = hashes.SHA256(),
        length = 32,
        salt = salt,
        iterations = 100000,
        backend = default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(p2.encode()))
    return key

def register(uname, p2):
    global wifi_ssid, wifi_p1
    wifi_ssid = 'FIREBOX13'
    wifi_p1 = hashlib.md5(p2.encode())        #p1=hash(p2)
    update(wifi_ssid, wifi_p1.digest())
    f = Fernet(gen_key(p2))
    wifi_p1 = f.encrypt(wifi_p1.digest())     #p1=encrypt(p1,p2)
    return True

def authenticate(uname, p2):
    global wifi_ssid, wifi_p1
    wifi_ssid = 'FIREBOX13'
    f = Fernet(gen_key(p2))
    wifi_p1 = f.decrypt(wifi_p1)              #p1=decrypt(p1,p2)
    if(connect(wifi_ssid, wifi_p1)):
        return True
    else:
        return False

# User's Actions

print("\nRegister\n")
uname = input('Enter Your Username - ')
pwd = input('Create Your Password - ')

if(register(uname, pwd)):
    print("\nRegistration Successful\n\nLogin\n")
    uname = input('Username - ')
    pwd = input('Password - ')
    if(authenticate(uname, pwd)):
        print("\nConnected Successfully")
    else:
        print("\nIncorrect Password")
else:
    print("Registration Failed")

pwd = hashlib.md5("FIREBOX".encode())
