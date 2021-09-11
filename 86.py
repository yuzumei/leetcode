# -*- coding:utf-8 -*-
# @Author : Yuzu
# @Time : 2021/9/10 23:38
# @file : 86.py
class Solution:
    def partition(self, s: str):
        n = len(s)
        memo = dict()
        for i in range(n):
            memo[i] = []
            for j in range(i, n):
                if s[i: j + 1] == s[i: j + 1][::-1]:
                    memo[i].append(j)
        ans = []
        def dfs(i, res):
            if i == n:
                ans.append(res)
                return
            for index in memo[i]:
                temp = res + [s[i : index + 1]]
                dfs(index + 1, temp)
        dfs(0, [])
        return ans

x = Solution()
print(x.partition('aaaaaaaa'))