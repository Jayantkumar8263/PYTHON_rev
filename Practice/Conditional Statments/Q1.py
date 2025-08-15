'''Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included).'''

#x = []
for x in range(1500, 2700):
    if (x % 7 == 0) and (x % 5 == 0) :
        print(x)
        
    else :
        print("Invalid")
