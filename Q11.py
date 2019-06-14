# Write a program which accepts a sequence of comma separated 4
# digit binary numbers as its input and then check whether they
# are divisible by 5 or not. The numbers that are divisible by 5
# are to be printed in a comma separated sequence.

binaries = input("Enter binary numbers separated by commas: ").split(",")

filteredbin = list(filter(lambda x: int(x,2) % 5 == 0, binaries));


print(",".join(filteredbin))
