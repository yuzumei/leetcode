nums=[1,2]
n=len(nums)
ans=nums+[1]
nums.insert(0,1)
for i in range(1,len(nums)):
    nums[i]*=nums[i-1]
for i in range(len(nums)-2,-1,-1):
    ans[i]*=ans[i+1]
for i in range(n):
    ans[i+1]*=nums[i]
print(ans[1:])
