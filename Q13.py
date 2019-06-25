# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3

import re

word = input("Enter a word: ")

print(f"LETTERS {len(re.findall(r'[A-Za-z]', word))}")
print(f"DIGITS {len(re.findall(r'[0-9]+', word))}")