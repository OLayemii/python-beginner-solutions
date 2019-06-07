# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.

def fac(n):
    return 1 if n == 1 else n * fac(n-1)