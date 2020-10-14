n=30
sum=0
for i in range(1,n-1):
    if n%i==0:
        sum=sum+i
##print(sum)
if sum>n:
    print("abundent number")
else:
    print("not abundent number")
