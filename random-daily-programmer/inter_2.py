def main():
    #Print info, and input user name
    name = str(input("What is your name Demon Slayer: "))
    print("Watch out {0}! A demon is heading straight for you, what ever will you do?".format(name))
    #Setup alive variable, and item flags
    alive = 1
    win = 0
    spear = 0
    bible = 0
    userchoice = (str(input("Quickly deice on your action (A) Run away (B) Open the chest to your left "
                            "(C) Attack the beast: ")))
    if userchoice == 'A' or userchoice == 'a':
        print("You run away with all your might, passing through the doors.")
        print("You slam the door shut behind you, you are in an armory, what do you do?")
        userchoice2 = (str(input("(A) Hide behind the door ready to ambush the creature, (B) Pick up the spear: ")))
        if userchoice2 =='A' or userchoice2 == 'a':
            print("The demon smashes the door down, as the door swings open on its hinge it crushes you to death.")
            alive = 0
        if userchoice2 =='B' or userchoice2 =='b':
            spear = 1
            print("You pick the spear up as the Demon smashes the door down, it is time to fight!")
            print("You charge, stabbing the Demon in it's black heart!")
            print("The Demon falls over, guts spilling out upon the floor!")
            win = 1


    if userchoice == 'B' or userchoice == 'b':
        userchoice3 = str(input("You open the chest, there is a bible in there. Do you take it? (Y/N): "))
        if userchoice3 == 'Y' or userchoice3 == 'y':
            print("You take the bible.")
            bible = 1
        if userchoice3 == 'n' or userchoice3 == 'n':
            print("You ignore the bible.")
        if bible == 1:
            print("The Demon rushes at you as you rise the bible up. A bright white light emits from the bible.")
            print("The light fades away and you open your eyes, the Demon is gone!")
            win = 1
        if bible == 0:
            print("The Demon rushes at you, it tears into your soft flesh.")
            alive = 0

    if userchoice == 'C' or userchoice == 'c':
        print("You charge at the Demon, it smashes into you with all its weight sending you flying across the room.")
        alive = 0

    if alive == 0:
        print("You died, game over!")
    if win == 1:
        print("You won, the demon is slain!")

main()