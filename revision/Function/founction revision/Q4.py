'''Write a function `char_frequency(s)` that takes a string and returns a dictionary with the count of each character'''

def str_dict(x):
    empty_dict = {}
    for i in x :
        if i in empty_dict :
            empty_dict[i] += 1
        else:
            empty_dict[i] = 1
    return empty_dict
s = input('enter the string :')
counts = str_dict(s)
print(counts)