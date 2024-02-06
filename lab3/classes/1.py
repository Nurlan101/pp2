class abc:
    def getString(self, text):
        return text
    def printSring(self, text):
        print(self.getString(text).upper())

apple = abc() 
aplle.printSring(apple.getString(input()))