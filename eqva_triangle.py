n=5
z=1
k=1
for i in range(1,n+1):
    for sp in range(n-i,0,-1):
        print(" ",end="")
    for j in range(1,k+1):
        print(z,end="")
    print()
    z+=1
    k+=2
