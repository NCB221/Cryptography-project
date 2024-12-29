from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import os

def get_key():
    attempts = 0
    max_attempts = 3
    
    while attempts < max_attempts:
        # Key must be 8 bytes long
        key = input("Enter an 8-character key: ").encode()
        if len(key) == 8:
            break
        else:
            print("The key must be exactly 8 characters long!")
        attempts+=1
    
    if attempts == 3: 
        print("Maximum attempts reached. Exiting.")
        exit()
    return key

def des_encrypt(plaintext, key):
    """
    Encrypts the plaintext using DES encryption.
    
    :param plaintext: The input text to encrypt.
    :param key: The encryption key (must be 8 bytes).
    :return: The encrypted ciphertext in hexadecimal format.
    """
    # Create a new DES cipher object
    cipher = DES.new(key, DES.MODE_ECB)
    
    # Pad the plaintext to be a multiple of 8 bytes
    padded_text = pad(plaintext.encode(), DES.block_size)
    
    # Encrypt the plaintext
    ciphertext = cipher.encrypt(padded_text)
    
    return ciphertext.hex()

def des_decrypt(ciphertext, key):
    """
    Decrypts the ciphertext using DES decryption.
    
    :param ciphertext: The encrypted text in hexadecimal format.
    :param key: The decryption key (must be 8 bytes).
    :return: The decrypted plaintext.
    """
    # Create a new DES cipher object
    cipher = DES.new(key, DES.MODE_ECB)
    
    # Convert the ciphertext from hex to bytes
    ciphertext_bytes = bytes.fromhex(ciphertext)
    
    # Decrypt and unpad the ciphertext
    decrypted_text = unpad(cipher.decrypt(ciphertext_bytes), DES.block_size)
    
    return decrypted_text.decode()

def encrypt_des():
    while True:
        plaintext = input("Enter the plaintext to encrypt: ")
        key = get_key()
        ciphertext = des_encrypt(plaintext, key)
        print(f"Encrypted text (hex): {ciphertext}")
        option = input(("Do you want to continue (type 'yes' to continue or press anything to escape): "))
        if option == "yes":
            continue
        else:
            break
    
def decrypt_des():
    while True:
        ciphertext = input("Enter cipher text to decrypt: ")
        key = get_key()
        decrypted_text = des_decrypt(ciphertext, key)
        print(f"Decrypted text: {decrypted_text}")
        option = input(("Do you want to continue (type 'yes' to continue or press anything to escape): "))
        if option == "yes":
            continue
        else:
            break
    
# Main program for test
if __name__ == "__main__":
    
    attempts = 0
    max_attempts = 3
    
    while attempts < max_attempts:
        # Key must be 8 bytes long
        key = input("Enter an 8-character key: ").encode()
        if len(key) == 8:
            break
        else:
            print("The key must be exactly 8 characters long!")
        attempts+=1
    
    if attempts == 3: 
        print("Maximum attempts reached. Exiting.")
        exit()
    # Input plaintext
    plaintext = input("Enter the plaintext to encrypt: ")
    
    # Encrypt the plaintext
    ciphertext = des_encrypt(plaintext, key)
    print(f"Encrypted text (hex): {ciphertext}")
    
    # Decrypt the ciphertext
    decrypted_text = des_decrypt(ciphertext, key)
    print(f"Decrypted text: {decrypted_text}")
