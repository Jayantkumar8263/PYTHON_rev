p = [2,1,2,3,4,1,4]

print(p)
#print(set(p))
#print(p.index(3))
u = 0
for i in p:
    u = u^i
print('unique element is :', u)