from math import gcd
def RSA(p:int,q:int):
    n=p*q
    t=(p-1)*(q-1)
    for i in range(n):
        if gcd(i,t)==1:
            e=i 
            break
    j=0
    while True:
        if (j*e)%t ==1:
            d=j
            break
        j+=1
    message=input("Enter the message: ")
    if message.isdigit():
        encrypted=(message**e)%n
        decrypted=(message**d)%n
        print("Encrypted message is ",encrypted)
        print("Decrypted message is ",decrypted)
    else:
        ascii_mes=[ord(char) for char in message]
        encrypted=[(char**e)%n for char in ascii_mes]
        decrypted=''.join([chr((char**d)%n) for char in encrypted])
        print("Encrypted message is ",encrypted)
        print("Decrypted message is ",decrypted)
    
print("Testcase 1")
RSA(p=43,q=64)
