'''Write a Python program to read a file line by line and store it into a list.
a = open('case.txt', 'r+')
#b = a.(' and I am dooing great.')
c = a.read()
#print(b)
print(c)
a.close()'''


with open('read.txt', 'w+') as f:
    #content_list = f.write('hi, there!')
    content = f.readline()
    #print(content_list)
    print(content)