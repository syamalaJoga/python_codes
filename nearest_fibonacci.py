def fibo_series(n):
    a=0
    b=1
    x=n
    n=n-2
    while True:
        c=a+b
        a,b=b,c
        if c>x:
            break
    return a,b
n=3
n2,n3=fibo_series(n)
if abs(n-n2)<abs(n-n3):
    print(n2)
else:
    print(n3)
