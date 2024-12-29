def getPlainText():
    plaintext = input("Enter plain text: ")
    return plaintext

def getEncryptedText():
    encryptedtext = input("Enter encrypted text: ")
    return encryptedtext

def getShift():
    shift = int(input("Enter shift: "))
    return shift

def caesar_encrypt(text, shift):
    """
    Encrypts the given text using the Caesar cipher.
    """
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Only encrypt alphabetic characters
            shift_base = 65 if char.isupper() else 97  # ASCII value of 'A' or 'a'
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char  # Non-alphabetic characters remain unchanged
    return encrypted_text

def caesar_decrypt(text, shift):
    """
    Decrypts the given text encrypted using the Caesar cipher.
    """
    return caesar_encrypt(text, -shift)

def encrypt_caesar_cipher():
    while True:
        plaintext = getPlainText()
        shift = getShift()
        print(f"Encrypted message: {caesar_encrypt(plaintext, shift)}")
        option = input(("Do you want to continue (type 'yes' to continue or press anything to escape): "))
        if option == "yes":
            continue
        else:
            break
    
def decrypt_caesar_cipher():
    while True:
        text = getEncryptedText()
        shift = getShift()
        print(f"Decrypted message: {caesar_decrypt(text, shift)}")
        option = input(("Do you want to continue (type 'yes' to continue or press anything to escape): "))
        if option == "yes":
            continue
        else:
            break