import random

def main():
    passwords = int(input("How many passwords would you like to generate: "))
    length = int(input("How long should the passwords be: "))
    for x in range(passwords):
        password = random.sample("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-=][",length)
        print("".join(password))
main()

"""
This generates an insecure password
The passwords should be considered insecure due to how the sample function of random works
Once a letter has been chosen from the sample into the password variable then that particular letter can't be used again
while generating that password variable.
Hence its impossible to generate a password length outside of the random.sample length
passwords are actually insecure because the sample function doesn't reuse its sample, once a letter has been used
"""