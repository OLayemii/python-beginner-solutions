import math
# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.

q = []
C = 50
H = 30
D = (input("Enter value for D: "))

d_array = [int(x) for x in D.split(",")]

for n in d_array:
    q.append(str(math.floor(math.sqrt((2*C*n)/H))))

print(",".join(q))

