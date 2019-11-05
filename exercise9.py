# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
# Extras:
# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random

ran = random.randint(1, 9)
count = 0

stop = False
while(not stop):

    num = input("Guess a number between 1 and 9, including 9, and see if it matches the random number: ")

    count +=1

    if int(num) == int(ran):
        print(("Congratulations! You typed {} and the random number is {}.".format(num,ran)))
        print("It took you {} guess(es).".format(count))
        break

    elif int(num) <= int(ran):
        print("You guessed too low")
    else:
        print("You guessed to high")

    answer = input("Do you wish to exit? Y/N. ")
    if answer == "Y":
        print("Game over.")
        stop = True
    else:
        stop = False
