#
# Write a program, which will find all such numbers between 1000 and 3000
# (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.



print(list((filter(lambda x: all(int(y) % 2 == 0 for y in x), [str(y) for y in range(1000, 3001)]))))