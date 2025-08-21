'''Write a Python program to access a function inside a function.'''

def Outer_fun():
    print(Outer_fun)
    def Inner_fun():
        print(Inner_fun)   
    Inner_fun()
Outer_fun()
