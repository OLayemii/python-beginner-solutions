# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106

number = input("Enter a number: ")
nums = []
for i in range(1,5):
    nums.append(number*i)
print(int(sum([int(x) for x in nums])))