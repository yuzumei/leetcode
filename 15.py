nums = [-1,0,1,2,-1,-4]
ans=[]
nums.sort()
n=len(nums)
for i in range(len(nums)):
    if i>0 and nums[i]==nums[i-1]:
        continue
    left=i+1
    right=n-1
    while left<right:
        if nums[i]+nums[left]+nums[right]==0:
            ans.append([nums[i],nums[left],nums[right]])
            temp=nums[left]
            while left<n and nums[left]==temp:
                left+=1
            temp=nums[right]
            while right>0 and nums[right]==temp:
                right-=1
        elif nums[i]+nums[left]+nums[right]>0:
            temp = nums[right]
            while right>0 and nums[right]==temp:
                right -= 1
        elif nums[i]+nums[left]+nums[right]<0:
            temp = nums[left]
            while left<n and nums[left]==temp:
                left += 1
print(ans)