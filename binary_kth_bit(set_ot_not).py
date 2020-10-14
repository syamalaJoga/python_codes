#using_function
##def set_or_unset(n, k):
##    if n & (1 << (k - 1)):
##        print("set") 
##    else:
##        print("unset")
##	
##n = int(input("Enter the number : "))
##k = int(input("Enter the Kth value : "))
##set_or_unset(n, k)





#usig_list(string)
##n=int(input("enter the number: "))
##k=int(input("enter the kth value: "))
##a=[]
##while n:
##    temp=n&1
##    a.append(temp)
##    a=a[::-1]
##    n=n>>1
####print(a)
##if a[k]==1:
##    print("set")
##else:
##    print("unset")





##3rd_method
##n=17
##k=2
##n=n>>k-1
##if n&1==1:
##    print("true")
##else:
##    print("False")




#4th_mehtod
##n=16
##k=2
##n=bin(n)
##n=n[2:]
##n=n[::-1]
###print(n)
##for i in range(len(n)):
##    if i==k-1:
##        if n[i]=="1":
##            print("true")
##            break
##else:
##    print("False")





#5th_method
def set_bit(n,k):
    n=n>>k-1
    if n & 1==1:
        return True
    return False
n=11
k=2
print(set_bit(n,k))
