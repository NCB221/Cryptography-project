from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def get_key():
    attempt = 0
    maximum_attempt = 3
    # Key must be 16, 24, or 32 bytes long
    key = input("Enter a key (16, 24, or 32 characters): ").encode()
    if len(key) not in [16, 24, 32]:
        print("The key must be exactly 16, 24, or 32 characters long!")
        exit()
    return key

def aes_encrypt(plaintext, key):
    """
    Encrypts the plaintext using AES encryption.
    """
    # Generate a random IV (Initialization Vector)
    iv = get_random_bytes(AES.block_size)
    
    # Create a new AES cipher object in CBC mode
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Pad the plaintext to be a multiple of AES block size (16 bytes)
    padded_text = pad(plaintext.encode(), AES.block_size)
    
    # Encrypt the plaintext
    ciphertext = cipher.encrypt(padded_text)
    
    return ciphertext.hex(), iv.hex()

def aes_decrypt(ciphertext, key, iv):
    """
    Decrypts the ciphertext using AES decryption.
    """
    # Convert the ciphertext and IV from hex to bytes
    ciphertext_bytes = bytes.fromhex(ciphertext)
    iv_bytes = bytes.fromhex(iv)
    
    # Create a new AES cipher object in CBC mode
    cipher = AES.new(key, AES.MODE_CBC, iv_bytes)
    
    # Decrypt and unpad the ciphertext
    decrypted_text = unpad(cipher.decrypt(ciphertext_bytes), AES.block_size)
    
    return decrypted_text.decode()

def encrypt_aes():
    while True:
    # Input plaintext
        plaintext = input("Enter the plaintext to encrypt: ")
        key = get_key()
        ciphertext, iv = aes_encrypt(plaintext, key)
        print(f"Encrypted text (hex): {ciphertext}")
        print(f"IV (hex): {iv}")
        print("Save this carefully for decryption.")
        option = input(("Do you want to continue (type 'yes' to continue or press anything to escape): "))
        if option == "yes":
            continue
        else:
            break
    
def decrypt_aes():
    while True:
    # Decrypt the ciphertext
        ciphertext = input("Enter the cipher text to encrypt: ")
        key = get_key()
        iv = input("Enter Initialization Vector (IV) to encrypt: ")
        decrypted_text = aes_decrypt(ciphertext, key, iv)
        print(f"Decrypted text: {decrypted_text}")
        option = input(("Do you want to continue (type 'yes' to continue or press anything to escape): "))
        if option == "yes":
            continue
        else:
            break


# Main program for test
if __name__ == "__main__":
    
     # Key must be 16, 24, or 32 bytes long
    key = input("Enter a key (16, 24, or 32 characters): ").encode()
    if len(key) not in [16, 24, 32]:
        print("The key must be exactly 16, 24, or 32 characters long!")
        exit()

    # Input plaintext
    plaintext = input("Enter the plaintext to encrypt: ")
    
    # Encrypt the plaintext
    ciphertext, iv = aes_encrypt(plaintext, key)
    print(f"Encrypted text (hex): {ciphertext}")
    print(f"IV (hex): {iv}")
    
    # Decrypt the ciphertext
    decrypted_text = aes_decrypt(ciphertext, key, iv)
    print(f"Decrypted text: {decrypted_text}")
