import string
import random
def generate_substituion():
    letters=list(string.ascii_uppercase)
    shuffled_letters=letters[:]
    random.shuffle(shuffled_letters)
    return dict(zip(letters,shuffled_letters))

def sub_encrypt(text,key):
    result=''
    for char in text:
        if char in key:
            result+=key[char]
        else:
            result+=char
    return result

def sub_decrypt(text,key):
    result=''
    reveresed_key={v:k for k,v in key.items()}
    for char in text:
        if char in key:
            result+=reveresed_key[char]
        else:
            result+=char
    return result

if __name__ =="__main__":
    text=input("Enter the text: ")
    key=generate_substituion()
    encrypted_text=sub_encrypt(text,key)
    print("Encrypted Text: ",encrypted_text,key)
    decrypted_text=sub_decrypt(text,key)
    print("Decrypted Text: ",decrypted_text)