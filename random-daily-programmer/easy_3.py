"""Program that encrypts, and decrypts texts with an alphabetical caesar cipher.
 It ignores numbers, and whitespace, and symbols
 The ASCII range of 97-122 is used for reference as to what symbols are valid"""


def bruteforce(ciphertext):
    print("This list contains all the possible shifts of the cipher-text.")
    for shift in range(1,27):
        plaintext = ""
        for x in ciphertext:
            if x.isalpha():
                x = x.lower()
                num = ord(x)
                num = num - shift
                if num < ord('a'):
                    num = num + 26
                plaintext = plaintext + str(chr(num))
            else:
                plaintext = plaintext + str(x)
        print("{0}. [{1}]".format(shift, plaintext))


def encrypt(plaintext, shift):
    #Encrypts the string with the caesar cipher
    ciphertxt = ""
    for x in plaintext:
        #Runs through isalpha to check if the var is an alpha char, changes it and appends it if so
        if x.isalpha():
            x = x.lower()
            num = ord(x)
            num = num + shift
            #If num is over the ASCII range then loop back to start of ASCII values
            if num > ord('z'):
                num = num - 26
            ciphertxt = ciphertxt + str(chr(num))
        #If not alpha char then just add the var
        else:
            ciphertxt = ciphertxt + str(x)
    return ciphertxt


def decrypt(ciphertext, shift):
    #Decrypts the string with the caesar cipher
    plaintext = ""
    for x in ciphertext:
        if x.isalpha():
            x = x.lower()
            num = ord(x)
            num = num - shift
            if num < ord('a'):
                num = num + 26
            plaintext = plaintext + str(chr(num))
        else:
            plaintext = plaintext + str(x)
    return plaintext


def main():
    #Ask the user if they want to encrypt or
    choice = str(input("Do you want to Decrypt, Encrypt, or Brute-Force: "))
    #Ask how much to shift the characters by
    shift = 0
    if choice[0] != 'b' and choice[0] != 'B':
        while 1 > shift or 26 < shift:
            try:
                shift = int(input("What is the shift of your cipher (1 - 26): "))
            except ValueError:
                print("Please input a valid integer")
    #Ask the user for their selected input and parse it to function, then printing it out
    plaintext = ""
    ciphertext = ""
    if choice[0] == 'D' or choice[0] == 'd':
        ciphertext = str(input("Input your ciphertext: "))
        plaintext = decrypt(ciphertext, shift)
        print("Your plaintext is [{0}]".format(plaintext))
    if choice[0] == 'E' or choice[0] == 'e':
        plaintext = str(input("Input your plaintext: "))
        ciphertext = encrypt(plaintext, shift)
        print("Your ciphertext is [{0}]".format(ciphertext))
    if choice[0] == 'B' or choice[0] == 'b':
        ciphertext = str(input("Input your ciphertext: "))
        plaintext = bruteforce(ciphertext)

main()