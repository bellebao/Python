n = int(input("last number of fibonacci:\n"))
l=[]
a = 0
b = 1
l.append(a)
l.append(b)
for i in range(n-1):
    a, b = b, a+b
    l.append(b)

print (l)
 
