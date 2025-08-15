'''Write a Python function to find the maximum of three numbers.'''

def maximum(a,b,c):
    '''if a > b and a > c :
        print('maximum of these numbers is :',a)
        return(a)
    elif b > a and b > c :
        print('maximum of these numbers is :',a)
        return(b)

    elif c > b and a < c :
        print('maximum of these numbers is :',a)
        return(c)'''
    print(max(a, b, c))
maximum(1, 2, 3)