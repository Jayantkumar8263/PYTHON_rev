''' Write a Python program to read an entire text file.'''

def file_read(fname):
        txt = open(fname, 'w+')
        print(txt.read())

file_read('Q1.txt')
