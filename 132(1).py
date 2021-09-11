s="fifgbeajcacehiicccfecbfhhgfiiecdcjjffbghdidbhbdbfbfjccgbbdcjheccfbhafehieabbdfeigbiaggchaeghaijfbjhi"
class Solution:
    def minCut(self, s: str) -> int:
        dp=[[False]*len(s) for _ in range(len(s))]
        import collections
        memo=collections.defaultdict(list)
        for i in range(len(s)):
            for j in range(i+1):
                if s[i]==s[j]:
                    if i-j<=1:
                        dp[i][j]=True
                    else:
                        dp[i][j]=dp[i-1][j+1]
                if dp[i][j]:
                    memo[i].append(j)
        f=[float('inf')]*len(s)
        f[0]=0
        for i in range(1,len(s)):
            for item in memo[i]:
                if item==0:
                    f[i]=0
                    break
                f[i]=min(f[i],f[item-1]+1)
        return f[-1]
x=Solution()
print(x.minCut(s))