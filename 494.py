nums=[0,0,0,0,0,0,0,0,1]
k=1
n=sum(nums)
m=len(nums)
'''dp[i][j]到第i个数和为j的可能'''
dp=[[0]*(2*n+2) for _ in range(m)]
dp[0][nums[0]]+=1
dp[0][-nums[0]]+=1
for i in range(1,m):
    for j in range(-n,n+1):
        dp[i][j]=dp[i-1][j-nums[i]]+dp[i-1][j+nums[i]]
print(dp)