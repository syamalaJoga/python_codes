n=int(input('please enter the no. in decimal format: '))
x=n
k=[]
while (n>0):
    a=int(n%2)
    k.append(a)
    n=(n-a)/2
k.append(0)
string=" "
for j in k[::-1]:
    string=string+str(j)
#print(k)
    #print(string)
print(x,string)
