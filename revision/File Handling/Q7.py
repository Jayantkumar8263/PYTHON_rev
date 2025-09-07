'''Write a Python program to read a file line by line store it into an array.'''

with open('text.txt', 'r+') as r : 
    data = r.readlines()
    print(data)