'''Write a Python program to reverse a tuple.'''

x = ('abc', 'def', 'ghi', 'jkl', 'mno')
y = list(x) 
print(tuple(y[::-1]))