''' Write a Python program to construct the following pattern, using a nested for loop.

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
* '''

for i in range(1, 6):
    print('* ' * i)

for i in range(4, 0, -2):
    print('* ' * i)