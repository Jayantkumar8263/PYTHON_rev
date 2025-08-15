'''Write a Python program to compute the element-wise sum of given tuples.
Original lists:
(1, 2, 3, 4)
(3, 5, 2, 1)
(2, 2, 3, 1)
Element-wise sum of the said tuples:
(6, 9, 8, 6)'''

a = (1, 2, 3, 4)
b = (3, 5, 2, 1)
c = (2, 2, 3, 1)

print(tuple(map(sum, zip(a, b, c))))

why are we using tuple(), map() and zip() functions here ?
