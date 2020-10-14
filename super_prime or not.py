#prime1
##import math
##def is_prime(n):
##    if n==1:
##        return False
##    else:
##        x=int(math.sqrt(n))
##        for i in range(2,x+1):
##            if n%i==0:
##                return False
##        else:
##            return True
#print(is_prime(1))
from prime1 import is_prime
def position_prime(n):
    position=0
    for i in range(1,n+1):#11
      if is_prime(i):#11
          position+=1#5
    return position
if is_prime(7):
    if is_prime(position_prime(7)):
        print('super prime')
    else:
        print('not super')
else:
    print('not a prime')
