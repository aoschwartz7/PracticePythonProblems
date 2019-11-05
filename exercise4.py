#Create a program that asks the user for a number and then prints out a list of all the divisors of that number.

num = input("enter a number and I will return its divisors: ")
num = int(num)

for x in range(1, num + 1):
    x = int(x)
    if num % x == 0:
        print(str(x) + " is a divisor of " + str(num))
