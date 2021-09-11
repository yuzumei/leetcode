# -*- coding:utf-8 -*-
# @Author : Yuzu
# @Time : 2021/9/5 22:00
# @file : 20.py
class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        dp=[[0]*n for _ in range(n)]
        ans=0
        for i in range(n):
            for j in range(i+1):
                if i==j:
                    dp[i][j]=1
                else:
                    if s[i]!=s[j]:
                        dp[i][j]=0
                    else:
                        dp[i][j]=1 if i-j==1 else dp[i-1][j+1]
                if dp[i][j]==1:
                    ans += 1
        return ans

x = Solution()
print(x.countSubstrings(s = "fdsklf"))