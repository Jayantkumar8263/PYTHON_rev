''' Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.'''

x = {
    y : y**2
    for y in range(1, 16)
}
print(x)