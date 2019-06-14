from pprint import pprint

# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
# The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡­Y-1.


vals = input("Enter value of X: ").split(",")

X = int(vals[0])
Y = int(vals[1])

arr = [[0 for y in range(0, Y)] for x in range(0, X)]


for i in range(0, X):
    for j in range(0, Y):
        arr[i][j] = i*j


pprint(arr)