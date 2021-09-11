class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m=len(text1)
        n=len(text2)
        ans=0
        dp=[[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if text1[i]==text2[j]:
                    dp[i][j]=dp[i-1][j-1]+1 if i>0 and j>0 else 1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1]) if i>0 and j>0 else 0
                ans=max(ans,dp[i][j])

        return ans

x=Solution()
print(x.longestCommonSubsequence(text1 = "oxcpqrsvwf", text2 = "shmtulqrypy"))