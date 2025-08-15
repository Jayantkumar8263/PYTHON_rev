'''Write a Python program to find the list of words that are longer than n from a given list of words.'''

a = input('Enter the list :')
n = input('Enter the length of the word :')
b = []
for x in a :
    if len(x) > n:
        print('words which are greater than n :', (b.append(x)))
    else:
        print('words which are less than or equal to n :',(a))