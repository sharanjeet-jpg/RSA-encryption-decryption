print("*" * 50)
print("**   RRR      SSS     AAA                             ***")
print("**   R  R    S       A   A                            ***")
print("**   RRR      SSS    AAAAA                            ***")
print("**   R  R        S   A   A                            ***")
print("**   R  R    SSSS    A   A   encryption/decryption    ***")
print("*" * 50)


p = int(input("\nEnter the first prime number (p): "))
q = int(input("Enter the second prime number (q): "))
n = p * q
phi = (p - 1) * (q - 1)

x = int(input("Encryption key press 1 or Decryption key press 2: "))
if x == 1:
    e = int(input("Encryption key value: "))
    print("Let's Find Decryption Key:------------- ")
    t = 0
    tt = 1
    r = phi
    rr = e
    while rr != 0:
        g = r % rr
        q = r // rr
        f = t - (q * tt)
        r = rr
        rr = g
        t = tt
        tt = f
    if (t * e) % phi == 1:
        print(f"Decryption key is: {t}",)
    else:
        print("Does not exist")

if x == 2:
    d = int(input("Decryption key value: "))
    print("Let's Find Encryption Key:------------- ")
    t = 0
    tt = 1
    r = phi
    rr = d
    while rr != 0:
        g = r % rr
        q = r // rr
        f = t - (q * tt)
        r = rr
        rr = g
        t = tt
        tt = f
    if (t * d) % phi == 1:
        print(f"Encryption key is: {t}")
    else:
        print("Does not exist")

print("Choose: ")
print("1. Encryption")
print("2. Decryption")
value = int(input("Choice: "))
result = 0

if value == 1:
    e = int(input("Enter Encryption key value: "))
    pt = int(input("Enter the value: "))
    ct = 1
    while e != 0:
        ct = (ct * pt) % n
        e -= 1
    result = ct

elif value == 2:
    d = int(input("Enter Decryption key value: "))
    ct = int(input("Enter the value: "))
    pt = 1
    while d != 0:
        pt = (pt * ct) % n
        d -= 1
    result = pt

print(f"Cipher Text is: {result}")
