''' Write a Python program to print the even numbers from a given list.
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]'''

def even(E):
    return(E)
x  = input('enter the list :')
for i in x :
    if i % 2 == 0 :
        print(i, 'is an even number')
    else:
        print(i, 'is not even number')
even(x)