'''Write a Python program to convert a given list of tuples to a list of lists.
Original list of tuples: [(1, 2), (2, 3), (3, 4)]
Convert the said list of tuples to a list of lists: [[1, 2], [2, 3], [3, 4]]
Original list of tuples: [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
Convert the said list of tuples to a list of lists: [[1, 2], [2, 3, 5], [3, 4], [2, 3, 4, 2]]'''

a = [(1, 2), (2, 3), (3, 4)]
b = [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
print(list(map(list , a)))
print(list(map(list , b)))
print(map(a, (1, 2)))

#here we are using map() and list() functions to convert the list of tuples to list of lists.
#map() function is used to apply the list() function to each element of the list of tuples.
#list() function is used to convert the tuple to list.