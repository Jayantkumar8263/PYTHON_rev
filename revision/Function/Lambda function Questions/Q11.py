'''Write a Python program to rearrange positive and negative numbers in a given array using Lambda.
Original arrays:  [-1, 2, -3, 5, 7, 8, 9, -10]'''

A = [-1, 2, -3, 5, 7, 8, 9, -10]
sorted_A = sorted(A, key=lambda point : point)
print(sorted_A)