import string
n=int(input("enter the range"))
alph=string.ascii_lowercase
l=[]
for i in range(n):
    l.append("-".join(alph[n-1:i:-1]+alph[i:n]).center(9,"-"))
for i in range(len(l)-1,0,-1):
    print(l[i])
for j in range(len(l)):
    print(l[j])
