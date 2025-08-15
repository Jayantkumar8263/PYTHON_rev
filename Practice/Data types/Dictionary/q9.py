'''Write a Python program to iterate over dictionaries using for loops.'''

a = {
    'name' : 'Abc',
    'age' : 19,
    'add' : 'def'
}
for values in a :
    print(values, a[values])
    
print(a)