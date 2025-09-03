'''Write a Python program to append text to a file and display the text.'''

a = open('case.txt', 'w+')
b = a.write('hello, user this ia a text file')
c = a.read(b)
print(b)
print(c)
a.close()