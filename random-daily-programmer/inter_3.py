class quotes:
    def __init__(self, name, quote):
        self.name = name
        self.quote = str(quote)

    def getquote(self):
        print("It is known that {0} once said \"{1}\"".format(self.name,self.quote))

def main():
    a = quotes("Memelord","I am the meme")
    a.getquote()
main()