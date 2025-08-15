'''Write a Python program to remove an empty tuple(s) from a list of tuples.
Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']'''

x = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
x.remove(x[0]), x.remove(x[0])
print(x)