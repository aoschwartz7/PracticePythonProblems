#Create a program that asks the user to enter their name and their age.
#Print out a message addressed to them that tells them the year that they will turn 100 years old.

def turn100(name, age):
    name = input("Please enter your name: ")
    age = input("Please enter your age: ")
    centuryold = 2019 +(100-int(age))
    print(name + ", if you're " + str(age) + " years old, you will turn 100 in " + str(centuryold))

turn100("name","age")
