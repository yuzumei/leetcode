nums=[2,7,9,3,1]
f=[0]*len(nums) #偷了
g=[0]*len(nums) #没偷
f[0]=nums[0]
f[1]=max(nums[0],nums[1])
g[1]=f[0]
for i in range(2,len(nums)):
    f[i]=max(f[i-2],g[i-1])+nums[i]
    g[i]=max(f[i-1],g[i-1])
print(max(f[-1],g[-1]))