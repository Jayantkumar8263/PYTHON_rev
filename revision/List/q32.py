'''Write a Python program to check whether a list contains a sublist.'''

x = ['abc', 'def', 'ghi', 'jkl']
y = ['ghi', 'jkl']
Z = ['abc', 'def']


if y in x :
    print('y is a sublist of x ', y)
elif Z in x :
    print('z is a subset of x ', Z)
