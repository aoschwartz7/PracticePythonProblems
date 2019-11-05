# Make a two-player Rock-Paper-Scissors game.
# (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner,
# and ask if the players want to start a new game)

import time

#boolean variable to stop the While loop
stop = False

while(not stop):

    print("Ready to play Rock-Paper-Scissors?")
    time.sleep(2)

    answerp1 = input("Player One, enter a move. Rock, Paper, or Scissors: ")
    time.sleep(1)

    answerp2 = input("Player Two, enter a move. Rock, Paper, or Scissors: ")
    time.sleep(1)

    if answerp1 == 'Rock' and answerp2 =="Scissors":
        print("Player One wins! Rock beats Scissors.")
    if answerp1 == 'Rock' and answerp2 =="Paper":
        print("Player Two wins! Paper beats Rock.")
    if answerp1 == 'Paper' and answerp2 =="Scissors":
        print("Player Two wins! Scissors beats Paper.")
    if answerp1 == 'Paper' and answerp2 =="Rock":
        print("Player One wins! Paper beats Rock.")
    if answerp1 == 'Scissors' and answerp2 =="Paper":
        print("Player One wins! Scissors beats Paper.")
    if answerp1 == 'Scissors' and answerp2 =="Rock":
        print("Player Two wins! Rock beats Scissors.")

    answer = input("Do you want to play again? Yes/No. ")

    if answer == "Yes":
        print("A new game will start now.")
        time.sleep(1)
    elif answer == "No":
        print("Game over!")
        stop = True
    else:
        print("Try again, and make sure to use correct word: Yes or No.")
