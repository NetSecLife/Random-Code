"""This script converts a given integer date into the day it would represent"""
import calendar


def main():
    #Grab three inputs of day [1-31], month[1-12], year
    year = int(input("Please input the Year as an integer (Ex. 1970): "))
    month = int(input("Please input the Month as an integer (Ex. 5): "))
    day = int(input("Please input the day as an integer (Ex. 12): "))
    #Parse this to .weekday
    h = 0
    try:
        h = calendar.weekday(year,month,day)
    except:
        print("The date you entered is out of range. Please try again.")
        exit()
    #derive day from the number result of weekday
    day_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    print("The day selected is {0}.".format(day_list[h]))
main()
