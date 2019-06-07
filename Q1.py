# Question:
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

result = list(filter(lambda x: x % 7 == 0 and x % 5 != 0, range(2000, 3201)))

print(",".join(str(x) for x in result))