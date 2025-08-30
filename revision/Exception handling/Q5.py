'''Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue.'''

def files(x):
    try:
        with open(x, 'w') as file:
              x = file.read()
              print(x)
    except:
        print('PermissionError')