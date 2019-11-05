# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
# Extras:
# If the number is a multiple of 4, print out a different message.

def equalorodd(num):
    num = input("Enter a number: ")
    num = int(num)
    if num % 2 == 0:
        print("your number is even")
        if num % 4 == 0:
            print("your number is also a multiple of 4")
    else:
        print("your number is odd")

equalorodd(5)
