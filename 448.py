nums=[4,3,2,7,8,2,3,1]
for i in range(len(nums)):
    if nums[i]>0:
        nums[nums[i] - 1]=-nums[nums[i]-1] if nums[nums[i] - 1]>0 else nums[nums[i] - 1]
    else:
        nums[-nums[i] - 1] = -nums[-nums[i] - 1] if nums[-nums[i] - 1] > 0 else nums[-nums[i] - 1]
ans=[]
for i in nums:
    if nums[i]<0:
        ans.append(i)
return ans