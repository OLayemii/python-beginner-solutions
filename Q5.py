# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.


class MyClass():
    def __init__(self):
        self.mystr = ""
    def getString(self):
        self.mystr = input("Enter a text")
    def printString(self):
        print(self.mystr.upper())


myc = MyClass();

myc.getString()

myc.printString()