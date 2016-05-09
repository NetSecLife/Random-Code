def main():
    #guess start
    guess = 50
    ceiling = 101
    floor = 0
    correct = 0
    #while loop going through numbers till guess is correct
    while correct == 0:
        #guess equals random int between ceiling and floor
        guess = int((ceiling +floor)/2)
        print("Is your number",str(guess),"(yes, higher, lower): ")
        userinput = input()
        if userinput[0] == 'y' or userinput[0] == 'Y':
            correct = 1
        elif userinput[0] == 'h' or userinput[0] == 'H':
            floor = guess
        elif userinput[0] == 'l' or userinput[0] == 'l':
            ceiling = guess
main()