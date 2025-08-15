'''Write a Python program to check if two given sets have no elements in common'''

x = {'apple', 'banana', 'cherry'}
y = {'apple', 'mango', 'grapes'}
if x.intersection(y) == {}:
    print('No common elements', x.intersection(y))
else:
    print('Common elements', x.intersection(y))
    