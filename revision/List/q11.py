'''Write a Python function that takes two lists and returns True if they have at least one common member.'''

a = input('Enter the list :')
b = input('Enter the list :')

for i in a and b :
    if i in a and b :
        print('common element', i)
    else:
        print('no common elements')
