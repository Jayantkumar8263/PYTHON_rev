''' Write a Python program to check if a set is a subset of another set '''

a = {11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
b = {16, 17, 18, 19, 20}
if b.issubset(a):
    print('true')
elif a.issubset(b):
    print('a is subset of b')

else:
    print('false')