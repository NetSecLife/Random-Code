def main():
    #print program info
    print("This script will calculate the three possible variables of Force, Mass, Acceleration based off the input "
          "of 2 integer variables")
    #Ask if user wants F M A
    choice = str(input("Would you like to calculate Force, Mass, or Acceleration (F/M/A): "))
    #collect input based off selection and parse into function, print results
    if choice[0] == 'F' or choice[0] == 'f':
        #F = M * A
        mass = int(input("Input the mass: "))
        acceleration = int(input("Input the acceleration: "))
        force = mass * acceleration
        print("The force is", force)
    elif choice[0] == 'M' or choice[0] == 'm':
        acceleration = int(input("Input the acceleration: "))
        force = int(input("Input the force: "))
        mass = force / acceleration
        print("The mass is", mass)
    elif choice[0] == 'A' or choice[0] == 'a':
        mass = int(input("Input the mass: "))
        force = int(input("Input the force: "))
        acceleration = force / mass
        print("The acceleration is", acceleration)
    else:
        print("Please input a valid character")
main()