'''Write a Python program to read a file line by line store it into a variable.'''

with open('case.txt', 'r+') as f :
    file = f.readline()
    print(file)