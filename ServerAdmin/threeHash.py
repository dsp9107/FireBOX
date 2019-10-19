import hashlib

def threeHash(xash):
    # ASCII Conversion
    yascii = ""
    
    for y in xash:
        yascii += str(ord(y))

    yascii = yascii.replace("0","9")

    # Priyam's Algo
    z = ""

    for i in range(len(yascii)-1,0,-1):
        z+=str(int(yascii)%int(yascii[i:]))

    # Hashing

    zash = hashlib.sha3_512(bytes(z, "utf-8")).hexdigest()

    return zash
