'''Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.'''

def file():
    try :
        file = open('file', 'r')
        content = file.read()
        print(content)
        file.close()
    except:
        print('FileNotFound')
file()