import Caesar_Cipher

def getPlainText():
    plaintext = input("Enter plain text: ")
    return plaintext

def getShift():
    shift = int(input("Enter shift: "))
    return shift

def main():
    #plaintext = getPlainText()
    shift = getShift()
    plaintext = getPlainText()
    result = Caesar_Cipher.caesar_encrypt(plaintext, shift)
    print("Encrypted text is: "+ result)
    
if __name__ == "__main__":
    main()


