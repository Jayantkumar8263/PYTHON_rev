'''Write a Python program to check whether an alphabet is a vowel or consonant.'''

x = input("enter the alphabet : ")
if x in ('a', 'e', 'i', 'o', 'u'):
    print("it's a vowel", x)
    
else:
    print('Invalid')