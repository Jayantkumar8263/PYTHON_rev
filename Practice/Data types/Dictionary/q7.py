'''Write a Python script to merge two Python dictionaries.'''

x = {
    1 : 2,
    2 : 4,
}
y = {
    4 : 8, 
    6 : 7
}
print('dictionary 1 :', x)
print('dictionary 2 :', y)
x.update(y)
print(x)