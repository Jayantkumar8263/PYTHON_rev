'''Write a Python program that executes a list operation and handles an AttributeError exception if the attribute does not exist.'''

my_list = [2, 3]
my_tuple = (1, my_list)
my_tuple[1].append(4)
print(my_tuple)