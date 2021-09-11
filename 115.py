s = "babgbag"
t = "bag"
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        import collections
        memo=collections.defaultdict(list)
        for i,num in enumerate(t):
            memo[num].append(i)
        dp=[[0]*len(t) for _ in range(len(s))]
        # dp[0][0]=1 if s[0]==t[0] else 0
        for i,alpha in enumerate(s):
            # if i!=0:
            dp[i]=dp[i-1][:]
            if alpha in memo:
                temp=memo[alpha][::-1]
                for point in temp:
                    if point==0:
                        dp[i][point]+=1
                    else:
                        if dp[i][point-1]!=0:
                            dp[i][point]=dp[i][point-1]+dp[i-1][point]
        return dp[-1][-1]
x=Solution()
print(x.numDistinct(s,t))