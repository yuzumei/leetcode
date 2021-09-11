# -*- coding:utf-8 -*-
# @Author : Yuzu
# @Time : 2021/9/5 14:03
# @file : 5847.py
class UF:
    def __init__(self, n):
        self.parents = {i : i for i in range(n)}

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def merge(self, x, y):
        self.parents[self.find(x)] = self.parents[self.find(y)]

class Solution:
    def findFarmland(self, land):
        def func(nums):
            t = len(nums)
            s = nums.pop(0)
            cnt = 1
            while cnt < n and nums:
                if nums.pop(0) != s + cnt:
                    break
                cnt += 1
            q = t // cnt
            i = s // n
            j = s - n * i
            return [i, j, i + q - 1, j + cnt - 1]

        import collections
        m, n = len(land), len(land[0])
        uf = UF(m * n)
        dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for i in range(m):
            for j in range(n):
                if land[i][j] == 1:
                    for d in dir:
                        ni, nj = i + d[0], j + d[1]
                        if 0 <= ni < m and 0 <= nj < n and land[ni][nj] == 1:
                            uf.merge(ni * n + nj, i * n + j)
        memo = collections.defaultdict(list)
        for i in range(m):
            for j in range(n):
                if land[i][j] == 1:
                    memo[uf.find(i * n + j)].append(i * n + j)
        ans = []
        for item in memo:
            ans.append(func(memo[item]))
        return ans

x = Solution()
print(x.findFarmland(land = [[1,1],[0,0]]))