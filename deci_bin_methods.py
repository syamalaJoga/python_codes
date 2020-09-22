#1stmethod
##n=5
##s=bin(n)
##res=0
##for i in s[2:]:
##    if i=="1":
##        res+=1
##print(res)

#2nd_method
##n=5
##res=0
##c=0
##while n:
##    if n%2!=0:
##        res+=1
##    n=n//2
##print(res)



#3rd_method
n=15
res=0
while n:
    n=n&(n-1)
    res+=1
print(res)
    
