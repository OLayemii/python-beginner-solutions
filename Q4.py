# Write a program which accepts a sequence of comma-separated numbers
# from console and generate a list and a tuple which contains every number.

numbers = input("Enter comma separated numbers")

nlist = list(numbers.replace(",",""))

print(list(nlist))
print(tuple(nlist))