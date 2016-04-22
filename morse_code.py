"""
This will encode and decode morse code containing symbols A-Z and 0-9
"""

class morsecode:
        def __init__(self, user_input):
                self.user_input = user_input

        def encode(self):
                code1, code2 = "", ""
                for word in self.user_input.split(" "):
                        for x in word:
                                x = x.upper()
                                b = morse['{0}'.format(x)]
                                code1 = code1 + b + " "
                        code2 = code2 + code1 + "/ "
                        code1 = ""
                x = len(code2)
                x = x - 3
                print(code2[:x])

        def decode(self):
                decrypted_code1, decrypted_code2 = "", ""
                for word in self.user_input.split(' / '):
                        for letter in word.split(' '):
                                x = inv_morse['{0}'.format(letter)]
                                decrypted_code1 = decrypted_code1 + x
                        decrypted_code2 = decrypted_code2 + decrypted_code1 + " "
                        decrypted_code1 = ""
                print(decrypted_code2)

morse= {'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
     	'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',
        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.' }

inv_morse = {v: k for k, v in morse.items()}

def main():
    choice = str(input("Would you like to encode or decode morse code? (E/D): "))
    if choice[0] == 'd' or choice[0] == 'D':
        user_code = str(input("Input your morse code, seperate words with a \" / \", and letters with a space :"))
        my_text = morsecode(user_code)
        my = my_text.decode()
        print(my)
    elif choice[0] == 'e' or choice[0] == 'E':
        user_code = str(input("Input your plaintext: "))
        my_text = morsecode(user_code)
        my = my_text.encode()
        print(my)

main()

#Pseudo code
#Setup dict of morse code values   *DONE*
#Take the user input *DONE*
#Split the user input into words by spilting using " / " *DONE*
#Further split the word by " " *DONE*
#Translate those split letters into ASCII letters *DONE*
#Make encode function *DONE*
#Make into class *DONE*