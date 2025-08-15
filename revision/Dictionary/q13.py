'''Write a Python program to map two lists into a dictionary.'''

a = {
    'a': [1, 2, 3],
    'b': [4, 5, 6],
    'c': [7, 8, 9] 
}
print(a)
b = map(dict, zip(a['a'], a['b'], a['c']))
print(b)