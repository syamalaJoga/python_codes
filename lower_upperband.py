##lis=[2,1,3,6,7,5,4,9,8]
##key=3
##
##step1-->sort that list
##lis.sort()-->
##[1,2,3,4,5,6,7,8,9]
## 0 1 2 3 4 5 6 7 8 -->index
## i     j m              
##                  
##step2-->
##lowe_bound-->i=0
##upper_bound-->j=len(lis)-1=8
##mid-->m-->(i+j)//2-->8//2-->4
##check-->if lis[m]==key-->5==9-->F
##	display-->yes
##	stop
##elif lis[m]<key:-->5<3-->F
##	i=m+1-->8
##else:
##	j=m-1
