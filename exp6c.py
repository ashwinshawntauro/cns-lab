import numpy as np

def text_to_vector(text):
    return [ord(ch)-ord('A') for ch in text]

def matrix_mod_mult(A,B,mod):
    return np.dot(A,B)%mod

def vector_to_text(vector):
    return ''.join(chr(num +ord('A')) for num in vector)

def pad_text(text,blocksize):
    padding= (blocksize-len(text)%blocksize)%blocksize
    return text+'X'*padding

def unpad_text(text):
    return text.rstrip('X')

def matrix_mod_inv(matrix,mod):
    det=int(np.round(np.linalg.det(matrix)))
    det_inv=pow(det,-1,mod)
    matrix_mod_inv=(
        det_inv*np.round(det*np.linalg.inv(matrix)).astype(int)%mod
    )
    return matrix_mod_inv%mod

def encrypt_mes(text,key_matrix):
    n=key_matrix.shape[0]
    padded_text=pad_text(text.upper().replace(' ',''),n)
    cipher_text=''
    for i in range(0,len(padded_text),n):
        block=text_to_vector(padded_text[i:i+n])
        block_vector=np.array(block).reshape(n,1)
        cipher_vector=matrix_mod_mult(key_matrix,block_vector,26).flatten()
        cipher_text+=vector_to_text(cipher_vector)
    return cipher_text

def decrypt_mes(text,key_matrix):
    n=key_matrix.shape[0]
    inverse_key_matrix=matrix_mod_inv(key_matrix,26)
    plain_text=''
    for i in range(0,len(text),n):
        block=text_to_vector(plain_text[i:i+n])
        block_vector=np.array(block).reshape(n,1)
        plaintext_vector=matrix_mod_mult(inverse_key_matrix,block_vector,26).flatten()
        plain_text+=vector_to_text(plaintext_vector)
    return unpad_text(plain_text)

if __name__ == "__main__":
    key_matrix=np.array([
        [1,2,4],
        [4,7,2],
        [6,8,9]
    ])
    text=input("Enter text message: ")
    encrypted_message=encrypt_mes(text,key_matrix)
    decrypted_message=decrypt_mes(encrypted_message,key_matrix)
    print("Encrypted Message: ",encrypted_message)
    print("Decrypted Message: ",decrypted_message)