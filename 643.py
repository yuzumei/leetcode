nums=[1,12,-5,-6,50,3]
k = 4
left=0
right=k
temp=0
ans=sum(nums[0:k])/k
res=0
while right<len(nums):
    temp-=nums[left]
    temp+=nums[right]
    res=max(temp,res)
    left+=1
    right+=1
print(ans+res/k)
