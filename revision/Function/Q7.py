'''Write a Python function that accepts a string and counts the number of upper and lower case letters.
Sample String : 'The quick Brow Fox' '''
def count():
    a = input('enter the string :')
    for i in a :
        if i == i.upper():
            print('no. of capital letters are : ',i, len(i))
        elif i == i.lower():
            print('no. of small letters are : ',i, len(i))
count()