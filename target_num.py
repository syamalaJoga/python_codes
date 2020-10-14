#smaller than the current number
#Given an array of integers nums and an integer target, 
##return indices of the two numbers such that they add up to target.
##You may assume that each input would have exactly one solution, 
##and you may not use the same element twice.
##You can return the answer in any order.
##Example 1:
##Input: nums = [2,7,11,15], target = 9
##Output: [0,1]
##Output: Because nums[0] + nums[1] == 9, we return [0, 1].
##Example 2:




nums=[2,3,1,2,4,3]
t=7
i=0
cur_sum=0
z=[]
for j in range(0,len(nums)):
    cur_sum+=nums[j]
    while(cur_sum>=5):
        z.append(len(nums[i:j+1]))
        cur_sum-=nums[i]
        i+=1
print(min(z))
            
