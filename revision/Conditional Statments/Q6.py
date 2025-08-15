'''Write a Python program to count the number of even and odd numbers in a series of numbers
Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) '''

x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
for i in x :
    if i % 2 == 0:
        print('x is an even number :', i)
    
    elif i % 2 != 0 :
        print('x is an odd number :', i)

else:
    print("invalid")