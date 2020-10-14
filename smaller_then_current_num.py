nums=[8,1,2,2,3]
arr=sorted(nums)
d={}
count=0
for i in range(len(nums)):
    if arr[i] not in d:
        d[arr[i]]=count
        count+=1
    else:
        count+=1
for i in range(len(nums)):
    nums[i]=d[nums[i]]
print(nums)
          




#input:nums[8,1,2,2,3]
##output:[4,0,1,1,3]
##explanation:
##for nums(0)=8 there exist four smaller numbers than it (1,2,2 and 3)
##for nums(1)=1 donot exist any smaller numbers than it

                                                        
