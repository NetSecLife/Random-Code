from bs4 import BeautifulSoup
import urllib.request
from tkinter import *
from tkinter import ttk
"""Project Outline: Program that will scrabe the URLs on a user given website.
Once the function to do this has been created and works in console then build a GUI application for the program"""

def scrape_url(html):
    for link in html.find_all('a'):
        link = (link.get('href'))
        if link[0:4] == "http":
            print(link)
        else:
            print("http://www.google.com" + link)


def main():

    #CONSOLE START
    user_website = input("Input: ")
    try:
        with urllib.request.urlopen(user_website) as response:
            html = response.read()
    except:
        print("Please enter a valid website address")
        sys.exit()
    soup = BeautifulSoup(html, 'html.parser')
    scrape_url(soup)
    #CONSOLE END

main()



#Console app logic flow:
#Take user input for which URL is to be scraped
#Parse the input to the scrape url function
#Scrape the URL
#Print out the results

#GUI app logic flow:

