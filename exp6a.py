def encrypt(text,shift):
    result=""
    for char in text:
        if char.isalpha():
            shift_base=ord('A') if char.isupper() else ord('a')
            result+=chr((ord(char)-shift_base+shift)%26+shift_base)
        else:
            result+=char

def decrypt(text,shift):
    return encrypt(text,-shift)

if __name__=="__main__":
    text = input("Enter text to encrypt: ")
    shift = int(input("Enter shift value: "))
    encrypted=encrypt(text,shift)
    decrypted=decrypt(text,shift)
    print('encrrypted: ',encrrypted)
    print('decrrypted: ',decrrypted)