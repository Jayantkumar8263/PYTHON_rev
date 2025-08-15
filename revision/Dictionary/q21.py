'''Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.
Sample data : {'1':['a','b'], '2':['c','d']}'''

x = {
    '1':['a','b'], '2':['c','d']
}
for i in x['1']:
    for j in x['2']:
        print(i+j)

