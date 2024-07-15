def caesar_encrypt(text,shift):
    result=""
    for char in text:
        if char.isalpha():
            shift_base=ord('A') if char.isupper() else ord('a')
            result+=chr((ord(char)-shift_base +shift)%26 +shift_base)
        else:
            result+=char
    return result
    
def ceaser_decrypt(text,shift):
    return caesar_encrypt(text,-shift)

if __name__=='__main__':
    text=input("Enter the text: ")
    shift=int(input("Enter shift bit: "))
    encrypted_text=caesar_encrypt(text,shift)
    print("Encrypted Text: ",encrypted_text)
    decrypted_text=ceaser_decrypt(encrypted_text,shift)
    print("Decrypted Text: ",decrypted_text)