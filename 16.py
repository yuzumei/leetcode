nums = [-1,2,1,-4]
target = 1
nums.sort()
ans=float('inf')
flag=0
for i in range(len(nums)-2):
    left=i+1
    right=len(nums)-1
    if nums[i]+nums[left]+nums[right]>target:
        while left<right and nums[i] + nums[left] + nums[right] > target:
            ans=min(ans,abs(nums[i] + nums[left] + nums[right]-target))
            flag==1 if nums[i] + nums[left] + nums[right]>target
            left+=1

