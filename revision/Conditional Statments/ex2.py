'''Write a program that prints the sum of all the even numbers from 1 to 100 using a loop.'''

for i in range(1, 101):  
    if i%2 == 0 :
        print(i, "it's is even number")
    elif i % 2 != 0 :
        print(i, "it's is not even number")