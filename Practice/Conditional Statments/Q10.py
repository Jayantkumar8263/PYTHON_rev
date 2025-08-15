'''Write a Python program that iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for multiples of five print "Buzz". For numbers that are multiples of three and five, print "FizzBuzz".'''

x = []
for x in range(0, 50):
    if (x % 3 == 0) :
        print('Fizz', x)
    elif (x % 5 == 0) :
        print('buzz',x)
    elif(x % 3 == 0 and x % 5 == 0) :
        print('Fizzbuzz', x)
else:
    print('Invalid', x)