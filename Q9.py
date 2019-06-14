# Write a program that accepts sequence of lines as input
# and prints the lines after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT

words = [];

while True:
    x = (input("Enter a word (Press enter to cancel): ").upper())

    if  x == "":
        for word in words:
            print(word)
        break

    words.append(x)