from sys import maxsize
l=[-2,-3,4,1,-2,-1,5,-3]
y=-maxsize-1
for i in range(len(l)):
    for j in range(i,len(l)):
        x=sum(l[i:j+1])
        if x>y:
           y=x
print(y)
