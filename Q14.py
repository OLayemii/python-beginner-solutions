# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9

from collections import defaultdict
import re

word = input("Enter a sentence: ")
counts = defaultdict(int)
for letter in word:
    if letter.isupper():
        counts["upper"] += 1
    elif letter.islower():
        counts["lower"] += 1
    else:
        pass

print(f"UPPER {counts['upper']}")
print(f"LOWER {counts['lower']}")

# Or i can use regex
upper = len(re.findall(r"[A-Z]", word))
lower = len(re.findall(r"[a-z]", word))

print(f"UPPER {upper}")
print(f"LOWER {lower}")