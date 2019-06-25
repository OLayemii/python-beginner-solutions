# Write a program that computes the net amount of a bank account based a transaction log
# from console input. The transaction log format is shown as following:
# D 100
# W 200
#
# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500
balance = 0
while True:
    s = input("Enter a log data: ")
    if not s:
        break
    else:
        s = s.split(" ")
        if s[0].upper() == "D":
            balance += int(s[1])
        elif s[0].upper() == "W":
            balance -= int(s[1])

print(balance)