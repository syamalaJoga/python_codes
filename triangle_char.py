##n=5
##x=64
##for i in range(1,n+1):
##    for j in range(n+1,i,-1):
##        print(chr(i+x),end="")
##    print()







n=5
x=64
for i in range(1,n+1):
    for j in range(1,n-1,-1):
        print(chr(j+x),end="")
    print()
