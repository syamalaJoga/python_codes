A=[1,2,3,4,2,5,4,3,2]
y=sorted(A)
if len(A)<3:
    print(False)
elif A==y or A[::-1]==y:
    print(False)
else:
    A.append(-1)
    for i in range(len(A)-1):
        if A[i]<A[i+1]:
            A[i]=0
        elif A[i]>A[i+1]:
            A[i]=1
        else:
            print(False)
            break
    del A[-1]
    x=sorted(A)
    if A==x:
        print(True)
    else:
        print(False)
#print(arr)
#arr=[0,0,0,0,1,1,1,1]
