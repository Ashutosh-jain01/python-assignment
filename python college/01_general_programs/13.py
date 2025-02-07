 #Convert bytes into KB, MB and GB.
# 1kb = 1000 bytes in decimal
# 1mb = 1000,000 bytes in decimal
# 1gb = 1000,000,000 bytes in decimal

def kb():
    bytes = int(input("enter any no. of bytes:"))

    print(f"{bytes} bytes in kb is {bytes/1000}")

def mb():
    bytes = int(input("enter any no. of bytes:"))

    print(f"{bytes} bytes in mb is {bytes/1000000}")

def gb():
    bytes = int(input("enter any no. of bytes:"))

    print(f"{bytes}bytesin gb is {bytes/1000000000}")

kb()
mb()
gb()