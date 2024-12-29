import numpy as np

def string_to_matrix(key_string, n):
    """
    Converts a string into a numeric matrix for the Hill cipher key.
    """
    key_string = key_string.upper().replace(" ", "")
    key_values = [ord(char) - ord('A') for char in key_string]
    
    # Ensure the string length matches n^2
    if len(key_values) != n * n:
        return None  # Invalid key length
    key_matrix = np.array(key_values).reshape(n, n)
    return key_matrix

def is_invertible_mod26(matrix):
    """
    Checks if a matrix is invertible modulo 26.
    """
    determinant = int(round(np.linalg.det(matrix))) % 26
    gcd = np.gcd(determinant, 26)
    return gcd == 1

def hill_encrypt(text, key_matrix):
    """
    Encrypts the given text using the Hill cipher.
    """
    n = key_matrix.shape[0]

    # Pad text to be a multiple of the key size
    text = text.replace(" ", "").upper()
    while len(text) % n != 0:
        text += 'X'  # Padding with 'X'

    # Convert text to numerical values (A=0, B=1, ..., Z=25)
    text_vector = [ord(char) - ord('A') for char in text]
    text_matrix = np.array(text_vector).reshape(-1, n)

    # Perform matrix multiplication and modulo operation
    encrypted_matrix = (np.dot(text_matrix, key_matrix) % 26).astype(int)

    # Convert back to characters
    encrypted_text = ''.join(chr(num + ord('A')) for num in encrypted_matrix.flatten())
    return encrypted_text

def hill_decrypt(ciphertext, key_matrix):
    """
    Decrypts the given text encrypted using the Hill cipher.
    
    :param ciphertext: The encrypted text to decrypt.
    :param key_matrix: The encryption key as a square numeric matrix.
    :return: The decrypted text.
    """
    n = key_matrix.shape[0]
    
    # Calculate the inverse of the key matrix modulo 26
    determinant = int(round(np.linalg.det(key_matrix))) % 26
    determinant_inverse = pow(determinant, -1, 26)
    adjugate = np.round(determinant * np.linalg.inv(key_matrix)).astype(int) % 26
    inverse_key_matrix = (determinant_inverse * adjugate) % 26

    # Convert ciphertext to numerical values
    ciphertext_vector = [ord(char) - ord('A') for char in ciphertext]
    ciphertext_matrix = np.array(ciphertext_vector).reshape(-1, n)

    # Perform matrix multiplication and modulo operation
    decrypted_matrix = (np.dot(ciphertext_matrix, inverse_key_matrix) % 26).astype(int)

    # Convert back to characters
    decrypted_text = ''.join(chr(num + ord('A')) for num in decrypted_matrix.flatten())
    return decrypted_text

def get_cipher_key(block_size):

    # Validate key string input
    attempts = 0
    max_attempts = 3
    key_matrix = None

    while attempts < max_attempts:
        key_string = input(f"Enter a string to use as the key (length must be {block_size**2}): ")
        key_matrix = string_to_matrix(key_string, block_size)
        if key_matrix is not None:
            break
        else:
            print(f"Invalid key length. Please provide a string of length {block_size**2}.")
        attempts += 1

    if attempts == max_attempts:
        print("Maximum attempts reached. Exiting.")
        exit()

    if not is_invertible_mod26(key_matrix):
        print("The key matrix is not invertible modulo 26. Encryption cannot be used.")
        exit()

    print(f"Key matrix:\n{key_matrix}")
    return key_matrix

def get_plain_text(block_size):
    # Input plaintext
    while True:
        plaintext = input("Enter the plaintext: ").replace(" ", "").upper()
        key_length = block_size ** 2

        if len(plaintext) != key_length:
            response = input(
                f"The plaintext length ({len(plaintext)}) does not match the key length ({key_length}).\n"
                "This may make the encrypted text undecipherable. Do you want to re-enter the plaintext? (yes/no): "
            ).strip().lower()
            if response == "no":
                break
        else:
            break
    return plaintext

def get_cipher_text(block_size):
     # Input plaintext
    while True:
        ciphertext = input("Enter the ciphertext: ").replace(" ", "").upper()
        key_length = block_size ** 2

        if len(ciphertext) != key_length:
            response = input(
                f"The ciphertext length ({len(ciphertext)}) does not match the key length ({key_length}).\n"
                "This may make the lead to mistake. Do you want to re-enter the ciphertext? (yes/no): "
            ).strip().lower()
            if response == "no":
                break
        else:
            break
    return ciphertext

def encrypt_hill_cipher():
    while True:
        block_size = int(input("Enter the block size (n x n matrix): "))
        key_matrix = get_cipher_key(block_size)
        plaintext = get_plain_text(block_size)
        ciphertext = hill_encrypt(plaintext, key_matrix)
        print(f"Encrypted: {ciphertext}")
        option = input(("Do you want to continue (type 'yes' to continue or press anything to escape): "))
        if option == "yes":
            continue
        else:
            break
    
    
def decrypt_hill_cipher():
    while True:
        block_size = int(input("Enter the block size (n x n matrix): "))
        key_matrix = get_cipher_key(block_size)
        ciphertext = get_cipher_text(block_size)
        decrypted_text = hill_decrypt(ciphertext, key_matrix)
        print(f"Decrypted: {decrypted_text}")
        option = input(("Do you want to continue (type 'yes' to continue or press anything to escape): "))
        if option == "yes":
            continue
        else:
            break
    
    
    
# Main program for test
if __name__ == "__main__":
    block_size = int(input("Enter the block size (n x n matrix): "))

    # Validate key string input
    attempts = 0
    max_attempts = 3
    key_matrix = None

    while attempts < max_attempts:
        key_string = input(f"Enter a string to use as the key (length must be {block_size**2}): ")
        key_matrix = string_to_matrix(key_string, block_size)
        if key_matrix is not None:
            break
        else:
            print(f"Invalid key length. Please provide a string of length {block_size**2}.")
        attempts += 1

    if attempts == max_attempts:
        print("Maximum attempts reached. Exiting.")
        exit()

    if not is_invertible_mod26(key_matrix):
        print("The key matrix is not invertible modulo 26. Encryption cannot be used.")
        exit()

    print(f"Key matrix:\n{key_matrix}")

    # Input plaintext
    while True:
        plaintext = input("Enter the plaintext: ").replace(" ", "").upper()
        key_length = block_size ** 2

        if len(plaintext) != key_length:
            response = input(
                f"The plaintext length ({len(plaintext)}) does not match the key length ({key_length}).\n"
                "This may make the encrypted text undecipherable. Do you want to re-enter the plaintext? (yes/no): "
            ).strip().lower()
            if response == "no":
                break
        else:
            break

    ciphertext = hill_encrypt(plaintext, key_matrix)
    print(f"Encrypted: {ciphertext}")

    # Decrypt the ciphertext
    if is_invertible_mod26(key_matrix):
        decrypted_text = hill_decrypt(ciphertext, key_matrix)
        print(f"Decrypted: {decrypted_text}")
    else:
        print("The key matrix is not invertible modulo 26. Encrypted text cannot be decrypted.")
