#Ask the user for a string and print out whether this string is a palindrome or not.
#(A palindrome is a string that reads the same forwards and backwards.)

word = input("Enter a word and see if it is a palindrome: ")
paltest = word[::-1]
if word == paltest:
    print(word, paltest)
    print(word + " is a palindrome.")
else:
    print(word, paltest)
    print(word + " is not a palindrome.")
