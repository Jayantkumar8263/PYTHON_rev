'''Write a Python program to check if each number is prime in a given list of numbers. Return True if all numbers are prime otherwise False.'''

x = [1,2,3,4,5]
for i in x :
    if i % i == 0 and i % 1 == 0:
        print([i])