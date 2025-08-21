'''Write a Python program to sort a list of dictionaries using Lambda.

Original list of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
Sorting the List of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]

'''

d = [{'make': 'Nokia', 'model': '216', 'color': 'Black'}, 
     {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, 
     {'make': 'Samsung', 'model': '7', 'color': 'Blue'}]

sorted_d = sorted(d, key = lambda d: d['model'])
print('Orignal list of dictionary:', d)
print('Sorted List of dictionaries :',sorted_d)