#code using function
##n=1000001
##seive=[1 for i in range(n)]
##def seivegenerate():
##    i=2 
##    while(i*i<=n):#2*2=4<=25 True
##        if seive[i]==1:#seive[2]==1 True
##            for j in range(i*i,n,i):#2*2=4
##                seive[j]=0#
##        i+=1 
##    seive[0]=0
##    seive[1]=0
##n=int(input())#5 
##seivegenerate()
##if seive[n]==1:
##    print("prime")
##else:
##    print('not prime')

#code
n=1000001
seive=[1 for i in range(n+1)]
seive[0]=0
seive[1]=0
i=2 
while(i*i<=n):#2*2=4<=25 True
    if seive[i]==1:#seive[2]==1 True
        for j in range(i*i,n+1,i):#2*2=4
            seive[j]=0#
    i+=1 
x=int(input())#5 
if seive[x]==1:
    print("prime")
else:
    print('not prime')
















