'''Write a Python program to guess a number between 1 and 9.
Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.'''

import random
a = int(input('enter a number :'))
x = random.randint(0,9)
if a == x:
    print(True)
if a != x :
    print(x)