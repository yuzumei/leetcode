nums1 = [2,1,-2,5]
nums2 = [3,0,-6]
m=len(nums1)
n=len(nums2)
dp=[[0]*n for _ in range(m)]

for i in range(m):
    for j in range(n):
        xij=nums1[i]*nums2[j]
        dp[i][j]=xij
        if i>0:
            dp[i][j]=max(dp[i-1][j],dp[i][j])
        if j>0:
            dp[i][j]=max(dp[i][j-1],dp[i][j])
        if i>0 and j>0:
            dp[i][j]=max(dp[i-1][j-1]+xij,dp[i][j])

return dp[-1][-1]