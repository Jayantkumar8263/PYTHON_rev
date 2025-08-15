'''Write a Python program to find the index of an item in a specified list.'''

x = [2,3,4,5,6]
for i_index, i_var in enumerate(x) : 
    print(i_index, i_var)
    
print('the index of the item is : ', x.index(4))