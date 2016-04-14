from bs4 import BeautifulSoup
import urllib.request

def scrape_headlines(soup):
    #Constrains to the headline section
    headlines = soup.find("ol")
    #For loop through headlines
    for heading in headlines:
        #Get rid of whitespace, then collect the data
        if heading == "\n":
            continue
        headline = heading.find("a").getText()
        description = heading.find("p").getText()
        for z in heading.find_all('a', href=True):
            url = (z['href'])
        #Pretty output
        Headline = "Headline: " + headline + "."
        Description = "Description: " + description
        URL = "URL: http://www.abc.net.au" + url
        print(Headline)
        print(Description)
        print(URL + "\n")

def main():
    #Open website and assign the source code to html
    with urllib.request.urlopen('http://www.abc.net.au/news/') as response:
        html = response.read()
    #Setup soup variable for harvesting
    soup = BeautifulSoup(html, 'html.parser')
    scrape_headlines(soup)

if __name__ == '__main__':
    main()

#Logic flow.
#Open site with urllib
#Assign site code to html variable
#Soup the html
#Constrain soup to the first <ol> tags
#For loop
#Gather the headline
#Gather the description
#Gather the url
#Add global abc site url to url variable
#Put together and output