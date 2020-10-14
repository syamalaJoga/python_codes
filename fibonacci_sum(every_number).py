from math import sqrt
def is_sqrt(a):
    x1=sqrt(a)
    if x1==int(x1):
        return True
    return False
def is_fibo(n):
    x=5*(n**2)-4
    y=5*(n**2)+4
    if is_sqrt(x) or is_sqrt(y):
        return n
def near_fibo(n,i=1):
    if is_fibo(n-i):
        return n-i
    i+=1
    return near_fibo(n,i)
n=0
while 1:
    if is_fibo(n):
        print(n)
        break
    else:
        r=near_fibo(n)
        n=n-r
        print(r)

    
