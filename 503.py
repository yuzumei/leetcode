nums=[2,41,13,4,1,3,6,12,7,1,0,4,1,0,1,2,4,5,23,1,3,5]
ans=[-1]*len(nums)
stack=[]
for j in range(2*len(nums)):
    i=j%len(nums)
    while stack and nums[stack[-1]]<nums[i]:
        temp=stack.pop()
        ans[temp]=nums[i]
    stack.append(i)
print(ans)