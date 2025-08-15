'''Write a Python program to print a tuple with string formatting.
Sample tuple : (100, 200, 300)
Output : This is a tuple (100, 200, 300)'''

x = ('a', 'b', 'c', 'd', 'e')   
x = tuple(x)
print('This is a tuple', x)
x= list(x)
print('This is a list', x)
x = str(x)
print('This is a string', x)
#x = dict(x)
#print('This is a dictionary', x)
