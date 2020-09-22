def fibo(n):
    a=0
    b=1
    print(a,b,end="")
    i=2
    while True:
        c=a+b
        print(c,end=" ")
        a,b=b,c
        i+=1
        if i==n:
            break
fibo(10)
