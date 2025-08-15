'''Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even number. The numbers obtained should be printed in a comma-separated sequence.'''

for x in range(100, 400):
    if x % 2 == 0:
        print(x, end=',')