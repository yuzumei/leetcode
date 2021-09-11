class Solution:
    def solve(self,n):
        dp=[0]*(n+1)
        dp[0],dp[1],dp[2]=0,0,1
        for i in range(3,n+1):
            dp[i]=min(max(dp[i-j]+1,j) for j in range(1,i))
        return dp
x=Solution()
print(x.solve(100))