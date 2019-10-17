import hashlib

# Hashing Phase 1

x = "chigfy"
xash = hashlib.sha3_512(bytes(str(x), "utf-8")).hexdigest()
print(xash)

y = xash

# Priyam's Algo

yascii = ""
for ys in y:
    yascii += str(ord(ys))
print(yascii)
yascii = yascii.replace("0","")

z = ""

for i in range(len(yascii)-1,0,-1):
    z+=str(int(yascii)%int(yascii[i:]))

print(z)

# Hashing Phase 2

zash = hashlib.sha3_512(bytes(z, "utf-8")).hexdigest()

print(zash)
